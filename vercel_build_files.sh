yum install sqlite sqlite-devel libsqlite3-dev -y
pip3 install -r requirements.txt
python3.12 manage.py collectstatic
