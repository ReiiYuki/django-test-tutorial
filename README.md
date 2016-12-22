# Django Testing Tutorial

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

  
