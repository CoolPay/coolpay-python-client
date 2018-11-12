try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import sys, re

reqs = ['requests>=2.5']

tests_requires = ['nose', 'responses', 'mock']

version = ''
with open('coolpay_api_client/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', fd.read(),
                        re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Cannot find version information')

setup(
    name='coolpay-api-client',
    version=version,
    description='Python client for CoolPay API',
    author_email="hello@coolpay.com",
    author="CoolPay Developers",
    url="https://github.com/CoolPay/coolpay-python-client",
    packages=['coolpay_api_client'],
    license='MIT',
    install_requires=reqs,
    tests_requires=tests_requires,
    test_suite='nose.collector')
