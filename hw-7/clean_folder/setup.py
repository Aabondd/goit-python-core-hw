from importlib.metadata import entry_points
from setuptools import setup, find_packages

setup(
    name='clean_folder',
    version='0.0.1',
    entry_points={'console_scripts': ['clean-folder=clean_folder.clean:start'],},
    description='clean&sort folder script',
    author='Oleksandr Bondareko',
    author_email='aabondd@gmail.com',
    license='MIT',
    packages=find_packages(),
)