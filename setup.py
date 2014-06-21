from distutils.core import setup

setup(
    name='OneCallSMS',
    version='0.0.0.0.1',
    author='Kristoffer Dalby',
    author_email='kradalby@kradalby.no',
    packages=['onecallsms'],
    scripts=[],
    url='https://github.com/kradalby/OneCallSMS',
    license='LICENSE.txt',
    description='Simple package for sending SMS through OneCalls website',
    long_description=open('README.md').read(),
    install_requires=[
        "requests >= 2.3.0",
    ],
)