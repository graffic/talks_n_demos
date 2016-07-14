from setuptools import setup

setup(
    name='My Script',
    version=1.0,
    py_modules=['myscript'],
    install_requires=['click'],
    entry_points="""
        [console_scripts]
        myscript=myscript:cli
    """)
