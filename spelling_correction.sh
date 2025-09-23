#!/bin/bash

# From page 40, section 2.1, in Scripting, by Michael Kofler, 2024, Rheinwerk.

sedcmd=""

while read -r findtxt replacetxt; do
    sedcmd+="s/$findtxt/$replacetxt/g;"
done < /Users/jhachtel/Projects/reference-scripts/config/spelling_corrections.txt

for filename in $*; do
    echo "Correct file $filename"
    sed -i.bak "$sedcmd" $filename
done
