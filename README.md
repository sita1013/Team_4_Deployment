# Team 4 CS551Q Django App

Our project was to show the PM2.5 levels of each country for the years that were provided in the excel sheet.
The current website shows these levels and has drop down boxes dedicated to countries and years. There is a second
page where the user can compare two countries using a bar graph. 


## Features
- Hompage = 
  introduces the user to the site with two options to either search for country or compare two countries. 
- Search for Country =
  gives drop down option for the user to pick country and year. Also can start typing to get
  to the country or year more quickly. Page does allow for user to return to Homepage or Compare Two Countries page. 
- Compare Two Countries =
  provides two drop down menus for the user to choose for countries and another drop down menu
  for the user to choose year. Page allows for user to return to Homepage or Search for One Country again. 


## Folder Structure
mysite/ – Main Django project folder
- urls.py includes:
  -- Admin (default, not customized)
  -- Routes for the countries app
countries/ – Django app folder
- country_data/: Contains the PM2.5 Excel dataset
- management/commands/: Custom command parse_country to load data
- templates/countries/:
  - homepage.html
  - pm25_lookup.html
  - barchart_compare.html (uses Chart.js)
Core Python files:
- models.py: Two models – Country and PM25Record
- views.py: Three main view functions for the respective pages
- urls.py: Routes connected to the views
- tests.py

'mysite' is the project folder and 'countries' is the app folder. In 'mysite', 'url' path does contain admin, although 
we haven't added any admin details as of yet. The second url path is for the 'countries' folder for the app. The 
'countries' folder countains 'country_data', 'management/commands', and 'templates/countries' folders. 

'country_data' holds the excel file where all the data is stored. 'management/commands' holds a python folder for 'parse_country' to 
read the excel file data. 'templates/countries' contains three html files. First for the 'homepage', second for the 
'pm25_lookup' page, and third for the 'barchart_compare' page. 'barchart_compare' uses Chart.js to display the data 
in bar graphs but the other files only have html and django template language structures. 

Outside of these folders but still in 'countries' folder, we have 'models', 'tests', 'urls', and 'views' python files. 
In 'models', we have two classess. One being country and the second being PM25 Record. In 'tests', we have lKj;fa;lsdjfa;ldkjfa;sldfkjas;ldkjfa;lsdkjf;lasdkjfla;ksdjfasdl;kjf
In 'views', we have three main functions. The firs for the logic behind the 'homepage', the second for the logic behind
the 'pm25_lookup' page, and the third for the 'barchart_compare' page. From there are the 'urls', where they connect
to the functions in 'views'. 


## Technologies
Backend: Django 4.x
Frontend: HTML, Django Templates, Chart.js
Database: SQLite (development), PostgreSQL (intended for production)

## Notes
We initially planned to use PostgreSQL for deployment and API-driven frontend interactions.
Due to limitations in Codio, we used SQLite for development. We aim to shift to PostgreSQL for final deployment using VS Code or other cloud environments.


## License
This project is **not licensed** for public use or redistribution.  
All rights are reserved by the authors (Team 4, 2025).


## Installation
-must have python 3.12.2
```bash
git clone https://github.com/sita1013/Team_4_CS551Q-Final.git
cd Team_4_CS551Q-Final
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py parse_country countries/country_data/pm25_data.xlsx.xlsx
python manage.py runserver 0.0.0.0:8000
* then visit <https://aliasoctavia-bingochamber-8000.codio-box.uk/>
