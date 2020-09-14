from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name='lusidfeatures',
    version='0.0.1',
    description='This package will allow to run the main file and retrieve a list of decorated feature methods in a cls',
    long_description=readme(),
    long_description_content_type='text/markdown',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    url='https://github.com/NotCreatedYet',
    author='Sebastian Lacki',
    email='sebastian.lacki@finbourne.com',
    license='MIT',
    keywords='core package',
    packages=['lusidfeatures'],
    install_requires=['parameterized>=0.7.4'],
    include_package_data=True,
    zip_safe=False
)
