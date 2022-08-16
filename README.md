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

## passing multiple arguments

'''python
def hello_world(request):

    request_args = request.args # returns a dictionary or null
    request_json = request.get_json(silent = True)

    if request_args and 'name' in request_args and 'lastname' in request_args: #check if requests_args is null if not set new variable name to 'name' from the dictionary requests_args
        name = request_args['name']
        lastname = request_args['lastname']
    elif request_json and 'name' in request_json and 'lastname' in request_json:
        name = request_json['name']
        lastname = request_json['lastname']
    else:
        name = 'World' #if the dictionary is null set variable to a string
        lastname = ''
    
    return f'Hello {name} {lastname}'
'''


## Deploying our functions to google cloud
First, we have to set our project ID with the following command:

gcloud config set project [YOUR_PROJECT_ID]

Then we deploy our function with this command:

gcloud functions deploy [FUNCTION_NAME] --runtime python37 --trigger-http