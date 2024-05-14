#!/bin/bash
ffmpeg_command="ffmpeg -i {} -metadata AUTHOR='YourName' -codec copy {}_with_meta.mov"

time find . -type f -name "*.mov" | xargs -I {} -P 32 bash -c "$ffmpeg_command"

echo "All MOV files processed."