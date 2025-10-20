#!/bin/bash
john --wordlist=~/Downloads/rockyou.txt --format=nt "$1" && john --show --format=nt "$1" | grep ':' | cut -d: -f2- > 5-password.txt
