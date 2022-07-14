# Import the required libraries
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_cors import CORS


# Create various application instances
# Order matters: Initialize SQLAlchemy before Marshmallow
db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()
cors = CORS()


def create_app():
    """Application-factory pattern"""
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


    from backend.programs.routes import programs
    from backend.tutors.routes import tutors
    from backend.admins.routes import admins
    from backend.students.routes import students
    
 
    #registering blueprints    
  
    app.register_blueprint(programs)
    app.register_blueprint(tutors)
    app.register_blueprint(admins)
    app.register_blueprint(students)
    



    # Initialize extensions
    # To use the application instances above, instantiate with an application:
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    cors.init_app(app)

    return app
