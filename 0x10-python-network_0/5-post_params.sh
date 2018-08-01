#!/bin/bash
#variable email must be send with val, subj with val using curl
curl $1 -s -X POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD"
