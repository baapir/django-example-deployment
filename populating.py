# on th venv
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_tuts.settings')

#start django
import django
django.setup()


##Fake pop script
import random
from django_level_two.models import AccessRecord, Topic, Webpage, UserAdded
from faker import Faker


fakegen = Faker()
##topics = ['search', 'social', 'sport', 'news', 'games']


def add_topics():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


def populating(n=5):
    for entry in range(n):
        top = add_topics()
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        webpg = Webpage.objects.get_or_create(category=top,  name=fake_name, url=fake_url)[0]
        acc_req = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]


def popul(n=5):
    for entry in range(n):
        fake_fname = fakegen.first_name()
        fake_lname = fakegen.last_name()
        fake_email = fakegen.email()

        newobj = UserAdded.objects.get_or_create(FirstName=fake_fname, LastName=fake_lname, Email=fake_email)[0]

if __name__=='__main__':
    print("populaing script!!!!!!!!!")
    popul(20)
    ##populating(20)
    print("populating")
