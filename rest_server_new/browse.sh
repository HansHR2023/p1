#!/usr/bin/env bash

argument_names=("url", "sleep_interval")
argument_values=("$@")
nr_of_arguments=${#argument_values[@]}

if [ $nr_of_arguments -lt ${#argument_names[@]} ]; then
    printf "USAGE: source navigate.sh %s\n" "${argument_names[*]}"
    exit 1;
fi  

sleep_interval="${argument_values[1]}"
url="${argument_values[0]}"

sleep ${sleep_interval}
python -m webbrowser -t ${url} 
