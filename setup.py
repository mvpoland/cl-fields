from setuptools import setup, find_packages
import cl_fields


setup(
    name="cl-fields",
    version=cl_fields.__version__,
    url='https://github.com/citylive/cl-fields/',
    license='BSD',
    description='CityLive fields & filters',
    long_description=open('README.rst', 'r').read(),
    author='Gert van Gool, City Live nv',
    packages=find_packages('.'),
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'Environment :: Web Environment',
        'Framework :: Django',
    ],
)
