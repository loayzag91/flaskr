#!/usr/bin/env python
import os
from app import create_app, config
from app.models import Entries, db
from flask_script import Server, Manager, Shell

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)

def make_shell_context():
    return dict(app=app, db=db, Entries=Entries)
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command("runserver", Server(host='0.0.0.0', port=80))

@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests', pattern='test*.py')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
    manager.run()
