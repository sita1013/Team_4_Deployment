import os
import tempfile
import pandas as pd
from django.core.management import call_command
from django.test import TestCase
from countries.models import Country, PM25Record, CountryMetadata
from django.urls import reverse

class SimpleURLTests(TestCase):
    def test_homepage_url(self):
        response = self.client.get(reverse('homepage'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'countries/homepage.html')

    def test_pm25_lookup_url(self):
        response = self.client.get(reverse('pm25_lookup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'countries/pm25_lookup.html')

    def test_barchart_compare_url(self):
        response = self.client.get(reverse('barchart_compare'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'countries/barchart_compare.html')


class PM25LoadCommandTests(TestCase):
    def setUp(self):
        # Create a temp file and close it immediately to avoid PermissionError on Windows
        self.temp_file = tempfile.NamedTemporaryFile(suffix=".xlsx", delete=False)
        self.temp_file.close()

        # PM2.5 data sheet
        pm25_df = pd.DataFrame({
            'Country Name': ['Testland'],
            'Country Code': ['TST'],
            'Indicator Name': ['PM2.5 air pollution'],
            'Indicator Code': ['EN.ATM.PM25.MC.M3'],
            '2000': [42.0],
            '2001': [43.0],
        })

        # Metadata sheet
        metadata_df = pd.DataFrame({
            'Country Code': ['TST'],
            'Region': ['Test Region'],
            'IncomeGroup': ['Test Income']
        })

        # Write both sheets to the Excel file
        with pd.ExcelWriter(self.temp_file.name, engine='openpyxl') as writer:
            pm25_df.to_excel(writer, index=False, sheet_name='Data')  # default startrow=0
            metadata_df.to_excel(writer, index=False, sheet_name='Metadata - Countries')

    def tearDown(self):
        # Remove the temp file after tests
        os.remove(self.temp_file.name)

    def test_pm25_load_command_creates_records(self):
        # Call the management command
        call_command('parse_country', self.temp_file.name)

        # Assert country was created
        self.assertTrue(Country.objects.filter(code='TST').exists())

        # Assert 2 PM2.5 records were created (for years 2000 and 2001)
        self.assertEqual(PM25Record.objects.filter(country__code='TST').count(), 2)

        # Assert metadata was created
        self.assertTrue(CountryMetadata.objects.filter(country__code='TST').exists())
