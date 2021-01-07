import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "testproject.settings")
import django

django.setup()

from faker import Faker
from random import *
from testapp.models import Hyd_Job, Mumbai_Job, Bangalora_Job, Pune_Job

fake = Faker()


def phonenumbergen():
    d1 = randint(7, 9)
    num = '' + str(d1)
    for i in range(0, 6):
        num = num + str(randint(0, 9))
    return int(num)


def populate(n):
    for i in range(n):
        fdate = fake.date()
        fcompany = fake.company()
        ftitle = fake.random_element(elements=("Project Manager", "TeamLead", "Software Engineer"))
        feligibility = fake.random_element(elements=("B.Tech", "M.tech", "MCA", "Phd"))
        faddress = fake.address()
        femail = fake.email()
        fphonenumber = phonenumbergen()

        hydjobs_record = Hyd_Job.objects.get_or_create(
            DATE=fdate,
            COMPANY=fcompany,
            TITLE=ftitle,
            ELIGIBILITY=feligibility,
            ADDRESS=faddress,
            EMAIL=femail,
            PHONENUMBER=fphonenumber)

    for i in range(n):
        fdate = fake.date()
        fcompany = fake.company()
        ftitle = fake.random_element(elements=("Project Manager", "TeamLead", "Software Engineer"))
        feligibility = fake.random_element(elements=("B.Tech", "M.tech", "MCA", "Phd"))
        faddress = fake.address()
        femail = fake.email()
        fphonenumber = phonenumbergen()

        mumjobs_record = Mumbai_Job.objects.get_or_create(
            DATE=fdate,
            COMPANY=fcompany,
            TITLE=ftitle,
            ELIGIBILITY=feligibility,
            ADDRESS=faddress,
            EMAIL=femail,
            PHONENUMBER=fphonenumber)

    for i in range(n):
        fdate = fake.date()
        fcompany = fake.company()
        ftitle = fake.random_element(elements=("Project Manager", "TeamLead", "Software Engineer"))
        feligibility = fake.random_element(elements=("B.Tech", "M.tech", "MCA", "Phd"))
        faddress = fake.address()
        femail = fake.email()
        fphonenumber = phonenumbergen()

        punejobs_record = Pune_Job.objects.get_or_create(
            DATE=fdate,
            COMPANY=fcompany,
            TITLE=ftitle,
            ELIGIBILITY=feligibility,
            ADDRESS=faddress,
            EMAIL=femail,
            PHONENUMBER=fphonenumber)

    for i in range(n):
        fdate = fake.date()
        fcompany = fake.company()
        ftitle = fake.random_element(elements=("Project Manager", "TeamLead", "Software Engineer"))
        feligibility = fake.random_element(elements=("B.Tech", "M.tech", "MCA", "Phd"))
        faddress = fake.address()
        femail = fake.email()
        fphonenumber = phonenumbergen()

        bangalorajobs_record = Bangalora_Job.objects.get_or_create(
            DATE=fdate,
            COMPANY=fcompany,
            TITLE=ftitle,
            ELIGIBILITY=feligibility,
            ADDRESS=faddress,
            EMAIL=femail,
            PHONENUMBER=fphonenumber)


populate(10)
