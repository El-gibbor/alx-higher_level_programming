#!/bin/bash
# sends a POST request with parameters to a URL with
curl -s POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
