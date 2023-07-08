# Blog_Django101
https://www.eduonix.com/new_dashboard/web-development-using-python-and-django-new-content

### Step 1:

`python -V`
-> Python 3.10.9

`pip install pipenv`

`pipenv install Django`

`pipenv shell`

`pip show Django`

`django-admin startproject mysite . `

`python manage.py runserver 0.0.0.0:8000`

`./manage.py migrate`

`python manage.py createsuperuser`
user:
email:
p/w:

go to:
http://0.0.0.0:8000/admin/


### Step 2: create "feed" folder:  
`python manage.py startapp feed`

### Step: 3   go to   "settings.py"   and add:    
`INSTALLED_APPS = [    "feed",`

__________________________________________________________________

#### database management is done automatically through migrations and models
### Step: 4   go to "feed/models.py" and add "Post Class:
`class Post(models.Model):
    text = models.CharField(max_length=140, blank=False, null=False)`

`python manage.py makemigrations
 "feed/migrations/0002_initial.py"`   is added

### Step: 5   go to "feed/admin.py"
`class PostAdmin(admin.ModelAdmin):
    pass
admin.site.register(Post,PostAdmin)`

### Step 6:   go to "feed/models.py" and add
   ` def __str__(self):
        return self.text`

