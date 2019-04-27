deactivate 
rm -rf venv3 
rm -rf django


python3 -m venv venv3 
source venv3/bin/activate
pip install --upgrade pip 
pip install -r requirements.txt 

django-admin startproject weather
mv weather django

cd django
mkdir djangoDB

cd weather
cp ../../secrets/settings_secret.py . 

# Remove secret-key from settings.py
sed -i 's/.*SECRET_KEY.*/from .settings_secret import */' settings.py

# And finally patch with my setup.
patch settings.py < ../../patches/patch_settings_py

cd ..

python manage.py migrate
python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('bauminao', 'patrick.baumgart@basf.com', '"`cat ../secrets/pass.secret`"')"
