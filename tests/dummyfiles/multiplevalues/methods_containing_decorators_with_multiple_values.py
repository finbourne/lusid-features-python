import unittest

from parameterized import parameterized

from lusidfeature.lusid_feature import lusid_feature


class ClassWithDecoratorsUsingMultipleFeatureValues(unittest.TestCase):

    @lusid_feature("F1")
    def test_dummy_method_1(self):
        pass  # Empty for testing purposes

    @parameterized.expand(
        [
            ("test1", 1),
            ("test2", 2)
        ]
    )
    @lusid_feature("F2", "F5", "F6")
    def test_dummy_method_2(self, test1, test2):
        pass  # Empty for testing purposes

    @lusid_feature("F7", "F8")
    def test_dummy_method_3(self):
        pass  # Empty for testing purposes

    def test_control_method(self):
        pass  # Empty for testing purposes
