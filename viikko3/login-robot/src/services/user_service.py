from entities.user import User
import re

class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")
            #username
        if not re.match("^[a-z]+$", username):
            raise UserInputError("Invalid username")
        if not re.match("^[a-zA-Z][a-zA-Z0-9.-]{3,}[a-zA-Z0-9]$", username):
            raise UserInputError("Username is too short")

            #password
        if not re.match("(?=^.{8,}$)", password):
            raise UserInputError("Password is too short")

        if not re.match("^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$", password):
            raise UserInputError("Must contain at least one special character")
        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa
