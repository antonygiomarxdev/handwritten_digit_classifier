from setuptools import setup, find_packages

setup(
    name='mnist_project',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'tensorflow',
        'numpy',
        'matplotlib',
        'scikit-learn',
        'seaborn'
    ],
    author='Tu Nombre',
    author_email='tuemail@example.com',
    description='Proyecto de reconocimiento de dígitos manuscritos con TensorFlow',
    url='https://github.com/tuusuario/mnist_project',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)
