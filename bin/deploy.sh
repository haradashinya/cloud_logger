#!/bin/bash
pip install wheel --user
python setup.py sdist bdist_wheel
python setup.py sdist upload


