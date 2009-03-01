#!/usr/bin/env bash

DEST_DIR=~/Library/Application\ Support/Quicksilver/Actions

if [ ! -d "$DEST_DIR" ] ; then 
    echo "creating target directory!" ; 
    mkdir -p "$DEST_DIR"
fi

echo "installing Quicksilver action"
cat <<EOF > "$DEST_DIR/tweet.py"
#!/usr/bin/env python
# encoding: utf-8
__requires__ = 'twitsilver>=0.1dev'
import sys
from pkg_resources import load_entry_point

sys.exit(
   load_entry_point('twitsilver==0.1dev', 'console_scripts', 'tweet')()
)
EOF
chmod a+x "$DEST_DIR/tweet.py"
echo "Done! Now restart Quicksilver (command-control-q)"
