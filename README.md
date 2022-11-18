# Task App
_This is a task application with a CRUD. It has integrated user authentication_
##Built with🛠️
* [Django](https://www.djangoproject.com/)
* [DjangoRestFramework](https://www.django-rest-framework.org/)

## Instructions📋:
_How to get a copy of the project running on your local machine_
<strong>1.Clone the repository</strong>
```
git clone https://github.com/santiudev/taskAppDjango.git
```
<strong>2.Create a virtual environment</strong>
_From the cloned directory run:_
```
python -m venv env
```
<strong>3.Activate the virtualenv</strong>
On macOs or Linux:
```
source venv/bin/activate
```
On Windows:
```
env\scripts\activate
```
<strong>3.Install required requirements</strong>
```
pip install -r requirements.txt
```
<strong>4.Run migrations</strong>
```
python manage.py makemigrations
```
```
python manage.py migrate
```
<strong>5.Create an admin User</strong>
```
python manage.py createsuperuser
```
<strong>5.Run the application</strong>
```
python manage.py runserver
```

<strong><em>Feel free to test and modify it.</strong></em>
_If you want to contribute You can create a pull request to the project_


