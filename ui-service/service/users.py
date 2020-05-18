#from ..model import models
import datetime as dt
import sys
import os
sys.path.append(os.getcwd() + '/..')
#from .. import app
import app
#sys.path.append(os.path.abspath('../model'))
sys.path.append(os.getcwd() + '/..')
from model.models import User


class UserService():
    def get_user(self, id=None):
        new_user = User(username='username',
                               email='email',
                               created=dt.now(),
                               bio="In West Philadelphia born n raised...",
                               admin=False)
        app.db.session.add(new_user)  # Adds new User record to database
        app.db.session.commit()  # Commits all changes
        return {'hello': 'world'}
