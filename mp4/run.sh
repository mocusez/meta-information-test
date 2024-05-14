#!/bin/bash
ffmpeg_command="ffmpeg -i {} -metadata comment='YourName' -codec copy {}_with_meta.mp4"

time find . -type f -name "*.mp4" | xargs -I {} -P 32 bash -c "$ffmpeg_command"

echo "All MP4 files processed."