from setuptools import setup, find_packages

setup(
    name="notes_app",
    version="1.0.0",
    description="Note taking app",
    long_description_content_type="text/markdown",
    author="Soumahoro",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(),
    install_requires=[
        "flask",
        "sqlalchemy",
        "psycopg2-binary",
    ],
    entry_points={"console_scripts": []},
)
