# Team_4_CS551Q-Final
Team 4 application final version

The project currently displays each countries percentage of pollution. 
The front-page pulls from a html document under templates but the logic is in views. 
There's an option to look up each country or go to comparing two countries. Each option
has their own html documents under templates and the logic is also in views. The xlsx file is
currently under country data while the parsing file resides in management/commands. This enables 
the computer to read the file and display the information. There was an option to display the income rate 
as well but we decided to wait to do that because we have to deploy to the cloud and the app is possibly 
already too big. 

The sqlite3 is currently an issue and we are attempting to get it to interact with PostgreSQL....however, Codio 
is having a lot of issues with that right now. We may just have to deploy with our app using PostgreSQL
via one team member's VSCode and ignore Codio accept for turning in the assignment. 