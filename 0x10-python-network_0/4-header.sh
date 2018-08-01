#!/bin/bash
# takes url as arg, sends a get req, displays body of resp
curl $1 -s -H "X-HolbertonSchool-User-Id: 98"
