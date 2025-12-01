"""
Author: Lexi Virta
Date: 2025-11-24
Description: Manages users in a text file database
"""

from pathlib import Path
import pyinputplus as pyip
import re

# Configurable file paths
DB_FILE = Path.resolve(Path("./data/users.db"))

# Define for configuration and compile for performance
username_regex = r"[a-zA-Z_0-9\-]+"
email_regex = r"[a-z0-9\.\-]+@[a-z0-9\.\-]+\.[a-z]{2,10}"

user_input_regex = r"^(" + username_regex + r")\s(" + email_regex + r")$"
user_input_pattern = re.compile(user_input_regex)

# Users data table
users = {}

def main():
    # Automatically create database file if it doesn't exist
    try:
        load_users()
        print(str(len(users)) + " user(s) loaded!")
    except FileNotFoundError:
        print("Database file not found. A new one will be created upon user modification.")
        print("\t" + str(DB_FILE))

    # Receive user commands
    while True:
        action = pyip.inputMenu([ "view", "add", "exit" ], numbered=True)

        if action == "view":
            command_view()
        elif action == "add":
            command_add()
        elif action == "exit":
            print("Goodbye!")
            return

        print("") # Add line after every operation

# "username email" -> (username, email)
def parse_user_string(user_string):
    if not user_input_pattern.match(user_string):
        raise ValueError("Invalid user string")
    
    (username, email) = user_input_pattern.search(user_string).groups()

    return (username, email)

# (username, email) -> "username email"
def build_user_string(username, email):
    return username + " " + email

# Write to database
def append_user(username, email):
    users[username] = email

    with open(DB_FILE, "a") as users_handle:
        users_handle.write(build_user_string(username, email) + "\n")

# Load database
def load_users():
    users.clear()

    with open(DB_FILE, "r") as users_handle:
        while True:
            line = users_handle.readline()
            if not line: return

            (username, email) = parse_user_string(line)
            users[username] = email

# view command
def command_view():
    print(f"{f' {len(users)} Registered User(s) ':=^60}")

    item_format = "{:<30}{:<30}"

    print(item_format.format("USERNAME", "EMAIL"))
    for (username, email) in users.items():
        print(item_format.format(username, email))

# add command
def command_add():
    print("Add one or multiple users in the following format:")
    print("username email@service.abc")
    print("Multiple users must be separated by a comma.")

    added_users = list()

    input_list = pyip.inputStr("Usernames: ")
    for line in input_list.split(","):
        username = ""
        email = ""

        # Try parsing the string, softly failing if malformed
        try:
            (username, email) = parse_user_string(line.strip())
        except ValueError:
            print("[!] Invalid user entry: \"" + line + "\"")
            continue

        # Make sure the user doesn't exist already
        if username in users:
            print("[!] User " + username + " already exists")
            continue
        
        # Add user to database and track the username to show in a summary
        append_user(username, email)
        added_users.append(username)
    
    # Show summary of changes
    if added_users:
        print(f"{f' {len(added_users)} User(s) Added ':=^32}")
        for added_user in added_users:
            print("[+] " + added_user)
    else:
        print("[!] No users added")

main()