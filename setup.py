from setuptools import setup
from cloud_security_posture_management.__version__ import __version__


setup(
    name="cloud_security_posture_management",
    version=__version__,
    author="sumit",
    author_email="sumit@mail.com",
    description="cloud-security-posture-management",
    long_description=open("README.md").read(),
    classifiers=[
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.12",
    entry_points={
        "console_scripts": [
            "cloud_security_posture_management=cloud_security_posture_management.main:main",
        ],
    },
)
