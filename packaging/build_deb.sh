#!/bin/bash

echo "======================"
echo "Modifying setup.py"
echo "======================"

VSTRING=$(git describe --tags --long | sed -e "s/v//")
echo "VSTRING: ${VSTRING}"
sed -r -e "s/( *)version =/\1version = \"${VSTRING}\",/" ./packaging/setup.py.in > setup.py

echo "======================"
echo "Modifying stdeb.cfg"
echo "======================"

cp ./packaging/stdeb.cfg ./stdeb.cfg

echo "======================"
echo "Building package"
echo "======================"

rm -rf deb_dist
python ./setup.py --command-packages=stdeb.command sdist_dsc --suite="testing"
cd ./deb_dist/python-utils-${VSTRING}
debuild
cd ../../


