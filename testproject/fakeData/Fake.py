from faker import Faker
from random import *
from django import *
from testapp.models import Hyd_Job
fake = Faker()

def phonenumbergen():
    d1 = randint(7, 9)
    num = '' + str(d1)
    for i in range(0, 9):
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
        print(femail)
        hydjobs_record = Hyd_Job.objects.get_or_create(
            DATE=fdate,
            COMPANY=fcompany,
            TITLE=ftitle,
            ELIGIBILITY=feligibility,
            ADDRESS=faddress,
            EMAIL=femail,
            PHONENUMBER=fphonenumber)
        hydjobs_record.save()
populate(5)
