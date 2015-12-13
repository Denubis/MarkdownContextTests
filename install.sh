#!/bin/bash
set -euo pipefail
sudo apt-get update 
sudo apt-get install wget rsync curl ghostscript graphicsmagick inkscape mupdf pstoedit imagemagick pandoc pandoc-citeproc -y 
sudo mkdir -p /opt/context
sudo chown `whoami`:`whoami` /opt/context
cd /opt/context
wget http://minimals.contextgarden.net/setup/first-setup.sh
sh ./first-setup.sh --modules=all
