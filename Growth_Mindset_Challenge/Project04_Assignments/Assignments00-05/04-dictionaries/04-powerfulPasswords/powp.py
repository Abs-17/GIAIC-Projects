import hashlib

def hash_password(password):
    """
    Returns the SHA-256 hash of the given password.
    """
    return hashlib.sha256(password.encode()).hexdigest()

def login(email, password_to_check, stored_logins):
    """
    Checking if the hashed password matches the stored hash for the given email.

    :test email: The email of the user trying to log in.
    :test password_to_check: The password input to verify.
    :test stored_logins: A dictionary containing email-password hash pairs.
    :return: True if the password matches, False otherwise.
    """
    if email in stored_logins:
        return hash_password(password_to_check) == stored_logins[email]
    return False


if __name__ == "__main__":
    # Simulated stored logins with hashed passwords
    stored_logins = {
        "user1@yahoo.com": hash_password("mypassword123"),
        "user2@msn.com": hash_password("securePass!"),
        "user3@gmail.com": hash_password("anotherSecret")
    }

    # User tries to log in
    email_input = input("Enter your email: ")
    password_input = input("Enter your password: ")

    if login(email_input, password_input, stored_logins):
        print("Login successful!")
    else:
        print("Invalid email or password.")
