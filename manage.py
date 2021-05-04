from app import make_app,db
from flask_script import Manager,Server
from app.models import User,Post,Review
from  flask_migrate import Migrate, MigrateCommand

#Creating app instance
app = make_app('development')

manager = Manager(app)
manager.add_command('server',Server)

#init migrate class and pass in app and sqlalchemy instance
migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

@manager.command #run the test files
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

@manager.shell #create shell context and return app,db instance and user class
def make_shell_context():
    '''
    flask-script shell for testing 
    features in app and debugging
    '''
    return dict(app = app, db = db, User = User, Post = Post, Review = Review) ##add models


if __name__ == '__main__':
    manager.run()