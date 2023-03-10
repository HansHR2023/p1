#!/usr/bin/env bash

projectName="medisch_centrum_randstad"

function refreshDB {
    echo "Remove current DB"
    rm db.sqlite3

    echo "Retrieve data from website"
    curl https://mc-randstad.netlify.app/data.csv | sed s/\;/,/g > "${projectName}/data/data.csv"

    ./migrate.sh

}

refreshDB