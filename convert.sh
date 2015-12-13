#!/bin/bash

if [ -z $1 ]; then
	echo "./convert.sh foo.md"
	exit 1;
fi

fullfile=$1


filename=$(basename "$fullfile")
extension="${filename##*.}"
filename="${filename%.*}"

pandoc --smart --normalize -f markdown -t native --filter ./contextBibliography.py -o $filename.nat $1
pandoc --natbib --template ./template.unitTest --smart --normalize -f markdown -t context --filter ./contextBibliography.py  -o $filename.tex $1

# we will try to guess the platform first
# (needs to be kept in sync with first-setup.sh and mtxrun)
# if yours is missing, let us know

system=`uname -s`
cpu=`uname -m`

case "$system" in
	# linux
	Linux)
		case "$cpu" in
			i*86) platform="linux" ;;
			x86_64|ia64) platform="linux-64" ;;
			# a little bit of cheating with ppc64 (won't work on Gentoo)
			ppc|ppc64) platform="linux-ppc" ;;
			# we currently support just mipsel, but Debian is lying (reports mips64)
			# we need more hacks to fix the situation, this is just a temporary solution
			mips|mips64|mipsel|mips64el) platform="linux-mipsel" ;;
			# TODO: probably both wrong and incomplete
			armv7l) platform="linux-armhf" ;;
			*) platform="unknown" ;;
		esac ;;
esac

#
# PATH
#

# this resolves to path of the setuptex script
# We use $0 for determine the path to the script, except for:
# * bash where $0 always is bash; here we use BASH_SOURCE
# * ksh93 where we use ${.sh.file}
# Thanks to Vasile Gaburici and Alessandro Perucchi for reporting this
# * http://www.ntg.nl/pipermail/ntg-context/2008/033953.html
# * http://www.ntg.nl/pipermail/ntg-context/2012/068658.html
if [ z"$BASH_SOURCE" != z ]; then
	SCRIPTPATH="$BASH_SOURCE"
elif [ z"$KSH_VERSION" != z ]; then
   	SCRIPTPATH="${.sh.file}"
else
	SCRIPTPATH="$0"
fi

OWNPATH=/opt/context/tex

# but one can also call
# . setuptex path-to-tree

TEXROOT=""
# first check if any path has been provided in the argument, and try to use that one
if [ -f "$OWNPATH/texmf/tex/plain/base/plain.tex" ]; then
	if [ -d "$OWNPATH/texmf-$platform/bin" ]; then
		TEXROOT="$OWNPATH"
	else
		echo "Binaries for platform '$platform' are missing."
		echo "(There is no folder \"$OWNPATH/texmf-$platform/bin\")"
	fi
else
	echo "\"$OWNPATH\" is not a valid TEXROOT path."
	echo "(There is no file \"$OWNPATH/texmf/tex/plain/base/plain.tex\")"
fi

if [ "$TEXROOT" != "" ]; then
	# for Alan Braslau's server :)
	if [ "x$PS1" != "x" ] ; then
		echo "Setting \"$TEXROOT\" as ConTeXt root."
	fi

# ConTeXt binaries have to be added to PATH
TEXMFOS=$TEXROOT/texmf-$platform
export PATH=$TEXMFOS/bin:$PATH

# unset variables that won't be used lately
unset platform cpu system OWNPATH SCRIPTPATH ARGPATH TEXMFOS

# not sure why this would be needed
# export CTXMINIMAL=yes

else
	echo "provide a proper tex root (like '. setuptex /something/tex')" ;
fi



context --batchmode -quiet unittest.tex