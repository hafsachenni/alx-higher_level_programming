#!/bin/bash
# Bash script that sends a request and dispaly only status code
curl -s -o /dev/null -w "%{http_code}" "$1"
