# sudo systemctl daemon-reload
# sudo systemctl restart <service name>
# sudo systemctl restart nginx
./manage.py makemigrations # --merge
./manage.py migrate
./manage.py collectstatic --no-input
./manage.py runserver 0.0.0.0:8000