#!/bin/bash
john --wordlist=~/Downloads/rockyou.txt --format=raw-md5 "$1" && john --show --format=raw-md5 "$1" | grep ':' | cut -d: -f2- > 4-password.txt
