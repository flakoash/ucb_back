#!/bin/bash
git submodule init
git submodule update
sudo apt-get install python-pip
sudo pip install virtualenv
virtualenv myprojectenv
source myprojectenv/bin/activate
pip install django==1.8.18 pyhdb
python pyhdb/setup.py install
python django_hana_pyhdb/setup.py install
sudo apt-get install libmysqlclient-dev
pip install mysqlclient

pip install coreapi ==2.3.3
pip install djangorestframework==3.6.4
pip install djangorestframework-simplejwt==3.2.3
pip install drf-dynamic-fields==0.3.0
pip install Pillow==5.1.0
pip install requests==2.18.4
pip install django-cors-headers==2.2.0

pip install pyjarowinkler==1.8

