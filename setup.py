from setuptools import find_packages,setup

setup(
    name='mcqgeneraor',
    version='0.0.1',
    author='Pushkar-Morankar',
    author_email='thepushkarmorankar@gmail.com',
    install_requires=["openai","langchian","streamlit","python-dotenv","PyPDF2"],
    packages= find_packages()
)