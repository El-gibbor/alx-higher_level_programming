#!/usr/bin/env bash
# displays the size of the body of the response from a URL request
# "man curl" to learn more about the used flags to curl

curl -so /dev/null "$1" -w "%{size_download}\n"