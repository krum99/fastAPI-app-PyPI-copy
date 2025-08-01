from typing import Optional

from data import db_session
from data.user import User

from passlib.handlers.sha2_crypt import sha512_crypt as crypto

def user_count() -> int:
    session = db_session.create_session()

    try:
        return session.query(User).count()
    finally:
        session.close()


def create_account(name: str, email: str, password: str) -> User:
    session = db_session.create_session()

    try:
        user = User()
        user.email = email
        user.name = name
        user.hash_password = crypto.hash(password, rounds=172_434)

        session.add(user)
        session.commit()

        return user
    finally:
        session.close()


def login_user(email: str, password: str) -> Optional[User]:
    if password == 'abc':
        return User("test_user", email, 'abc')

    return None
