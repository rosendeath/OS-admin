#!/bin/bash

count=0

for file in /etc/*; do
    if [ -f "$file" ]; then
        count=$((count + 1))
    fi
done

echo "Counted files in /etc: $count"
