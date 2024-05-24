yum install sqlite sqlite-devel -y
pip3 install -r requirements.txt
python3.12 manage.py collectstatic
