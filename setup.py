from setuptools import setup
from setuptools import find_packages

setup(
    name='BBC_foods_web_scraper',
    version='0.0.1',
    description='Package allows you to scrape data from given website',
    url='https://github.com/RaghulSekar1997/Data-Collection-Pipeline',
    author='Raghul Sekar',
    license='MIT',
    packages=find_packages(),
    install_requires=['boto3', 'pandas', 'selenium', 'sqlalchemy'],
)