import unittest

from lusidfeature.lusid_feature import lusid_feature


class ControlClassWithDecoratorWithBracketsButNoInputValue(unittest.TestCase):

    @lusid_feature()
    def test_dummy_method_1(self):
        pass  # Empty for testing purposes

    @lusid_feature("F5")
    def test_control_method(self):
        pass  # Empty for testing purposes
