import pandas as pd
from django.core.management.base import BaseCommand
from countries.models import Country, PM25Record, CountryMetadata

class Command(BaseCommand):
    help = "Load PM2.5 data and metadata from Excel file into the database"

    def add_arguments(self, parser):
        parser.add_argument('filepath', type=str, help='Path to the Excel file')

    def handle(self, *args, **kwargs):
        filepath = kwargs['filepath']
        self.stdout.write(f"Reading file: {filepath}")

        # === Load PM2.5 Data Sheet ===
        df = pd.read_excel(filepath, sheet_name='Data', skiprows=3, engine='openpyxl')
        df.dropna(axis=1, how='all', inplace=True)
        df.dropna(subset=["Country Name"], inplace=True)

        df_melted = df.melt(
            id_vars=["Country Name", "Country Code", "Indicator Name", "Indicator Code"],
            var_name="Year",
            value_name="PM25_Level"
        )
        df_melted["Year"] = pd.to_numeric(df_melted["Year"], errors="coerce")
        df_melted.dropna(subset=["Year"], inplace=True)
        df_melted["Year"] = df_melted["Year"].astype(int)
        df_melted.dropna(subset=["PM25_Level"], inplace=True)

        for _, row in df_melted.iterrows():
            country, _ = Country.objects.get_or_create(
                code=row["Country Code"],
                defaults={"name": row["Country Name"]}
            )
            PM25Record.objects.update_or_create(
                country=country,
                year=row["Year"],
                defaults={"value": row["PM25_Level"]}
            )

        self.stdout.write(self.style.SUCCESS("PM2.5 data loaded successfully."))

        # === Load Metadata Sheet ===
        self.stdout.write("Loading country metadata...")
        meta_df = pd.read_excel(filepath, sheet_name='Metadata', engine='openpyxl')
        meta_df.dropna(subset=["Country Code", "Income Level"], inplace=True)

        for _, row in meta_df.iterrows():
            CountryMetadata.objects.update_or_create(
                code=row["Country Code"],
                defaults={"income_level": row["Income Level"]}
            )

        self.stdout.write(self.style.SUCCESS("Country metadata loaded successfully."))
