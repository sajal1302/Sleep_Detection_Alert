# Sleep_Detection_Alert

step1:- conda create --name myenv django python=3.6

step2:- conda activate myenv

step3:- Installing all the library
	pip install opencv-python
	pip install dlib
	pip install imutils
	pip install scipy
	pip install playsound
	pip install bcrypt
	pip install django[argon2]

step3:-creating django framework
	django-admin startproject first_project
	python manage.py startapp first_app

step4:-running the django framework
	python manage.py migrate
	python manage.py makemigrations app

step5:- A server url will be generated copy that and paste that into any browser.

step6:- signup,login push the start button and the algo will start working
	for exiting press q
