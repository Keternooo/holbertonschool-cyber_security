#!/bin/bash
john --wordlist=~/Downloads/rockyou.txt --format=raw-sha256 "$1" && john --show --format=raw-sha256 "$1" | grep ':' | cut -d: -f2- > 6-password.txt
