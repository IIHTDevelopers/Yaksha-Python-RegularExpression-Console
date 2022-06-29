import unittest
from validate_mobile_number import validate_mobile_number
from validate_email_id import validate_email_id
from test.TestUtils import TestUtils
class FuctionalTests(unittest.TestCase):
    def test_10digit_mobile_number(self):
        test_obj = TestUtils()
        result=validate_mobile_number('9493401968')
        if result=='TRUE':
            test_obj.yakshaAssert("Test10DigitMobileNumber", True, "functional")
            print("Test10DigitMobileNumber = Passed")
        else:
            test_obj.yakshaAssert("Test10DigitMobileNumber", False, "functional")
            print("Test10DigitMobileNumber = Failed")

    def test_11digit_mobile_number(self):
        test_obj = TestUtils()
        result=validate_mobile_number('09493401968')
        if result=='TRUE':
            test_obj.yakshaAssert("Test11DigitMobileNumber", True, "functional")
            print("Test11DigitMobileNumber = Passed")
        else:
            test_obj.yakshaAssert("Test11DigitMobileNumber", False, "functional")
            print("Test11DigitMobileNumber = Failed")

    def test_13digit_mobile_number(self):
        test_obj = TestUtils()
        result=validate_mobile_number('+919493401968')
        if result=='TRUE':
            test_obj.yakshaAssert("Test13DigitMobileNumber", True, "functional")
            print("Test13DigitMobileNumber = Passed")
        else:
            test_obj.yakshaAssert("Test13DigitMobileNumber", False, "functional")
            print("Test13DigitMobileNumber = Failed")

    def test_gmail_dot_com(self):
        test_obj = TestUtils()
        result=validate_email_id('venu@gmail.com')
        if result=='TRUE':
            test_obj.yakshaAssert("TestGmailDotCom", True, "functional")
            print("TestGmailDotCom = Passed")
        else:
            test_obj.yakshaAssert("TestGmailDotCom", False, "functional")
            print("TestGmailDotCom = Failed")

    def test_gmail_co_dot_in(self):
        test_obj = TestUtils()
        result=validate_email_id('venu@gmail.co.in')
        if result=='TRUE':
            test_obj.yakshaAssert("TestGmailCoDotIn", True, "functional")
            print("TestGmailCoDotIn = Passed")
        else:
            test_obj.yakshaAssert("TestGmailCoDotIn", False, "functional")
            print("TestGmailCoDotIn = Failed")

    def test_gmail_co_uk(self):
        test_obj = TestUtils()
        result=validate_email_id('venu@gmail.co.uk')
        if result=='TRUE':
            test_obj.yakshaAssert("TestGmailCoUk", True, "functional")
            print("TestGmailCoUk = Passed")
        else:
            test_obj.yakshaAssert("TestGmailCoUk", False, "functional")
            print("TestGmailCoUk = Failed")

    def test_yahoo_dot_com(self):
        test_obj = TestUtils()
        result=validate_email_id('venu@yahoo.com')
        if result=='TRUE':
            test_obj.yakshaAssert("TestYahooDotCom", True, "functional")
            print("TestYahooDotCom = Passed")
        else:
            test_obj.yakshaAssert("TestYahooDotCom", False, "functional")
            print("TestYahooDotCom = Failed")

    def test_yahoo_dot_co_dot_in(self):
        test_obj = TestUtils()
        result=validate_email_id('venu@yahoo.co.in')
        if result=='TRUE':
            test_obj.yakshaAssert("TestYahooDotCoDotIn", True, "functional")
            print("TestYahooDotCoDotIn = Passed")
        else:
            test_obj.yakshaAssert("TestYahooDotCoDotIn", False, "functional")
            print("TestYahooDotCoDotIn = Failed")

    def test_yahoo_dot_co_dot_uk(self):
        test_obj = TestUtils()
        result=validate_email_id('venu@yahoo.co.uk')
        if result=='TRUE':
            test_obj.yakshaAssert("TestYahooDotCoDotUk", True, "functional")
            print("TestYahooDotCoDotUk = Passed")
        else:
            test_obj.yakshaAssert("TestYahooDotCoDotUk", False, "functional")
            print("TestYahooDotCoDotUk = Failed")

    def test_9_digit_mobile_number(self):
        test_obj = TestUtils()
        result=validate_mobile_number('949340196')
        if result=='FALSE':
            test_obj.yakshaAssert("Test9DigitMobileNumber", True, "functional")
            print("Test9DigitMobileNumber = Passed")
        else:
            test_obj.yakshaAssert("Test9DigitMobileNumber", False, "functional")
            print("Test9DigitMobileNumber = Failed")

    def test_invalid_mobile_number(self):
        test_obj = TestUtils()
        result=validate_mobile_number('5949340196')
        if result=='FALSE':
            test_obj.yakshaAssert("TestInvalidMobileNumber", True, "functional")
            print("TestInvalidMobileNumber = Passed")
        else:
            test_obj.yakshaAssert("TestInvalidMobileNumber", False, "functional")
            print("TestInvalidMobileNumber = Failed")

    def test_invalid_email_id(self):
        test_obj = TestUtils()
        result=validate_email_id('venu@g.com')
        if result=='FALSE':
            test_obj.yakshaAssert("TestInvalidEmailId", True, "functional")
            print("TestInvalidEmailId = Passed")
        else:
            test_obj.yakshaAssert("TestInvalidEmailId", False, "functional")
            print("TestInvalidEmailId = Failed")

    def test_invalid_special_char_email_id(self):
        test_obj = TestUtils()
        result=validate_email_id('venu#gopal@gmail.com')
        if result=='FALSE':
            test_obj.yakshaAssert("TestInvalidSpecialCharEmailId", True, "functional")
            print("TestInvalidSpecialCharEmailId = Passed")
        else:
            test_obj.yakshaAssert("TestInvalidSpecialCharEmailId", False, "functional")
            print("TestInvalidSpecialCharEmailId = Failed")

    def test_first_char_at_email_id(self):
        test_obj = TestUtils()
        result=validate_email_id('1@gmail.com')
        if result=='FALSE':
            test_obj.yakshaAssert("TestFirstCharAtEmailId", True, "functional")
            print("TestFirstCharAtEmailId = Passed")
        else:
            test_obj.yakshaAssert("TestFirstCharAtEmailId", False, "functional")
            print("TestFirstCharAtEmailId = Failed")
