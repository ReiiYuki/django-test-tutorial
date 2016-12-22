# Django Testing Tutorial

## Environment
```
Django
```

## Initialize Project

1. We start from initializing project. In your console type

  ```
  django-admin startproject djangotest
  cd djangotest
  ```

2. Let's create some app, in your console type

  ```
  django-admin startapp exampleapp
  ```

3. Next, connect app to your Project

  In `djangotest/settings.py` edit

  ```python
  INSTALLED_APPS = [
      'exampleapp.apps.ExampleappConfig',
      'django.contrib.admin',
      'django.contrib.auth',
      .
      .
      .
  ]
  ```

4. Create some model for testing. In this case I create person for example.

  In `exampleapp/models.py`

  ```python
  class Person(models.Model) :
      first_name = models.CharField(max_length=50)
      last_name = models.CharField(max_length=50)
      birthday = models.DateField()
  ```

5. Migrate our model to Database

  In your console
  ```
  python manage.py makemigrations
  python manage.py migrate
  ```

## Testing

1. In django they give `tests.py` in each app so you can write you own test case in that. So we start by edit `exampleapp/tests.py` and add some test class.

  ```python
  from django.test import TestCase

  # Create your tests here.
  class PersonTest(TestCase) :

  ```

2. Create some testcase by write the method which start with `test_`

  ```python
  from django.test import TestCase
  from .models import Person
  import datetime
  # Create your tests here.
  class PersonTest(TestCase) :

      def test_create_person(self) :
          Person.objects.create(first_name="Reii",last_name="Yuki",birthday="1996-3-25")
          latest_person = Person.objects.latest('id')
          self.assertEqual(latest_person.first_name,"Reii")
          self.assertEqual(latest_person.last_name,"Yuki")
          self.assertEqual(latest_person.birthday,datetime.date(1996,3,25))

  ```

3. Let's run our TestCase

  In console type

  ```
  django manage.py test
  ```

  If test successful
  ```
  Creating test database for alias 'default'...
  .
  ----------------------------------------------------------------------
  Ran 1 test in 0.002s

  OK
  Destroying test database for alias 'default'...
  ```

4. You can prepare some data at the start of testing by declare it in method called `setUp`

  ```python
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

  ```

5. In fact there are many assert function in django testcase, you can look at their [Offical site](https://docs.djangoproject.com/en/1.10/topics/testing/tools/#django.test.TestCase)

## Licence
MIT
