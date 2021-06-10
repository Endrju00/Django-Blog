import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()

##FAKER
import random
from first_app.models import User
from faker import Faker

fakegen = Faker()

def populate(N=5):
    for entry in range(N):

        fake_name = fakegen.name().split()
        fake_firstname = fake_name[0]
        fake_secondname = fake_name[1]
        fake_email = fakegen.email()

        user = User.objects.get_or_create(
            first_name=fake_firstname,
            second_name=fake_secondname,
            email=fake_email)[0]

if __name__ == '__main__':
    print('populating script!')
    populate(20)
    print("populating complete")
