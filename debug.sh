#!/bin/bash
 
while true
do
    ./test.sh >> log 2>> log
    if [[ $? -ne 0 ]]
    then
        cat log
        break
    fi
done
