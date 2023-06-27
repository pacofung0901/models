"""Setup script for object_detection with TF2.0."""
import os
from setuptools import find_packages
from setuptools import setup

REQUIRED_PACKAGES = [
    # Required for apache-beam with PY3
    'avro-python3==1.10.2',
    'apache-beam==2.43.0',
    'pillow==7.0.0',
    'lxml==4.5.0',
    'matplotlib==3.6.2',
    'Cython==0.29.33',
    'contextlib2==21.6.0',
    'tf-slim==1.1.0',
    'six==1.14.0',
    'pycocotools==2.0.6',
    'lvis==0.5.3',
    'scipy==1.10.0',
    'pandas==1.5.2',
    'tf-models-official==2.11.2',
    'tensorflow_io==0.29.0',
    'keras==2.11.0',
    'pyparsing==2.4.7',  # TODO(b/204103388)
    'sacrebleu==2.2.0'  # https://github.com/mjpost/sacrebleu/issues/209
]

setup(
    name='object_detection',
    version='0.1',
    install_requires=REQUIRED_PACKAGES,
    include_package_data=True,
    packages=(
        [p for p in find_packages() if p.startswith('object_detection')] +
        find_packages(where=os.path.join('.', 'slim'))),
    package_dir={
        'datasets': os.path.join('slim', 'datasets'),
        'nets': os.path.join('slim', 'nets'),
        'preprocessing': os.path.join('slim', 'preprocessing'),
        'deployment': os.path.join('slim', 'deployment'),
        'scripts': os.path.join('slim', 'scripts'),
    },
    description='Tensorflow Object Detection Library',
    python_requires='>3.6',
)
