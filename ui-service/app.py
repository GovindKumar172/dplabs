from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from resources.banner import Banner

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/dplabs_ui_services'
db = SQLAlchemy(app)
api = Api(app)

# api.add_resource(Banner, '/banner', '/banner/<string:id>')
api.add_resource(Banner, '/banner', '/banner/<string:id>')
# api.add_resource(Bar, '/Bar', '/Bar/<string:id>')

if __name__ == '__main__':
    app.run(debug=False)
