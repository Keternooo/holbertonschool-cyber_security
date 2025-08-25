#!/bin/bash
nmap -p U:22,80,443 -PS $1
