time find . -type f -name "*.jpg" | xargs -n 1 -P 32 exiftool -overwrite_original -Copyright="Copyright © YourName 2023" -Make="New Manufacturer" -Model="New Model" -Title="AI Made" -Subject="AI Made DDG" -Author="Diffussion"