import unittest

from parameterized import parameterized

from lusidfeature.lusid_feature import lusid_feature


class ClassWithTestMethodsUsingManyDecorators(unittest.TestCase):

    # This setUp and tearDown ensures that all tests have been run
    def setUp(self) -> None:
        print(f"Setting up {self._testMethodName}")
        # skip test_control_method
        if self._testMethodName == "test_control_method":
            self.should_be_true = True
        else:
            self.should_be_true = False

    def tearDown(self) -> None:
        print(f"Tearing down {self._testMethodName} \n")
        self.assertTrue(self.should_be_true)

    def test_dummy_method_1(self):
        print(f"inside {self._testMethodName}")
        self.should_be_true = True
        self.assertTrue(self.should_be_true)

    @lusid_feature("F3")
    @parameterized.expand(
        [
            ("test1", 1),
            ("test2", 2)
        ]
    )
    def test_method_with_decorator_on_top(cls, test1, test2):
        print(f"inside {cls._testMethodName}")
        cls.should_be_true = True
        cls.assertTrue(cls.should_be_true)
        cls.assertEqual(type(test1), str)
        cls.assertEqual(type(test2), int)

    @lusid_feature("F4")
    @unittest.skip
    def test_that_skip_works_properly(self):
        print(f"inside {self._testMethodName}")
        self.should_be_true = True
        self.assertTrue(self.should_be_true)

    @parameterized.expand(
        [
            ("test1", 1),
            ("test2", 2)
        ]
    )
    @lusid_feature("F5")  # This should never happen though
    def test_method_with_decorator_on_bottom(self, test1, test2):
        print(f"inside {self._testMethodName}")
        self.should_be_true = True
        self.assertTrue(self.should_be_true)
        self.assertEqual(type(test1), str)
        self.assertEqual(type(test2), int)

    @lusid_feature("F6")
    def test_simple_test_passes(self):
        print(f"inside {self._testMethodName}")
        self.should_be_true = True
        self.assertTrue(self.should_be_true)
