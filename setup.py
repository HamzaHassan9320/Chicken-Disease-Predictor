import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

Repo_Name = "Chicken-Disease-Predictor"
Author_User_Name = "HamzaHassan9320"
Src_Repo = "ChickenDiseaseCNN"
Author_Email = "hamza_hassan45@hotmail.com"

setuptools.setup(
    name=Src_Repo,
    version=__version__,
    author=Author_User_Name,
    author_email=Author_Email,
    description="A small python package for CNN application",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/HamzaHassan9320/Chicken-Disease-Predictor",
    project_urls={
        "Bug Tracker": f"https://github.com/HamzaHassan9320/Chicken-Disease-Predictor/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)
