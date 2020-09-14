# lusid-features-python
=======
# Lusid Feature Decorator Scanner

## Description

This repository contains source code which provides a python decorator called 'lusid_feature', dasdf

## Usage

### Installing

Run:
```
pip install lusidfeatures
```

### Importing

This repository has two main functions that need to be imported for the scanner to work

1. lusid_feature in lusid_feature.py - The decorator used with functions and methods
2. get_features_file(argv) in entrypoint - The function that extracts all decorator values and writes them to a file

lusid_feature example import:
```
from lusidfeatures.lusid_feature import lusid_feature
```

get_features_file(argv) example import:
```
from lusidfeatures.entrypoint import get_features_file
```

### Implementing lusid_feature decorator

When successfully imported, lusid_feature decorator can be used to decorate functions and methods in the following manner: 

```
@lusid_feature("F1")
def some_function():
    # function/method implementation
```

Rules around using lusid_feature decorator:
- The decorator must always be called with brackets, and have a string value passed. Correct: ```@lusid_feature("F1")``` Wrong:```@lusid_feature```
- The decorator must not have an empty string passed. The following will throw an error: ```@lusid_feature("")```
- The decorator must not have duplicate feature values across the package files that are being scanned. The following with throw an error:
```
@lusid_feature("F1")
def some_function():
    # function/method implementation

@lusid_feature("F1")
def some_other_function():
    # function/method implementation
```
- The decorator value should start with a capital 'F'
### Running the decorator scanner

To extract the feature values and write them to a file, the following function must be imported and run from a main function in a main.py file:

```
def main(argv):
    get_features_file(argv)


if __name__ == "__main__":
    main(sys.argv)

```

the **sys.argv** input variable should be passed as multiple parameters from the command line, which will be later parsed with argparser


### Input parameters (sys.argv)

The command line requires two parameters

- --outpath or -o
This is the directory and filename of where the features text file should be written
Example:
```
-o <your-absolute-path>/<your-filename>.txt
```
- --package or -p
This is the package that the decorator scanner should look for decorators in
Example:
```
-p <package>.<packagenext>.<packagenext>
```

To run, set your PYTHONPATH for the required folders and run the following example in a similar way:

```
python main.py -p "tests.tutorials" -o "/usr/app/features.txt"
```

## Output file

The decorator scanner should write a file to the specified path with the example content:

features.txt

```
F1
F32
F2
F3
F10
F11
F8
etc...
```
