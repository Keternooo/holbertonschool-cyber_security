#!/bin/bash
echo -n Geeks For Geeks | sha1sum | awk '{ print $1 }' > 0_hash.txt
