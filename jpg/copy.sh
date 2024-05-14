#!/bin/bash

source_image="1.jpg"
target_folder="."

if [ ! -d "$target_folder" ]; then
    mkdir "$target_folder"
fi

for ((i=2; i<=10000; i++)); do
    num=$(printf "%04d" $i)
    target_image="${target_folder}/${num}.jpg"
    cp "$source_image" "$target_image"
done

echo "Copy JPG Complete"