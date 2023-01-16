#!/bin/bash
echo "input file name"
read file_name
echo "#!/usr/bin/python3" > $file_name.py
chmod +x $file_name.py
vi $file_name.py
