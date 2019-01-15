# iCrawler :spider_web:
A Python's django based application that triggers spiders from Django views. 

   - Basic structure of a Django project.
   - Basic structure for scrapy.
   - Configuration of scrapy in order to access Django models objects.
   - Basic scrapy pipeline to save crawled objets to Django models.
   - Basic spider definition
   - Basic demo from the oficial tutorial that crawls data from http://quotes.toscrape.com

### Setup
1 - Install requirements
```
$ pip install -r requirements.txt
```
2 - Data migration
```
$ python manage.py migrate
```
### Run the project
3- Start django server
```
$ python manage.py runserver
```
4- Run spider
```
$ cd scrapy_app
$ scrapyd
```
Then if you go to the localhost http://127.0.0.1:6800/, you will see the scrapyd logs and jobs under the default app. 

5- To run it you must send a http request to Scrapyd with the job info
```
curl http://localhost:6800/schedule.json -d project=default -d spider=toscrape-css
```
This project is inspired from a blog post of [medium](https://medium.com/@ali_oguzhan/how-to-use-scrapy-with-django-application-c16fabd0e62e?fbclid=IwAR0Ni7cvNk3aKJLTkWkzkYLjOHoYOpV3Tp1Mr_eYh2rxts0lBjI6rGkG_bM) by Ali Oğuzhan Yıldız
