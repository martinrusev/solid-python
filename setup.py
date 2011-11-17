from setuptools import setup

version = '0.2.2'

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
    author_email='martin@amon.cx',
    url='https://github.com/martinrusev/amon-clients/python/amonpy',
    license='BSD',
	packages=['amonpy','amonpy.adapters'],
    package_dir={'amonpy':'amonpy'},
    zip_safe=False,
    install_requires=['requests',],
) 
