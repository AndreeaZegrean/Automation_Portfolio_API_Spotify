from generate_token import Generate_token

def get_token():
    token_object = Generate_token()
    return token_object.authorization()
