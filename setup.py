from setuptools import setup, find_packages

setup(
    name='scrpproxies',
    url='https://github.com/jenslaufer/scrpproxies',
    author='Jens Laufer',
    author_email='jenslaufer@gmail.com',
    packages=['scrpproxies'],
    install_requires=['pandas'],
    version='0.2.0',
    license='MIT',
    description='module for proxy rotation for scraping',
    include_package_data=True
)

