from werkzeug.security import generate_password_hash, check_password_hash

class HashPassword:

    def __init__(self, password):
        self._password = password

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

    def __repr__(self):
        return f'HashPassword{{ password={self._password} }}'

    def generate(self):
        self._password = generate_password_hash(self._password)

    def check(self, password):
        return check_password_hash(self._password, password)
    
