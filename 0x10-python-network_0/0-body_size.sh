#!/bin/bash
# displays the body size of the response from a URL request
curl -w "%{size_download}""\n" -o /dev/null -s "$1"