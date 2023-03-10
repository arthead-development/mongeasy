from setuptools import setup, find_packages

setup(
    name='mongeasy',
    version='0.1.0',
    description='A simple and easy-to-use Python wrapper around the pymongo library.',
    url='https://github.com/username/mongeasy',
    author='Joakim Wassberg',
    author_email='joakim.wassberg@arthead.se',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Database',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='mongodb pymongo database wrapper orm',
    python_requires='>=3.8',
    packages=find_packages(),
    install_requires=[
        'pymongo>=4.3.3',
        'bcrypt>=4.0.1',
        'pydantic>=1.10.5',
        'marshmallow>=3.19.0',
        'voluptuous>=0.13.1'
    ],
    extras_require={
        'dev': [
            'pytest>=7.2.1',
            'pytest-cov>=4.0.0',
        ],
    },
)
