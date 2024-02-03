import hashlib
import json
import os
import sqlite3

# Connect to db and retrieve cursor
con = sqlite3.connect("ppab6.db")
cur = con.cursor()

# Create table of user logins
if cur.execute("SELECT EXISTS(SELECT 1 FROM sqlite_master WHERE type='table' AND name='users')") == 0:
    cur.execute("CREATE TABLE users(username, password_hash)")

def get_input_user():
    return input('Input username: ')

def get_input_password():
    return input('Input password: ')

def generate_hash(data):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(data.encode('utf-8'))
    return sha256_hash.hexdigest()

def add_user(username=None, password=None):
    username = username or get_input_user()
    password = password or get_input_password()
    password_hash = generate_hash(password)

    cur.execute(f"SELECT EXISTS(SELECT 1 FROM users WHERE username='{username}')")
    r = cur.fetchone()

    if r[0] == 1:
        print("Username already exists! Pick another username.\n")
    elif r[0] == 0:
        cur.execute("Insert INTO users(username, password_hash) VALUES (?, ?)", (username, password_hash))
        con.commit()

def is_valid_credentials(username, password):
    password_hash = generate_hash(password)

    #if username not in STORED_CREDENTIALS or password_hash != STORED_CREDENTIALS[username]:
     #   print("Error - Invalid input")
      #  return

    print('Deepest darkest secret: I want terminator robot army')

add_user('test', 'testone1')
