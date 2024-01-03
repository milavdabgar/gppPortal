#! /bin/sh
echo "======================================================================"
echo "Welcome to to the setup. This will setup the local virtual env." 
echo "And then it will install all the required python libraries."
echo "You can rerun this without any issues."
echo "----------------------------------------------------------------------"

if [ -d ".pyvenv" ];
then
    echo ".pyvenv folder exists. Installing using pip"
else
    echo "creating .pyvenv and install using pip"
    python -m venv .pyvenv
fi

# Activate virtual env
. .pyvenv/bin/activate

# Upgrade the PIP
pip install --upgrade pip
pip install -r requirements.txt
export FLASK_APP=main.py
# flask db init
# Work done. so deactivate the virtual env
deactivate
