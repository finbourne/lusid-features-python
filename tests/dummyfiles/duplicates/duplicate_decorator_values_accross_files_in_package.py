import unittest

from lusidfeature.lusid_feature import lusid_feature


class ThisPackageContainsDuplicateFeatureAcrossTwoFiles(unittest.TestCase):

    @lusid_feature("F1")
    def test_dummy_method_1(self):
        pass  # Empty for testing purposes

    @lusid_feature("F2")
    def test_control_method(self):
        pass  # Empty for testing purposes
