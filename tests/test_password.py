import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "app"))

from server import is_password_valid  # noqa: E402


class TestPasswordValidation(unittest.TestCase):
    def test_rejects_common_password(self):
        self.assertFalse(is_password_valid("password"))

    def test_rejects_too_short(self):
        self.assertFalse(is_password_valid("Ab1!"))

    def test_rejects_missing_uppercase(self):
        self.assertFalse(is_password_valid("lowercase123!"))

    def test_rejects_missing_lowercase(self):
        self.assertFalse(is_password_valid("UPPERCASE123!"))

    def test_rejects_missing_digit(self):
        self.assertFalse(is_password_valid("NoDigitsHere!"))

    def test_rejects_missing_special_char(self):
        self.assertFalse(is_password_valid("NoSpecialChar123"))

    def test_accepts_valid_password(self):
        self.assertTrue(is_password_valid("SUPERsecurepass31231!@#"))


if __name__ == "__main__":
    unittest.main()
