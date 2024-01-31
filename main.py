STORED_USER = 'robert'
STORED_PASSWORD = 'password123'

def is_valid_credentials(username, password):
    if username != STORED_USER or password != STORED_PASSWORD:
        print("Error - Invalid input")
        return
    
    print('Deepest darkest secret: I want terminator robot army')