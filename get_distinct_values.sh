#!/usr/bin/bash

field_position=$1
filename=$2

DEFAULT_SEPARATOR=","

tail -n +2 ${filename} | cut -d${DEFAULT_SEPARATOR} -f${field_position} | sort | uniq
