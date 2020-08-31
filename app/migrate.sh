#!/bin/bash
if [ ! -e $1 ]; then
    echo "-- First container startup --"
    python3 manage.py db init
    python3 manage.py db migrate
    python3 manage.py db upgrade

    touch $1
else
    echo "-- Not first container startup --"
fi
