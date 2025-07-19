from setuptools import setup, find_packages

setup(
    name="gufic_env",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "scipy==1.15.2",
        "mujoco==3.3.0",
        "matplotlib",
        "sympy",
        "control",
        "tikzplotlib",
    ],
)