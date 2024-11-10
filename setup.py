from setuptools import setup, find_packages

setup(
    name='math_quiz',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'math_quiz=math_quiz.math_quiz:math_quiz',
        ],
    },
    install_requires=[
        # Add your dependencies here if you have any
    ],
    author='piyal94',
    author_email='shahriarpiyal@gmail.com',
    description='A simple math quiz game',
    license='MIT',
    url='https://github.com/piyal94/dsss_homework_2_',
)
