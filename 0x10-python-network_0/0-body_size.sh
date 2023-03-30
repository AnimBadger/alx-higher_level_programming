#!/usr/bin/env bash
# script that sends request to URL and display size in byte

curl -s "$1" | wc -c