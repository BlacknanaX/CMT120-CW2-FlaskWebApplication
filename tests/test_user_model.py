import unittest
from blog.models import User


class UserModelTestCase(unittest.TestCase):
    def test_password_setter(self):
        u = User(password='123456')
        self.assertEqual(u.password_hash is not None)

    def test_no_password_getter(self):
        u = User(password='123455')
        with self.assertEqual(AttributeError):
            u.password

    def test_password_verification(self):
        u = User(password='123456')
        self.assertTrue(u.verify_password('123456'))
        self.assertFalse(u.verify_password('098765'))

    def test_password_slts_are_random(self):
        u = User(password='123456')
        u2 = User(password='123456')
        self.assertTrue(u.password_hash != u2.password_hash )


# if __name__ == '__main__':
#     unittest.main()
