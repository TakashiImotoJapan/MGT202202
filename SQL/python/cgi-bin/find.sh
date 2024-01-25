#!/bin/bash

if [[ -f /tmp/$1 ]]; then
  exit 0
else
  exit 1
fi
