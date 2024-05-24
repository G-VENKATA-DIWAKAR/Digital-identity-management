#!/usr/bin/env python
# coding: utf-8

# In[5]:


import hashlib
import random

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = self.hash_password(password)
        self.digital_id = None

    def hash_password(self, password):
        
        digest = hashlib.sha256(password.encode()).hexdigest()
        return digest

class DigitalIdentity:
    def __init__(self, user):
        self.user = user
        self.token = None

    def generate_token(self):
        
        random.seed()
        token = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=16))
        self.token = token

def secure_authentication(user, entered_password):
    
    entered_password_hash = hashlib.sha256(entered_password.encode()).hexdigest()
    print(f"Expected hash: {user.password}")  
    print(f"Entered password hash: {entered_password_hash}")  
    return user.password == entered_password_hash


if __name__ == "__main__":
    
    alice = User("Alice", "StrongPassword123")
    alice_digital_identity = DigitalIdentity(alice)
    alice_digital_identity.generate_token()

    
    entered_password = input("Enter your password: ").strip()  

    if secure_authentication(alice, entered_password):
        print("Login successful. Welcome, {}!".format(alice.username))
        
        if alice_digital_identity.token:
            print("Digital Identity Token:", alice_digital_identity.token)
        else:
            print("No digital identity token available.")
    else:
        print("Login failed. Incorrect password.")


# In[ ]:




