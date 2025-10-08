#!/bin/bash 
whois "$1" | grep -E "Registrant|Admin|Tech"| grep -v "If you wish to contact"| sed 's/: /,/g' > "$1".csv
