import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','chandansjob.settings')
import django
django.setup()

from testapp.models import Hydjobs
from testapp.models import Punejobs
from testapp.models import Bangjobs
from faker import Faker
from random import *
fake = Faker()

def phonenumbergen():
	d1 = randint(6,9)
	num = '' + str(d1)
	for i in range(9):
		num += str(randint(0,9))
	return int(num)
def populate(n):
    for i in range(n):
        fdate = fake.date()
        fcomany = fake.company()
        ftitle = fake.random_element(elements=('Project Manager','Team Lead','Software Engineer','Associate Engineer'))
        feligibility = fake.random_element(elements=('B.Tech','M.Tech','MCA','Phd'))
        faddress = fake.address()
        femail = fake.email()
        fphonenumber = phonenumbergen()
        hyd_job_record = Hydjobs.objects.get_or_create(
        date = fdate,
        company = fcomany,
        title = ftitle,
        eligibility = feligibility,
        address = faddress,
        email = femail,
        phonenumber = fphonenumber,
        )
        pune_job_record = Punejobs.objects.get_or_create(
            date=fdate,
            company=fcomany,
            title=ftitle,
            eligibility=feligibility,
            address=faddress,
            email=femail,
            phonenumber=fphonenumber,
        )
        Bang_job_record = Bangjobs.objects.get_or_create(
            date=fdate,
            company=fcomany,
            title=ftitle,
            eligibility=feligibility,
            address=faddress,
            email=femail,
            phonenumber=fphonenumber,
        )
n = int(input('Enter number of records:'))
populate(n)
print(f'{n} records inserted successfully......')