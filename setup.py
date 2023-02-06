from setuptools import setup, find_packages

def readme():
    with open('README.md') as f:
        README = f.read()
    return README

    
setup(
    name='js',
    version='0.0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Convert job descriptions to skills needed for that job',
    url='https://github.com/ujjwal-upadhyay/Testing_DATA534',
    author='Ujjwal, Varshita, Nowshabha',
    author_email='ypadhyay.ujjwal007@gmail.com',
    python_requires='>=3.9',
)
