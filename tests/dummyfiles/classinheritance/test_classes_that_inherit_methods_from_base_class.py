import unittest

from lusidfeature.lusid_feature import lusid_feature


class BaseClass(object):

    @lusid_feature("F1", "F2")
    def test_dummy_method_1(self):
        pass  # Empty for testing purposes

    def test_control_method(self):
        pass  # Empty for testing purposes


class ExtendedClass1(unittest.TestCase, BaseClass):

    @lusid_feature("F3")
    def test_dummy_method_not_override_1(self):
        pass  # Empty for testing


class ExtendedClass2(unittest.TestCase, BaseClass):

    @lusid_feature("F4", "F5")
    def test_dummy_method_1(self):
        pass  # Empty for testing

    def control_method(self):
        pass # Empty for testing
