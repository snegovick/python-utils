#!/bin/bash

echo "======================"
echo "Modifying setup.py"
echo "======================"

VSTRING=$( cat ./packaging/version )
echo "VSTRING: ${VSTRING}"
sed -r -e "s/( *)version =/\1version = \"${VSTRING}\",/" ./packaging/setup.py.in > setup.py

echo "======================"
echo "Modifying stdeb.cfg"
echo "======================"

DEB_VERSION=$( cat ./packaging/deb-version )
LSB_RELEASE=$( lsb_release -r | sed -e "s/Release:\t*//")
sed -e "s/Debian-Version:/Debian-Version: ${DEB_VERSION}/" ./packaging/stdeb.cfg.in | sed -e "s/suite:/suite: ${LSB_RELEASE}/" > ./stdeb.cfg

echo "======================"
echo "Building package"
echo "======================"

rm -rf deb_dist
python ./setup.py --command-packages=stdeb.command sdist_dsc --suite="${LSB_RELEASE}"
cd ./deb_dist/python-utils-${VSTRING}
debuild
cd ../../
