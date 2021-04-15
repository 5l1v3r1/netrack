from setuptools import *

kwargs = {
    "author" : "Nathalon",
    "description" : "netrack 1.0.0 [ARP reconnaissance tool]",
    "entry_points" : {"console_scripts" : ["netrack=netrack.netrack:main"]},
    "license" : "GPL v3",
    "name" : "netrack",
    "packages" : ["netrack"],
    "version" : "V1.0.0",
}

setup(**kwargs)
