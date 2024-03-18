import unittest
from email_validate import Email


class TestEmailValidate(unittest.TestCase):
    """A test for the class Email"""
    
    def test_valid_email(self):
        valid_emails = [
            "test@example.com",
            "user123@gmail.com",
            "user.name12345@domain.co.uk"
        ]

        for email in valid_emails:
            self.assertTrue(Email.validate(email))
            

    def test_invalid_email(self):
        invalid_emails = [
            "invalidemail.com",
            "user@",
            "@domain.com",
            "user@domain",
            "user@domain."
        ]

        for email in invalid_emails:
            self.assertFalse(Email.validate(email))


if __name__ == "__main__":
    unittest.main()
        

    
