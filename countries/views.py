from django.shortcuts import render
from .models import PM25Record, Country
from django.db.models import Max

def homepage(request):
    
    latest_year = PM25Record.objects.aggregate(Max('year'))['year__max']

    top_records = PM25Record.objects.filter(year=latest_year).order_by('-value')[:5]

    countries = [record.country.name for record in top_records]
    values = [record.value for record in top_records]

    return render(request, 'countries/homepage.html', {
        'countries_json': countries,
        'values_json': values,
        'latest_year': latest_year,
    })

def pm25_lookup_view(request):
    selected_country = request.GET.get('country')
    selected_year = request.GET.get('year')
    countries = Country.objects.order_by('name')
    years = PM25Record.objects.values_list('year', flat=True).distinct().order_by('year')
    record = None
    yearly_records = []
    year_list = []
    value_list = []
    country_name = ""
    if selected_country:
        yearly_records = PM25Record.objects.filter(
            country__code=selected_country
        ).order_by('year')
        year_list = [r.year for r in yearly_records]
        value_list = [r.value for r in yearly_records]
        if yearly_records:
            country_name = yearly_records[0].country.name
    if selected_country and selected_year:
        record = PM25Record.objects.filter(
            country__code=selected_country,
            year=selected_year
        ).first()
    context = {
        'countries': countries,
        'years': years,
        'selected_country': selected_country,
        'selected_year': selected_year,
        'record': record,
        'year_list': year_list,
        'value_list': value_list,
        'country_name': country_name,
    }
    return render(request, 'countries/pm25_lookup.html', context)

def barchart_compare(request):
    countries = Country.objects.order_by('name')
    years = PM25Record.objects.values_list('year', flat=True).distinct().order_by('year')
    selected_year = request.GET.get('year')
    country1_code = request.GET.get('country1')
    country2_code = request.GET.get('country2')
    record1 = record2 = None
    if selected_year and country1_code and country2_code:
        record1 = PM25Record.objects.filter(country__code=country1_code, year=selected_year).first()
        record2 = PM25Record.objects.filter(country__code=country2_code, year=selected_year).first()
    return render(request, 'countries/barchart_compare.html', {
        'countries': countries,
        'years': years,
        'selected_year': selected_year,
        'country1_code': country1_code,
        'country2_code': country2_code,
        'record1': record1,
        'record2': record2,
    })