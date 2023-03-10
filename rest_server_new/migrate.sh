#!/usr/bin/env bash

projectName="medisch_centrum_randstad"

cd ${projectName}

echo "Remove current DB"
rm db.sqlite3

echo "Make migrations"
python manage.py makemigrations

echo "Migrate the built-in user model"
python manage.py migrate

echo "Import data"
python manage.py load_data