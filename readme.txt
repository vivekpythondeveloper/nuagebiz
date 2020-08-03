I have created a Django project. 

please install Redis server v=6.0.6  in you pc so that my async task will run

database is sqllite3

create superuser by running the below command
python manage.py createsuperuser

To access the project, it is better to use a virtual directory as it will keep the django version in your computer and the one used in this project seperate.

Commands to use virtual directory in mac os:
python3 -m venv envnuagebiz

>>cd pathname or of project directory
>>source envnuagebiz\bin\activate 
>>cd to the project directory where your manage.py file is

Now you will be in the root directory of the project. You can run the server by this command:

>> python manage.py runserver


Check the following links after this server:

http://127.0.0.1:8000/nuagebiz/search (first page of search)
http://127.0.0.1:8000/nuagebiz/search?q=micromax tv   (page after searching the product)
http://127.0.0.1:8000/nuagebiz/search?page=2   (second page)