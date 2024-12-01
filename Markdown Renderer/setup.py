from setuptools import setup, find_packages

setup(
    name="my_package",  # The name of your package
    version="0.1.0",  # The version of your package
    packages=find_packages(),  # Automatically find packages in the directory
    install_requires=[
        'pywebview',
        'markdown',
        'flask'
    ],
    description="A brief description of your package",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/my_package"
)
