from setuptools import setup

version = '0.1.2'

setup(
    name='amonpy',
    version=version,
    description="Python client for the Amon API",
    long_description= open('README.rst').read(),
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Environment :: Web Environment",
    ],
    keywords='amon, monitoring, api,',
    author='Martin Rusev',
    author_email='martinrusev@live.com',
    url='https://github.com/martinrusev/amon-clients/python/amonpy',
    license='BSD',
	packages=['amonpy',],
    package_dir={'amonpy':'amonpy'},
    zip_safe=False,
    install_requires=['setuptools','requests',],
) 
