from setuptools import find_packages, setup
with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()
setup(
    name='turkish-name-generator',
    packages=find_packages(include=['trnamegen']),
    include_package_data=True,
    data_files=[('', ["trnamegen/data/isimler.csv", "trnamegen/data/soyisimler.txt"])],
    version='1.0.6',
    description='This package generates random Turkish names. You can choose the gender of name and you can get also only first name or last name.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    url="https://github.com/MrMirhan/turkish-name-generator",
    author='MrMirhan',
    author_email='me@mirhan.net',
    license='MIT',
    install_requires=['pandas']
)