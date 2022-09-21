#   ---------------------------------------------------------
#   Copyright (c) 2020 Microsoft Corporation. All rights reserved.
#   ---------------------------------------------------------
"""Azure Managed Applications Python SDK"""
from os import environ

from setuptools import find_packages, setup  # noqa: H301

from azureiai import generate_swagger

SWAGGER_JSON = "Partner_Ingestion_SwaggerDocument.json"
generate_swagger(SWAGGER_JSON)

NAME = "az-partner-center-cli"
VERSION = "0.0.42"

REQUIRES = [
    "azure-mgmt-deploymentmanager",
    "azure-mgmt-resource",
    "azure-storage-blob",
    "azure-identity>=1.2.0",
    "urllib3 >= 1.15",
    "six >= 1.10",
    "certifi",
    "python-dateutil",
    "requests",
    "pyyaml",
    "pygments",
    "wget",
    "adal",
    "cryptography>=3.3.1",
]

ENTRY_POINTS = {"console_scripts": ["ama=azureiai.ama_app:main", "azpc=azureiai.azpc_app:main"]}

setup(
    name=NAME,
    version=VERSION,
    description="https://api.partner.microsoft.com/v1.0/ingestion",
    author_email="",
    url="",
    keywords=["Swagger", "https://api.partner.microsoft.com/v1.0/ingestion"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""
    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501
    """,
    entry_points=ENTRY_POINTS,
    python_requires=">=3.7,<4",
)
