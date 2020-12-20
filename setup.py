import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django_presskit",
    version="1.3.0",
    author="Future Proof Games",
    author_email="info@futureproofgames.com",
    description="A port of presskit() to Django",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/FutureProofGames/django-presskit.git",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Framework :: Django :: 2.2",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
)
