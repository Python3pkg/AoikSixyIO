import os
from setuptools import find_packages
from setuptools import setup

setup(
    name='AoikSixyIO',

    version='0.1.0',

    description="""Make Python string encoding and IO code 2*3 compatible, mess-free, and error-proof.""",

    long_description="""`Documentation on Github
<https://github.com/AoiKuiyuyou/AoikSixyIO>`_""",

    url='https://github.com/AoiKuiyuyou/AoikSixyIO',

    author='Aoi.Kuiyuyou',

    author_email='aoi.kuiyuyou@google.com',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],

    keywords='',

    package_dir={'':'src'},

    packages=find_packages('src'),

    entry_points={
        'console_scripts': [
            'aoiksixyioexp=aoiksixyio.aoiksixyioexp:main',
        ],
    },
)
