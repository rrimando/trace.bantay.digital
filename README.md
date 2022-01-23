# Trace Bantay Digital

We have archived trace and have made it public for anyone who may find it useful https://github.com/rrimando/trace.bantay.digital

Trace by Bantay Digital was a simple log book and QR code generator application tool meant to simply log user locations and associate them with individuals and establishment in the simplest way possible. The team was prepared to give it out absolutely free, powered by volunteer work and genuine concern for the community.

While larger applications aimed to build more robust and complicated trace applications, trace at its core was aimed to roll out as quick as it could. Many hours have been spent building the application and many more were spent by volunteer workers / users in testing and meeting with LGUs and interested collaborators.

There is still quite a long way till we are out of this pandemic, we are glad the worst maybe over.

To all of you who have spent time and effort to try to get Trace out thank you, although we were never rolled out due to unforeseen circumstance, your good intentions and contributions are greatly appreciated.

TO THE TEAM:

Thanks you all for your time and effort! We can never repay you for the countless meetings and discussions to shape Trace. We are eternally grateful! Much love! It was a privilege working with you guys!

# django-wyvern

A Personal CMS Built on Django

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

### Activating virtualenv

pip install django
pip install configparser
pip install mysqlclient

## Application Configuration

- https://www.pythonforbeginners.com/code-snippets-source-code/how-to-use-configparser-in-python
- https://docs.python.org/3.4/library/configparser.html

## MySQL

### If you need to have mysql@5.7 first in your PATH run:

`echo 'export PATH="/usr/local/opt/mysql@5.7/bin:$PATH"' >> ~/.bash_profile`

### For compilers to find mysql@5.7 you may need to set:

`export LDFLAGS="-L/usr/local/opt/mysql@5.7/lib" export CPPFLAGS="-I/usr/local/opt/mysql@5.7/include"`

### For pkg-config to find mysql@5.7 you may need to set:

`export PKG_CONFIG_PATH="/usr/local/opt/mysql@5.7/lib/pkgconfig`

### To have launchd start mysql@5.7 now and restart at login:

`brew services start mysql@5.7`
Or, if you don't want/need a background service you can just run:
`/usr/local/opt/mysql@5.7/bin/mysql.server start`

## Running Migrations

`./manage.py makemigrations ./manage.py migrate`
