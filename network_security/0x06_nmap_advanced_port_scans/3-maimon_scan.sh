#!/bin/bash
sudo nmap -sM -p ftp,ssh,telnet,http,https -vv --reason "$1"
