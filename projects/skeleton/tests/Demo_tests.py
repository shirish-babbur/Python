from nose.tools import *
import Demo

def setup():
    print("SETUP!")

def teardown():
    print("TEAR DOWN1!")

def test_basic():
    print("I RAN!")
