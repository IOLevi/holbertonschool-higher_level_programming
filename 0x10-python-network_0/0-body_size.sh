#!/bin/bash
#send a request to url -- display size of the body of response 
curl -sI $1 | grep -i "Content-Length:" | cut -d" " -f2
