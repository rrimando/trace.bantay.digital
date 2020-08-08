# Development Timeline

 - [ ] Create todo list on Github
 - [ ] Create clean version 
 - [ ] Start test and CICD
 - [ ] Begin code cleanup
 - [ ] Security  

#

# django-wyvern

A Personal CMS Built on Django

# Stack

# Coding Standards

Tab or Spaces

- Please use spaces, 4 for each tab. While this may seem trivial it will prevent indentation problems with Python code.

# Forms

## Form Styling

### Django Crispy Forms

# Design Elements

*https://simpleisbetterthancomplex.com/tutorial/2018/08/13/how-to-use-bootstrap-4-forms-with-django.html*

*https://pypi.org/project/django-crud-generator/*

*https://useiconic.com/open#icons*

*https://getbootstrap.com/docs/4.0/utilities/spacing/*

*https://github.com/django-ckeditor/django-ckeditor*
*https://django-ckeditor.readthedocs.io/en/latest/#required-for-using-widget-with-file-upload*

# Template Folder Heirarchy

- blog/
  - pages/
    - list.html
    - single.html
    - custom.html
  - partials/
- shop/
  - cart/
  - checkout/
- blocks/
  - header.html
  - footer.html
- base/
  - base-{}.html  


  # Development, Deployment and CICD Documentation

#### Stack Notes
- Python 3.7.3
- Django 2.0.1

## Building The Environment 

### Installing Python 3.7.3

### Installing pip3

### Installing virtualenv

### Activating virtualenv

pip install django
pip install configparser
pip install mysqlclient

# Troubleshooting

## Application Configuration

- https://www.pythonforbeginners.com/code-snippets-source-code/how-to-use-configparser-in-python
- https://docs.python.org/3.4/library/configparser.html

## MySQL

### Allow blank root password
- https://serverfault.com/questions/563714/allow-linux-root-user-mysql-root-access-without-password

### ERROR 2002 (HY000): Can't connect to local MySQL server through socket '/tmp/mysql.sock' (2)
- https://stackoverflow.com/questions/15016376/cant-connect-to-local-mysql-server-through-socket-homebrew/15016441

### If you need to have mysql@5.7 first in your PATH run:

`echo 'export PATH="/usr/local/opt/mysql@5.7/bin:$PATH"' >> ~/.bash_profile`

### For compilers to find mysql@5.7 you may need to set:
`export LDFLAGS="-L/usr/local/opt/mysql@5.7/lib"
   export CPPFLAGS="-I/usr/local/opt/mysql@5.7/include"`

### For pkg-config to find mysql@5.7 you may need to set:

`export PKG_CONFIG_PATH="/usr/local/opt/mysql@5.7/lib/pkgconfig`

### To have launchd start mysql@5.7 now and restart at login:
  `brew services start mysql@5.7`
Or, if you don't want/need a background service you can just run:
  `/usr/local/opt/mysql@5.7/bin/mysql.server start`

## Running Migrations

`./manage.py makemigrations
./manage.py migrate`
