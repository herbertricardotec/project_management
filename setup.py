from setuptools import setup, find_packages

setup(
    name='project_management',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'flask',
        'flask-sqlalchemy',
        'flask-migrate',
        'flask-cors',
        'flask-jwt-extended',
        'python-dotenv'
    ],
)