#!/bin/bash
if [ ! -e $1 ]; then
    echo "-- First container startup --"
    python manage.py db init
    python manage.py db migrate
    python manage.py db upgrade

    touch $1
else
    echo "-- Not first container startup --"
fi
