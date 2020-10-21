import unittest

from parameterized import parameterized

from lusidfeature.lusid_feature import lusid_feature


class ClassWithDecoratorsUsingDuplicateMultipleFeatureValues(unittest.TestCase):

    @lusid_feature("F1")
    def test_dummy_method_1(self):
        pass  # Empty for testing purposes

    @lusid_feature("F7", "F8", "F8")
    def test_dummy_method_3(self):
        pass  # Empty for testing purposes

    def test_control_method(self):
        pass  # Empty for testing purposes

