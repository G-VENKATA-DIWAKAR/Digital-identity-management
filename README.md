User Authentication and Digital Identity System.
This repository contains a simple Python-based user authentication system that uses hashed passwords for secure login and generates a digital identity token for authenticated users. The system is implemented using two main classes, User and DigitalIdentity, and includes a function for secure authentication.
Features:
1.Secure password hashing using SHA-256.
2.Random token generation for digital identity using the secrets module.
3.Command-line interface for user login.
4.Basic authentication flow.
Requirements:
Python 3.x
Installation:
1.Clone the repository:
git clone https://github.com/yourusername/user-authentication-system.git
cd user-authentication-system
2.No additional packages are required. The script uses Python's standard library.
Usage:
1.Run the script:
python3 main.py
2.Enter the password when prompted to authenticate.
Code Overview:
User Class
Represents a user with a username and a hashed password.
*__init__(self, username, password): Initializes a new user with a username and a hashed password.
*hash_password(self, password): Hashes the provided password using SHA-256 and returns the hash.
DigitalIdentity Class:
Represents a digital identity for a user, including a randomly generated token.
*__init__(self, user): Initializes a new digital identity for the given user.
*generate_token(self): Generates a random token using the secrets module and stores it.
secure_authentication Function:
Checks if the entered password matches the stored hashed password.
*secure_authentication(user, entered_password): Returns True if the entered password, when hashed, matches the stored hashed password; False otherwise.
Main Script Execution:
1.Creates a user named "Alice" with the password "StrongPassword123".
2.Creates a digital identity for Alice and generates a random token.
3.Prompts the user to enter a password.
4.Authenticates the user and displays a welcome message along with the digital identity token 5.if the authentication is successful.
Sample output:
Enter your password: StrongPassword123
Login successful. Welcome, Alice!
Digital Identity Token: 9a1b2c3d4e5f6789abcdef0123456789
