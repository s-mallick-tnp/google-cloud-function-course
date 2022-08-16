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