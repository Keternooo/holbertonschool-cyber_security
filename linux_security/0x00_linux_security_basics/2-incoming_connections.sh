#!/bin/bash

iptables -A INPUT -p tcp --dport 80 -J ACCEPT
