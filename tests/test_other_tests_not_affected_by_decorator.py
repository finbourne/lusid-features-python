import unittest

from parameterized import parameterized

from lusidfeature.lusid_feature import lusid_feature


class ClassWithTestMethodsUsingManyDecorators(unittest.TestCase):

    def test_dummy_method_1(self):
        self.assertTrue(True)

    @lusid_feature("F3")
    @classmethod
    @parameterized.expand(
        [
            ("test1", 1),
            ("test2", 2)
        ]
    )
    def test_dummy_method_2(cls, test1, test2):
        cls.assertTrue(type(test1) == str)
        cls.assertTrue(type(test2) == int)

    @lusid_feature("F4")
    @unittest.skip
    def test_control_method(self):
        pass  # Empty for testing purposes

    @parameterized.expand(
        [
            ("test1", 1),
            ("test2", 2)
        ]
    )
    @lusid_feature("F5")
    def test_dummy_method_2(self, test1, test2):
        self.assertTrue(type(test1) == str)
        self.assertTrue(type(test2) == int)

