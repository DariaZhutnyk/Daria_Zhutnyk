import unittest
from shift_test import ShiftTest

global tester

def test_init_driver():
    global tester
    tester = ShiftTest()

def test_login_page():
    tester.login_page()

def test_main_page():
    tester.main_page()

def test_shift_page():
    tester.shift_page()

def test_check_new_row():
    tester.check_new_row()

def test_remove_row_and_check():
    tester.remove_row_and_check()

if __name__ == '__main__':
    unittest.main()


