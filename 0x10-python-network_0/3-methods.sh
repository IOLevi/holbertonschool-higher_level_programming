#!/bin/bash
# grep for allow header -- all http methods 
curl -sI $1 | grep -i "Allow:" | cut -d" " -f2-
