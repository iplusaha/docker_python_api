from setuptools import setup

setup(
    name='AWS EC2 Pricing',
    version='0.1',
    long_description=__doc__,
    packages=['ec2_costing'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask']
)

