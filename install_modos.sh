#!/bin/bash
#
# install_modos -- install the `modo` scripts
#
# 2020-01-15    `l10nrestore` is now a zsh script.

declare instopts localgroup prefix src

# Settings
grep -q staff /etc/group && localgroup=staff
grep -q wheel /etc/group && localgroup=wheel
: ${localgroup:=root}
prefix=/usr/local
instopts="-g $localgroup -m 755"

for src in modo qmdo l10nrestore; do
    if [[ ! -f $prefix/sbin/$src || $src -nt $prefix/sbin/$src ]]; then
        echo $src -\> $prefix/sbin
        sudo install $instopts $src $prefix/sbin
    fi
done

if [[ ! -f $prefix/bin/podo || podo -nt $/prefix/bin/podo ]]; then
    echo podo -\> $prefix/bin
    sudo install $instopts podo $prefix/bin
fi
