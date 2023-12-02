#!/bin/bash
# displays the body size of the response from a URL request
curl -o /dev/null -s "$1" -w "%{size_download}"\n"