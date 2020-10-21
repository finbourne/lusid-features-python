import unittest

from lusidfeature.feature_extractor import extract_all_features_from_package
from lusidfeature.get_project_root import get_project_root


class FeatureExtractorTests(unittest.TestCase):
    def test_get_valid_decorators(self):
        package = "tests.dummyfiles.valid"
        expected_features = ["F4", "F3", "F1", "F2"]

        feature_list_from_function = extract_all_features_from_package(package, get_project_root())
        expected_set = set(expected_features)
        actual_set = set(feature_list_from_function)

        self.assertEqual(len(feature_list_from_function), 4)
        self.assertEqual(expected_set, actual_set)

    def test_if_throws_error_on_duplicate_decorators(self):
        package = "tests.dummyfiles.duplicates"
        expected_duplicate = "F1"

        with self.assertRaises(Exception) as context:
            extract_all_features_from_package(package, get_project_root())

        self.assertTrue(f'lusid_feature error: Feature code "{expected_duplicate}" is a duplicate. '
                        'Please make sure each feature code is unique. Also make sure lusid_feature '
                        'decorator is on top of any other decorators for that function/method.' in str(context.exception))

    def test_if_throws_error_on_empty_string_value_decorators(self):
        package = "tests.dummyfiles.empties"

        with self.assertRaises(Exception) as context:
            extract_all_features_from_package(package, get_project_root())

        self.assertTrue("lusid_feature error: Some decorated methods have no value passed. "
                        "Please make sure each lusid_feature decorator has a value code passed." in str(
            context.exception))

    def test_if_throws_error_on_no_input_decorators(self):
        package = "tests.dummyfiles.noinput"

        with self.assertRaises(ValueError) as context:
            extract_all_features_from_package(package, get_project_root())

        self.assertTrue("lusid_feature error: Decorator requires at least some input." in str(context.exception))

    def test_if_returns_empty_list_with_no_annotations(self):
        package = "tests.dummyfiles.notannotated"
        expected_features = []

        feature_list_from_function = extract_all_features_from_package(package,get_project_root())

        self.assertEqual(len(feature_list_from_function), 0)
        self.assertEqual(feature_list_from_function, expected_features)

    def test_if_functions_get_annotated(self):
        package = "tests.dummyfiles.functions"
        expected_features = ["F1", "F2", "F3"]

        feature_list_from_functions = extract_all_features_from_package(package, get_project_root())

        self.assertEqual(len(feature_list_from_functions), 3)
        self.assertEqual(set(expected_features), set(feature_list_from_functions))

    def test_if_throws_error_on_no_decorator_brackets(self):
        package = "tests.dummyfiles.nobrackets"

        with self.assertRaises(Exception) as context:
            extract_all_features_from_package(package, get_project_root())

        self.assertTrue("lusid_feature error: Decorator requires a string input parameter." in str(
            context.exception))

    def test_if_returns_correct_codes_with_multiple_decorators(self):
        package = "tests.dummyfiles.multidecorator"
        expected_features = ["F1", "F2", "F3", "F4"]

        feature_list_from_functions = extract_all_features_from_package(package, get_project_root())

        self.assertEqual(set(expected_features), set(feature_list_from_functions))

    def test_if_returns_correct_codes_with_multiple_decorator_inputs_in_module(self):
        package = "tests.dummyfiles.multiplevalues.methods_containing_decorators_with_multiple_values"
        expected_features = ["F1", "F2", "F5", "F6", "F7", "F8"]

        feature_list_from_functions = extract_all_features_from_package(package, get_project_root())

        self.assertEqual(set(expected_features), set(feature_list_from_functions))

    def test_if_returns_correct_codes_with_multiple_decorator_inputs_in_package(self):
        package = "tests.dummyfiles.multiplevalues"
        expected_features = ["F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8"]

        feature_list_from_functions = extract_all_features_from_package(package, get_project_root())

        self.assertEqual(set(expected_features), set(feature_list_from_functions))

    def test_if_throws_error_on_duplicate_multiple_decorator_input(self):
        package = "tests.dummyfiles.errorsmultiplevalues.methods_containing_decorators_with_duplicate_multiple_values"
        expected_duplicate = "F8"

        with self.assertRaises(Exception) as context:
            extract_all_features_from_package(package, get_project_root())

        self.assertTrue(f"lusid_feature error: Feature code \"{expected_duplicate}\" is a duplicate." in str(
            context.exception))

    def test_if_throws_error_on_multiple_decorator_input_having_empty_values(self):
        package = "tests.dummyfiles.errorsmultiplevalues.methods_containing_multivalue_decorators_with_empty_strings"

        with self.assertRaises(Exception) as context:
            extract_all_features_from_package(package, get_project_root())

        self.assertTrue("lusid_feature error: Some decorated methods have no value passed. "
                        "Please make sure each lusid_feature decorator has a value code passed." in str(
            context.exception))

