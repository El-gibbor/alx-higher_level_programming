#!/bin/bash
# sends a POST request with parameters to a URL with
curl -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
