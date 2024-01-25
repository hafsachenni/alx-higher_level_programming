#!/bin/bash
#sends a json post request
curl -sX POST -H "Content-Type: hafsa/json" -d @"$2" "$1"
