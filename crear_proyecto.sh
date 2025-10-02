#!/bin/bash

if python3 --version ;then
echo "Python installed"
else
echo "Python will be installed"
sudo apt install python3
fi

if pip3 --version ; then 
echo "Pip installed"
else 
echo "Pip will be installed"
sudo apt install python3-pip
fi 

sudo apt install python3.12-venv

mkdir EjPractico2
cd EjPractico2/
mkdir TP2-IDS
cd /$HOME/EjPractico2/TP2-IDS/
mkdir .venv
mkdir static
mkdir templates
cd /$HOME/EjPractico2/TP2-IDS/static/
mkdir css
mkdir images
cd /$HOME/EjPractico2/TP2-IDS/
mkdir templates
touch app.py
