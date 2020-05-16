pip install venv curd
cd curd/Scripts
activate
cd ../..
virtualenv --clear venv
pip install -r requirements.txt
pip install mysqlclient-1.4.6-cp38-cp38-win32.whl