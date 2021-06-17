from werkzeug.security import generate_password_hash, check_password_hash

class HashPassword:

    def __init__(self, hash = ""):
        self._hash = hash

    @property
    def hash(self):
        return self._hash

    @hash.setter
    def hash(self, hash):
        self._hash = hash

    def __repr__(self):
        return f'HashPassword{{ hash={self._hash} }}'

    def generate(self):
        self._hash = generate_password_hash(self._hash)

    def check(self, password):
        try:
            return check_password_hash(self._hash, password)
        except AttributeError:
            return None
    
