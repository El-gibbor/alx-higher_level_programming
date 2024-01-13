#!/usr/bin/node
// writes a string to a file. string and file are passed via cl

const { argv } = require("process")
const fs = require("fs")

fs.writeFile(argv[2], argv[3], "utf-8", (err) => {
    if (err){
        console.error(err)
    }
})
