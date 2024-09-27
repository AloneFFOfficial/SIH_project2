from setuptools import setup, find_packages

setup(
    name = "SIH_project2",
    version='0.1',
    packages=find_packages(),
    install_requires=[dotenv,streamlit,generativeai,spacy,langchain],

)
