#!/bin/bash

sudo apt-get install python-pip
sudo pip install virtualenv
virtualenv myprojectenv
source myprojectenv/bin/activate
pip install django==1.8.18 pyhdb
git submodule init
git submodule update
python pyhdb/setup.py install
python django_hana_pyhdb/setup.py install
sudo apt-get install libmysqlclient-dev
pip install mysqlclient

