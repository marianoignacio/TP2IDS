#!/bin/bash

condicion=0

while [[ $condicion == 0 ]]; 
do
echo "Ingrese una opción para hacer con el trabajo"

echo "------------------------"

echo " 1)Instalar python"
echo " 2)Instalar pip"
echo " 3)Intalar complementos del entrono virtual"
echo " 4)Crear el entorno"
echo " 5)Salir"
echo "----------------------"

read opcion
case $opcion in

1)
	if python3 --version ;then
	echo "Python installed"
	else
	echo "Python will be installed"
	sudo apt install python3
	fi
;;

2)
	if pip3 --version ; then
	echo "Pip installed"
	else
	echo "Pip will be installed"
	sudo apt install python3-pip
	fi 
;;

3)
	sudo apt install python3.12-venv
;;

4)
	mkdir EjPractico2
	cd ./EjPractico2
	mkdir TP2-IDS
	cd ./TP2-IDS
	mkdir .venv
	mkdir static
	mkdir templates
	touch app.py
	cd ./static
	mkdir css
	mkdir images
	cd ..
	cd ./templates
	touch index.html

echo "Entorno creado correctamente"
;;

5)
	condicion=1
	echo "Saliendo del programa..."

;;

esac
done

