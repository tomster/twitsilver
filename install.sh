#!/usr/bin/env bash

python setup.py install

DEST_DIR=~/Library/Application\ Support/Quicksilver/Actions/

if [ ! -d "$DEST_DIR" ] ; then 
    echo "creating target directory!" ; 
    mkdir -p "$DEST_DIR"
fi

echo "installing Quicksilver action"
cp bin/tweet "$DEST_DIR"
