__author__="Divine Gbagi"
__date__="09/23/2020"
"""Tests emails individually to see if they're valid
"""
from unittest import *
from modValidateEmail import *

class TestValidEmail(TestCase):   
    def testUserName(self):
        self.assertEqual(isValidMSUMEmail('.joe@mnstate.edu'),False)
        self.assertEqual(isValidMSUMEmail('joe4@mnstate.edu'),False)
        self.assertEqual(isValidMSUMEmail('joe$smith@mnstate.edu'),False)
        self.assertEqual(isValidMSUMEmail('joe.smith@mnstate.edu'),True)

    def testTooManyAmpersands(self):
        self.assertEqual(isValidMSUMEmail('jim@smith@mnstate.edu'),False)
        self.assertEqual(isValidMSUMEmail('@jim@smith@mnstate.edu'),False)

    def testNotMnstate(self):
        self.assertEqual(isValidMSUMEmail('jim.smith@mnstate.edu'),True)

    def testGoodEmail(self):
        self.assertEqual(isValidMSUMEmail('jesse.jones@mnstate.edu'),True)

#main
#unittest.main()
suite = TestLoader().loadTestsFromTestCase(TestValidEmail)
TextTestRunner(verbosity=2).run(suite)
