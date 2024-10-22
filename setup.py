from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="dio-analisador-excel",
    version="0.0.1",
    author="Ednylton Santos",
    author_email="ednyltonsiilva@hotmail.com",
    description="Um pacote com funções úteis para exibir informações de planilhas excel.",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/EddySDMF/dio-analisador-excel.git",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)