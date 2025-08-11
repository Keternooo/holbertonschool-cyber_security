#!/bin/bash

iptables -A INPUT -p tcp --dport 22 -J ACCEPT
iptables -P INPUT DROP
