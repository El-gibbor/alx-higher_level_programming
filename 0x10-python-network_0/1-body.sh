#!/bin/bash
# curl a URL and displays the body of the response for 200 status code
curl "$1" -sL

# if [ "$(curl -sL "$1" -w '%{http_code}\n')" == "200" ]; then curl -sL "$1"; fi
