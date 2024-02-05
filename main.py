import hashlib
import sqlite3

database_title = 'users'

# Connect to db and retrieve cursor
con = sqlite3.connect("ppab6-v1.db")
cur = con.cursor()

# Create table of user logins
if cur.execute(f"SELECT EXISTS(SELECT 1 FROM sqlite_master WHERE type='table' AND name='{database_title}')") == 0:
    cur.execute(f"CREATE TABLE {database_title}(username, password_hash)")

def get_input_user():
    return input('Input username: ')

def get_input_password():
    return input('Input password: ')

def user_exists(username):
    cur.execute(f"SELECT EXISTS(SELECT 1 FROM {database_title} WHERE username='{username}')")
    r = cur.fetchone()

    if r[0] == 1:
        return True

def generate_hash(data):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(data.encode('utf-8'))
    return sha256_hash.hexdigest()

def add_user(username=None, password=None):
    username = username or get_input_user()
    password = password or get_input_password()
    password_hash = generate_hash(password)

    if not user_exists(username):
        print("Username already exists! Pick another username.\n")
        return

    cur.execute(f"Insert INTO {database_title}(username, password_hash) VALUES (?, ?)", (username, password_hash))
    con.commit()

def is_valid_credentials(username=None, password=None):
    username = username or get_input_user()
    password = password or get_input_password()
    password_hash = generate_hash(password)

    if user_exists(username):
        
        # Check if password matches in database
        cur.execute(f"SELECT EXISTS(SELECT 1 FROM {database_title} WHERE username='{username}' AND password_hash='{password_hash}')")
        r = cur.fetchone()

        if r[0] == 1:
            print('Deepest darkest secret: I want terminator robot army')
        else:
            print("Error - Invalid input")

is_valid_credentials()
con.close()