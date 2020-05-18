from flask_restful import Resource
import sys
import os
from ..service import users
#import service.users as users
#sys.path.append(os.getcwd() + '/..')
#from service.users import UserService

class Banner(Resource):
    def get(self, id=None):
        UserService.get_user()
        return {'hello': 'world'}

    def post(self):
        pass
