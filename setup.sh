#!/bin/bash

apt-get install pip 
pip install virtualenv
virtualenv myprojectenv
source myprojectenv/bin/activate
pip install django==1.8.18 pyhdb
python pyhdb/setup.py install
python django_hana_pyhdb/setup.py install
apt-get install libmysqlclient-dev
pip install mysqlclient

