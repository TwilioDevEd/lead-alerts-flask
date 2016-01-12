"""
This script holds the commands nedeed for runnin the migrations and the tests
"""

from flask import Flask
from flask.ext.script import Manager
from lead_alerts import app

manager = Manager(app)

@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('.', pattern="*_tests.py")
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == "__main__":
    manager.run()
