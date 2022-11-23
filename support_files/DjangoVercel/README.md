# Note:
I have made a simple machine learning deployment site with a picked titatic model. The website works on localhost, and predict survival rate based on some inputs by the user. The goal was to see if we can host/deploy it somewhere. I was able to find Vercel, a online deploment site where we can deploy django webapps. However, it seems to work with only simple models. Since we need many dependencies, Vercel reaches it's free tier limit. : ( 

# Django on Vercel
This is a simple project developed using Django framework and it contains the settings required for successfull deployment of Django projects on Vercel.
## Setup

Below are the steps to follow to setup this project locally on your machine;

* Clone the project locally on your machine using **git clone**
* Create and activate a new virtual enviroment.
* To install dependencies run
```
pip install -r requirements.txt
```
* Go to the projects setting.py file and remove the comments in the database section.

* In your terminal execute the following commands to makemigrations and migrate to database

```
python manage.py makemigrations
python manage.py migrate
```

