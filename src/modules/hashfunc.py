import hashlib
import secrets
# This file simply describes the hashing algorithm.


def hash_password(password):
    """ Simply describe the algorithm used for password hashing: SHA3-256 """

    sha3_object = hashlib.sha3_256(password.encode('UTF-8'))
    hashed = sha3_object.hexdigest()
    return hashed


def verify_password(password, password_hash):
    """ Check if the password entered is correct or not """

    password_entered = hash_password(password)
    return secrets.compare_digest(password_entered, password_hash)

