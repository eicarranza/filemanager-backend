# File Manager -backend
FileManager is a microservices based application. This project is the backend app created with Django, which will provied services through django REST framework in order to by consumed by a frontend created in Angular to manage files (upload and visualize files).

[![](https://github.com/eicarranza/filemanager-backend/blob/main/img/home.jpg?raw=true)](https://github.com/eicarranza/filemanager-backend/blob/main/img/home.jpg?raw=true)

In order to improve the management of information and put into practice the knowledge acquired as a FullStack developer, this system is created which involves:

- Backend supported in Python Django. 
- Front End Angular

This project will also employ technologies such as:
- Django API Rest

License: BSD

##Settings
Download this project following the normal github convention. Download the  frontend project from [Front end Angular](https://github.com/eicarranza/filemanager-frontend.git "Front end Angular") 


##Dependences
Before to start the project, verify if you have already installed next dependences:
- Python 3.8
- Pip
- Python RestFramework


Download this project following the normal github convention. Download the  frontend project from [Front end Angular](https://github.com/eicarranza/filemanager-frontend.git "Front end Angular") 


Basic Commands
--------------


* To create an **superuser account**, use this command:

    `$ python manage.py createsuperuser`

* To import the project **seeds**, use this command:

    `$ python manage.py loaddata ./files/Fixture/fixture.json`

* Run backend project with:

    `$ python manage.py runserver`


Deployment
----------
This backend will configure the Django project, providing seeds to the application such as file size allowed, files type allowed, among other. 

- Download the repository from [here](https://github.com/eicarranza/filemanager-backend.git "here").

- Next, import seeds to the project:
`$ python manage.py loaddata ./files/Fixture/fixture.json`

- Create an **superuser account**, use this command:
`$  python manage.py createsuperuser`

- Finally, start the backend project:
`$ python manage.py runserver`

- Verify the project on next url:
`http://localhost:8000/admin/`
