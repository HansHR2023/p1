#!/usr/bin/env bash

port=8080
start_page=1
url="http://localhost:8080/medish_centrum_randstad/api/netlify?page=${start_page}"
 
source ./browse.sh ${url} 5 &

printf "Start django application at %s\n" ${url}
python medisch_centrum_randstad/manage.py runserver 0.0.0.0:${port}
