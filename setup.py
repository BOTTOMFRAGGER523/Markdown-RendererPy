from setuptools import setup, find_packages

setup(
    name="markdownrenderer",  # The name of your package
    version="1.0",  # The version of your package
    packages=find_packages(),  # Automatically find packages in the directory
    install_requires=[
        'pywebview',
        'markdown',
        'flask'
    ],
    description="A brief description of your package",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="BOTTOMFRAGGER523",
    url="https://github.com/BOTTOMFRAGGER523/Markdown-RendererPy"
)
