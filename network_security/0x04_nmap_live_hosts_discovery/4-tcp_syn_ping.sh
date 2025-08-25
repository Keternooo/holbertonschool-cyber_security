#!/bin/bash
sudo nmap -p U:22,80,443 -PS $1
