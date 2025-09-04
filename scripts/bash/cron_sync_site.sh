#!/bin/bash

#############
#
# v 1.0
#
# Output code:
# 0 - Success whatever if there is an update or not
# 1 - Download or untar of lasted release failed

# var definitions
export WEB_DIR="/var/www/"
export SITE_DIRNAME="10s25"
export LATEST_RELEASE_SRC="https://github.com/10s25/site/archive/refs/tags/last.tar.gz"
export LATEST_RELEASE_DIRNAME="site-last"

# sync
cd ${WEB_DIR}
rm -f last.tar*
wget ${LATEST_RELEASE_SRC} 2> /dev/null
tar -xf last.tar.gz
if [ "$?" -eq 0 ]; then
    # the fetch and untar where successful
    diff ${LATEST_RELEASE_DIRNAME} ${SITE_DIRNAME} 1> /dev/null
    if [ "$?" -eq 0 ]; then
        # No change in lasted release
        rm -rf ${LATEST_RELEASE_DIRNAME}
    else
        # New changes detected, replace the site directory with latest
        rm -rf ${SITE_DIRNAME}.save
        mv ${SITE_DIRNAME} ${SITE_DIRNAME}.save
        mv ${LATEST_RELEASE_DIRNAME} ${SITE_DIRNAME}
        chown -R www-data:www-data ${SITE_DIRNAME}
    fi
else
    echo "ERROR: fails to download the lasted release"
    exit 1
fi
exit 0
