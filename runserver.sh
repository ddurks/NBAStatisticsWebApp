#!/usr/bin/env bash

while true; do
  echo "Re-starting Django runserver"
  python manage.py runserver 0.0.0.0:8080
  sleep 4
done
