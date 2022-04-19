# Real-Time

## Author
>[Brian Otieno](https://github.com/Otybrian)  
  
# Description  
Tis is a neighborhood app where a user must signup first, be able to join a hood owned by the hood admin, and once you 
join a hood, one can see businesses and posts in only that wood they belong to.  

##  Live Link  
 Click [View Site] () to visit the site live

 ## User Story  
  
* Sign in with the application to start using.
* Set up a profile about me and a general location and my neighborhood name.
* Find a list of different businesses in my neighborhood.
* Find Contact Information for the health department and Police authorities near my neighborhood.
* Create Posts that will be visible to everyone in my neighborhood.
* Change My neighborhood when I decide to move out.
* Only view details of a single neighborhood.

## Screenshots 
###### Home page
At the homepage, user is able to visit login and signup pages. If an authenticated use
![Screenshot from 2022-04-19 19-43-49](https://user-images.githubusercontent.com/93243367/164054117-d7900028-34e0-4e39-9b33-79d1a3cf785b.png)
r, they are able to visit the existing hoods

![Screenshot from 2022-04-19 17-41-09](https://user-images.githubusercontent.com/93243367/164049367-d46c8d18-0cae-47ed-8deb-6cb079ecc257.png)

###### Profile
A user is able to view and update their profiles once signed in


###### Neighborhoods
Here the user is able to join a hood or create a new one. Once joine, a user is able to view details of the hood including businesses and posts by other people.
![Screenshot from 2022-04-19 17-37-56](https://user-images.githubusercontent.com/93243367/164049435-91a16549-9886-405a-8a21-d97e168297ab.png)



The user is also able to add new businesses and new posts which will only be seen by people from the same neighborhood.

###### Uploading
Users are able to make uploads in the pages screenshot below.
## Setup and Installation  
To get the project .......  
  
##### Cloning the repository:  
 ```bash 
https://github.com/Owiti-Charles/HoodWatch.git
```
##### Navigate into the folder and install requirements  
 ```bash 
cd Real-Time 
```
##### Install and activate Virtual  
 ```bash 
- python3 -m venv virtual - source virtual/bin/activate  
```  
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations hood
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  



## Technology used  
  
* [Python3.6](https://www.python.org/)  
* [Django 3.2.1](https://docs.djangoproject.com/en/2.2/)  
* [Heroku](https://heroku.com)  
  
  
## Known Bugs  
* There are no known bugs currently but pull requests are allowed incase you spot a bug  
  
## Contact Information   
If you have any question or contributions, please email me at [otbrayo@gmail.com]  
  
## License 

*MIT license
