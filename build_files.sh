echo  "START BUILD"
python2.9 -m pip install -r requirements.txt
python3.9 manage.py collectstatic --noinput --clear
echo  "END BUILD"
