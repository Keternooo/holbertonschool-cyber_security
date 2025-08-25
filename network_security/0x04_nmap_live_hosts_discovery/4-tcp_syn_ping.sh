#!/bin/bash
sudo nmap -sn -p U:22,80,443 -PS $1
