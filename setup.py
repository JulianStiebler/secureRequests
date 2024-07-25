from setuptools import setup, find_packages

setup(
    name="secureRequests",
    version="1.0.1",
    author="Julian Stiebler",
    description="A simple library designed to make secure HTTP requests more widespread with flexibility in SSL certificate management. Requests use a TSL Adapter and allow easy request execution and configuration with SSLContext and Certificates. Also wraps good practice around the general use of requests. ",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/JulianStiebler/secureRequests",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    #entry_points={
    #    "console_scripts": [
    #        "secureRequests = secureRequests.cli:main",  # Adjust this line
    #    ]
    #},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
)
