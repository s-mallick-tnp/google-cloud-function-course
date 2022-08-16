def hello_world(request):

    request_args = request.args # returns a dictionary or null

    if request_args and 'name' in request_args: #check if requests_args is null if not set new variable name to 'name' from the dictionary requests_args
        name = request_args['name']
    else:
        name = 'World' #if the dictionary is null set variable to a string
    
    return f'Hello {name}'