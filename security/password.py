from argon2 import PasswordHasher
from argon2.exceptions import VerificationError, VerifyMismatchError

pwd_context = PasswordHasher()

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(password: str, password_hash: str):
    try:
        return pwd_context.verify(password_hash, password)
    except (VerifyMismatchError, VerificationError):
        return False
