from .classes.Version import Version
from .classes.User import User
from .Authenticator import Authenticator

class Routes:

    @staticmethod
    def setRoutes(api, mysql):
        api.add_resource(Version, '/')

        User.setDatabase(mysql)
        api.add_resource(User, '/user')

        Authenticator.setDatabase(mysql)
        api.add_resource(Authenticator, '/genToken', '/validate')