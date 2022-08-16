# Google cloud function course
## Strating a project

to start a new project in google cloud, we can go to [Firebase console](https://console.firebase.google.com) or [Google cloud platform console](https://console.cloud.google.com)

## creating a virtual environment
'''
python3 -m venv envName
'''

## Activate virtual env. 

'''
C:\> <venv>\Scripts\activate.bat
'''
<venv> must be replaced by the path of the directory containing the virtual environment

then on Visual studio code press "ctrl + shift + p" then "Select interpreter" brows "Add enterpreter path" then select "python.exe" file from \venv\Scripts\python.exe folder. close the terminal and open it again


## isntall required packages
add requirements.txt file. this file contains all required packages

pip install -r requirements.txt


## Create first cloud function
inside the targeted folder create a python file "main.py" and create a function there.

## test a function localy
navigate to the targeted folder ie. cd Helloworld

functions-framework --target hello_world

## Pstman
Postman is the most popular software to test APIs