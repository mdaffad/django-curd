sudo service mysql stop
sudo apt-get -y install libmysqlclient-dev
pip3 install virtualenv
virtualenv venv
source venv/bin/activate
pip3 install -r requirements.txt
