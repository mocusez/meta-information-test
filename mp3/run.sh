#!/bin/bash
ffmpeg_command="ffmpeg -i {} -metadata title='歌曲标题' -metadata artist='艺术家名字' -metadata album='专辑名称' -c copy {}_with_meta.mp3"

time find . -type f -name "*.mp3" | xargs -I {} -P 32 bash -c "$ffmpeg_command"

echo "All MP3 files processed."