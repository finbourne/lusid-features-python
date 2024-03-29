import importlib
import inspect
import pkgutil

from lusidfeature.get_project_root import get_project_root


def get_decorator_values_from_classes(module):
    classes = inspect.getmembers(module, predicate=inspect.isclass)
    for cls_name, cls in classes:
        # get all class methods that are not inherited. Avoids duplicate extraction
        methods = [(n, m) for (n, m) in cls.__dict__.items() if callable(m)]
        for method_name, method in methods:
            if hasattr(method, "decorator_value"):
                yield method.decorator_value


def get_decorator_values_from_functions(module):
    functions = inspect.getmembers(module, predicate=inspect.isfunction)
    for function_name, function in functions:
        if hasattr(function, "decorator_value"):
            yield function.decorator_value


def extract_all_features_from_package(package_name, root):
    feature_list = []
    for importer, name, is_pkg in pkgutil.walk_packages([root]):
        if is_pkg or not name.startswith(package_name):
            continue

        module = importlib.import_module(name)

        for feature_codes in get_decorator_values_from_classes(module):
            feature_list = feature_list + feature_codes

        for feature_codes in get_decorator_values_from_functions(module):
            feature_list = feature_list + feature_codes

    return feature_list
