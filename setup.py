import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django_presskit",
    version="1.1.0",
    author="Future Proof Games",
    author_email="info@futureproofgames.com",
    description="A port of presskit() to Django",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/FutureProofGames/django-presskit.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Framework :: Django :: 1.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
