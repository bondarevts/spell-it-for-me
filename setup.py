from setuptools import setup

with open('README.md') as readme_file:
    long_description = readme_file.read()

setup(
    name='spell-it-for-me',
    version='0.1.1',
    url='https://github.com/bondarevts/spell-it-for-me',
    author='Timofei Bondarev',
    author_email='bondarevts@gmail.com',
    description='A simple command line tool to display a spelling for any phrase using a phonetic alphabet.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    py_modules=['spell'],
    entry_points={'console_scripts': ['spell = spell:main']},
    package_dir={'': 'src'},
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Operating System :: OS Independent',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Communications',
        'Topic :: Utilities',
    ],
)
