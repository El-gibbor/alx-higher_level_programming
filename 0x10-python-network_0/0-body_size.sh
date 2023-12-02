#!/bin/bash
# displays the size of the body of the response from a URL request
curl -o /dev/null -o "$1" -w "%{size_download}"\n"