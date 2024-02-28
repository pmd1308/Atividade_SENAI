#!/bin/bash
for dir in */; do
    cd "$dir"
    git init
    cd ..
done