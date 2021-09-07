from setuptools import find_packages, setup
setup(
    name='turkish-name-generator',
    packages=find_packages(include=['trnamegen', 'trnamegen.data']),
    data_files=[("data", ["data/isimler.txt", "data/soyisimler.txt"])],
    version='1.0.0',
    description='This package generates random Turkish names. You can choose the gender of name and you can get also only first name or last name.',
    author='MrMirhan',
    author_email='me@mirhan.net',
    license='MIT',
    install_requires=['pandas'],
    setup_requires=['pandas'],
    tests_require=['pandas'],
    test_suite='tests'
)