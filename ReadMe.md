# Meta Information Writing/Reading Test
read and write meta Information under Ubuntu
## Prerequisite
jpg/mov/mp3/mp4 test need
```markdown
apt install ffmpeg exiftool
```
png test need
```markdown
pip install pillow
```

## Test file basic information
```markdown
1.jpg 385KB
1.mov 19058KB
1.mp3 57KB
1.mp4 35719KB
1.png 508KB
```

## How to use
Before you to start use, you should change the **file number** and **Process number**

Example:
```bash
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
```
Change the file number 10000 to you want
```bash
time find . -type f -name "*.jpg" -print0 | xargs -0 -n 1 -P 16 exiftool -
```
Change the process number 16 to you want(you can reference the number of nproc)

The bash script use **time** command
The python use **time** module

## Test Result 
### 1
CPU：11th Gen Intel(R) Core(TM) i9-11900K @ 3.50GHz（8cores 16threads）

Memory: 57GB

Hardware: 
Write——162MB/s
Read——173MB/s

**Each folder have 100 file**

#### Write
|  | jpg | mov | mp3 | mp4 | mp4 |
| --- | --- | --- | --- | --- | --- |
| real | 0m6.252s | 0m2.416s | 0m1.144s | 0m2.923s | 0m3.73s |
| user | 1m26.431s | 0m20.929s | 0m10.399s | 0m22.209s |  |
| sys | 0m6.768s | 0m14.029s | 0m5.973s | 0m20.593s |  |


### 2
CPU：13th Gen Intel(R) Core(TM) i9-13900K @ 3.50GHz（16cores 32threads）

Memory: 64GB

Hardware: Samsung SSD 980 PRO 1TB

Write——3.4GB/s

Read——6.7GB/s

**Each folder have 10000 file**

#### Software Version
| ffmpeg | 4.2.7 |
| --- | --- |
| exiftool | 11.88 |
| Pillow | 5.1.0 |


#### Write
|  | jpg | mov | mp3 | mp4 | mp4 |
| --- | --- | --- | --- | --- | --- |
| real | 1m46.472s | 1m47.662s | 0m15.132s | 4m16.822s | 1m6.22s |
| user | 45m8.066s | 10m14.761s | 4m8.562s | 9m55.467s |  |
| sys | 4m36.100s | 16m9.223s | 2m16.391s | 23m12.517s |  |


#### Read
|  | jpg | mov | mp3 | mp4 | mp4 |
| --- | --- | --- | --- | --- | --- |
| real | 0m29.699s | 0m25.083s | 0m14.574s | 0m23.209s | 0m0.88s |
| user | 11m50.016s | 7m5.895s | 4m1.597s | 5m59.756s |  |
| sys | 1m19.797s | 3m54.465s | 2m15.412s | 4m31.707s |  |

