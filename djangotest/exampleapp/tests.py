from django.test import TestCase
from .models import Person
import datetime
# Create your tests here.
class PersonTest(TestCase) :

    def setUp(self) :
        Person.objects.create(first_name="Kirigaya",last_name="Kasuto",birthday="2008-10-7")

    def test_update_birthday(self) :
        kirito = Person.objects.get(first_name="Kirigaya")
        old_birthday = kirito.birthday
        kirito.birthday = datetime.date(2009,10,7)
        kirito.save()
        new_birthday = kirito.birthday
        self.assertNotEqual(old_birthday,new_birthday)
        self.assertEqual(new_birthday,datetime.date(2009,10,7))

    def test_create_person(self) :
        Person.objects.create(first_name="Reii",last_name="Yuki",birthday="1996-3-25")
        latest_person = Person.objects.latest('id')
        self.assertEqual(latest_person.first_name,"Reii")
        self.assertEqual(latest_person.last_name,"Yuki")
        self.assertEqual(latest_person.birthday,datetime.date(1996,3,25))
