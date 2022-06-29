import unittest
from validate_mobile_number import validate_mobile_number
from validate_email_id import validate_email_id
from test.TestUtils import TestUtils
class ExceptionalTest(unittest.TestCase):
    def test_type_error_for_mobile_number(self):
        test_obj = TestUtils()
        try:
            validate_mobile_number(9640647024)
            test_obj.yakshaAssert("TestTypeErrorForMobileNumber", False, "exception")
            print("TestTypeErrorForMobileNumber = Failed")
        except TypeError:
            test_obj.yakshaAssert("TestTypeErrorForMobileNumber", True, "exception")
            print("TestTypeErrorForMobileNumber = Passed")

    def test_type_error_for_mail_id(self):
        test_obj = TestUtils()
        try:
            validate_email_id(12345)
            test_obj.yakshaAssert("TestTypeErrorForMailId", False, "exception")
            print("TestTypeErrorForMailId = Failed")
        except TypeError:
            test_obj.yakshaAssert("TestTypeErrorForMailId", True, "exception")
            print("TestTypeErrorForMailId = Passed")
