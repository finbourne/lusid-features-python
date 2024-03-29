import unittest

from parameterized import parameterized

from lusidfeature.lusid_feature import lusid_feature


class ClassWithMethodsWithMoreThanOneDecorator(unittest.TestCase):

    @lusid_feature("F1")
    def test_dummy_method_1(self):
        pass  # Empty for testing purposes

    @lusid_feature("F2")
    @classmethod
    @parameterized.expand(
        [
            ("test1", 1),
            ("test2", 2)
        ]
    )
    def test_dummy_method_2(cls, test1, test2):
        pass  # Empty for testing purposes

    @lusid_feature("F5", "F6")
    @parameterized.expand(
        [
            ("test1", 1),
            ("test2", 2)
        ]
    )
    def test_decorator_with_only_lusidfeature_and_paremeterized(cls, test1, test2):
        pass  # Empty for testing purposes

    def test_control_method(self):
        pass  # Empty for testing purposes

