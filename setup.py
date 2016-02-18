import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='cf-pretty-form-errors',
    version='1.0.4',
    packages=['cf_pretty_form_errors', ],
    include_package_data=True,
    license='BSD License',
    description='Make your crispy form errors more pretty',
    long_description=README,
    keywords='crispy-forms errors',
    url='https://github.com/razortheory/cf-pretty-form-errors',
    author='Roman Karpovich',
    author_email='fpm.th13f@gmail.com',
    install_requires=['django-crispy-forms', ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    zip_safe=True
)
