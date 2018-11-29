import unittest

def suite():
    return unittest.TestLoader().discover("polls.tests",pattern="*.py")
