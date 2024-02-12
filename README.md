# Introduction to Django Web Store Project
**Description**

This repository serves as an introductory project for a web store, built using Django, Oscar, and Wagtail frameworks. 
The project is designed to showcase the fundamental capabilities of each of these frameworks within the context of an online store.

**1 - Clone repo**
  1. Make new folder and open it in console
```
mkdir shop
cd shop
```
  2. Clone this repository
```
git clone https://github.com/serikzhant/shop .
```
  3. Make virtual environment and activate it
```
virtualenv venv
.\venv\Scripts\activate
```
  4. Install all required packages
```
pip install -r requirements.txt
```
  5. Create superuser
```
py .\manage.py createsuperuser
```
  6. Run shop server
```
py .\manage.py runserver    
```
**2 - Start your own project**

_Despite the fact that the oscar framework is based on a django, it has a lot of useful features out of the box, and therefore the launch of project is different._
1. make directory
2. create and activate virtual environment to isolate dependencies
3. pip install django-oscar-wagtail
   _initiate base wagtail structure for your project_
4. wagtail start "project name" .
   
   
