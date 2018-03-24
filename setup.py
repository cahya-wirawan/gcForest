import os
from setuptools import setup, find_packages

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except ImportError:
    long_description = open('README.md').read()

__version__ = "1.1.1"
"""
exec(open('setup.cfg').read())
"""

setup(
    name='gcForest',
    version=__version__,
    description='Deep forest: Towards an alternative to deep neural networks',
    long_description=long_description,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Text Processing :: Filters'
    ],
    keywords='machine learning random forest',
    url='https://github.com/kingfengji/gcForest',
    author='Zhi-Hua Zhou',
    author_email='zhouzh@lamda.nju.edu.cn',
    license='MIT',
    packages=find_packages('lib'),
    package_dir={'': 'lib'},
    python_requires='>=2.7, >=3.5',
    install_requires=[
        'joblib',
        'keras',
        'psutil',
        'simplejson',
        'scikit-learn',
        'scipy',
        'tensorflow',
        'xgboost'
    ],
#    scripts=[''],
#    data_files=[(''])],
    include_package_data=True,
    zip_safe=False)
