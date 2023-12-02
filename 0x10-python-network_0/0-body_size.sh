#!/bin/bash
# displays the size of the body of the response from a URL request
curl -so /dev/null "$1" -w "%{size_download}\n"