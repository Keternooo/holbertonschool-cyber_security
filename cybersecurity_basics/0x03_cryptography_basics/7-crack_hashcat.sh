#!/bin/bash
hashcat "$1" ~/Downloads/rockyou.txt -m 0 && hashcat "$1" --show -m 0 | cut -d: -f2- > 7-password.txt
