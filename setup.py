import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "Fake-Image-Detection"
AUTHOR_USER_NAME = "Jay-sanjay"
SRC_REPO = "cnnClassifier"  # taken as local package name
AUTHOR_EMAIL = "landgejay@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A Compact Facial Video Forgery Detection Network using Deep Learning ",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/Jay-sanjay/Fake-Image-Detection",
    project_urls={
        "Bug Tracker": f"https://github.com/Jay-sanjay/Fake-Image-Detection/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)
