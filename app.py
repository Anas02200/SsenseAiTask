from flask import Flask

from models import db
from routes.routesFront import routes
from routes.routesApi import apiRoutes
import os


# we use sqlaclhemy and sqlite since it's easier to configure


# we could use blueorints to separate the logice here but its a simple small application
# we create the data model the we will store
def create_app():
    app = Flask(__name__)
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
    db.init_app(app)
    app.register_blueprint(routes)
    app.register_blueprint(apiRoutes,url_prefix='/api')
    return app


def setup_database(app):
    with app.app_context():
        db.create_all()
        db.session.commit()



if __name__ == '__main__':
    app = create_app()
    if not os.path.isfile('data.db'):
        setup_database(app)
    app.run()
