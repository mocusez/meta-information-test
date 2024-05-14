ffmpeg_command="ffprobe {} "
last="mp3"

time find . -type f -name "*_with_meta.${last}" | xargs -I {} -P 32 bash -c "$ffmpeg_command"

echo "All ${last} files processed."