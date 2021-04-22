#!/bin/bash

polo(){
    if [[ -n $last_path ]] 
    then
        cd $last_path
    else
    echo "marco is not called yet"
    fi
}
