from setuptools import setup, find_packages

setup(
    name="hello_widget",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["anywidget>=0.6.0"],
    include_package_data=True,
    package_data={"hello_widget": ["static/*"]},
)