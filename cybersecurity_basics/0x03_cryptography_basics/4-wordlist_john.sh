#!/bin/bash
john --wordlist=~/Downloads/rockyou.txt --format=lm "$1" && john --show --format=lm "$1" | grep ':' | cut -d: -f2- > 4-password.txt

