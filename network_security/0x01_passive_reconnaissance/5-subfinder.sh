#!/bin/bash

subfinder -silent -d $1
subfinder -silent -d "$1" -nW -oI | awk -F',' '{ if (NF >= 2) { print $1","$2 } else { print } }' > "$1.txt"
