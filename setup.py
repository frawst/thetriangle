from setuptools import setup

with open('README.md') as f:
    readme = f.read()

# TODO Add author email.
setup(
    name='thetriangle',
    description='Generate serpinski triangles using cool maths',
    long_description=str(readme),
    license='MIT',
    author='Justyn Chaykowski',
    author_email='frawst@live.ca'
    url='https://github.com/frawst/thetriangle',
    install_requires=['pillow'],
    classifiers=[
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Education',
            'Natural Language :: English',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5'
        ],
)
