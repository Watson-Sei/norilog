import os
from setuptools import setup, find_packages

def read_file(filename):
    basepath = os.path.dirname(os.path.dirname(__file__))
    filepath = os.path.join(basepath, filename)
    if os.path.exists(filepath):
        return open(filepath).read()
    else:
        return ''

setup(
    name='norilog1',
    version='1.0.0',
    description='The NoriLog1 web application',
    long_description=read_file('README.rst'),
    author='Watson-Sei',
    author_email='seinabehack@gmail.com',
    url='https://github.com/Watson-Sei/norilog',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Flask',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7'
    ],
    package=find_packages(),
    include_package_data=True,
    license='BSD License',
    install_requires=[
        'Flask',
    ],
    entry_points = """
        [console_scripts]
        norilog1 = norilog1:main
    """,
)
