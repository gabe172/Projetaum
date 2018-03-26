#!/bin/bash

iptables -A FORWARD -p icmp -j REJECT
iptables -A INPUT -p icmp -j REJECT
iptables -A OUTPUT -p icmp -j REJECT
