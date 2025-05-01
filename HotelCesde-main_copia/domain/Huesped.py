from domain.User import User

class Customer(User):

    def __init__(self, id, name, last_name, email, password , status, origin, occupation):
        super().__init__(id, name, last_name, email, password, status)
        self._origin = origin
        self._occupation = occupation


    @property
    def origin(self):
        return self._origin

    @origin.setter
    def origin(self,origin):
        self._origin = origin

    @property
    def occupation(self):
        return self._occupation

    @occupation.setter
    def occupation(self, occupation):
        self._occupation =occupation