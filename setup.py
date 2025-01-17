import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='parsinorm-fork',
    version='0.0.4',
    packages=['parsinorm-fork'],
    author="HaraAi",
    author_email="info@hara.ai",
    description="Persain Text Pre-Proceesing Tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/saeid-a/ParsiNorm",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['num2fawords==1.1', 'persian-tools==0.0.10', 'urlextract==1.4.0', 'nltk>=3.6.5', 'hazm>=0.7.0'],
)
