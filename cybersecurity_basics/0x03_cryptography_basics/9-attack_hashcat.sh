#!/bin/bash
hashcat -a 1 "$1" wordlist1.txt wordlist2.txt -m 0 && hashcat "$1" --show -m 0 | cut -d: -f2- > 9-password.txt
