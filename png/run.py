import os
import time
from concurrent.futures import ThreadPoolExecutor, as_completed  # 将as_completed也从模块中导入
from PIL import Image, PngImagePlugin
import os

def add_metadata_to_png(file_path):
    with Image.open(file_path) as img:
        metadata = PngImagePlugin.PngInfo()
        metadata.add_text('Copyright', 'Copyright © YourName 2023')
        img.save(file_path, pnginfo=metadata)

    print(f"Processed {file_path}")

def main():
    start_time = time.time()

    png_files = [f for f in os.listdir('.') if f.endswith('.png')]
    total_files = len(png_files)


    with ThreadPoolExecutor(max_workers=os.cpu_count()) as executor: 
        futures = {executor.submit(add_metadata_to_png, file): file for file in png_files}
        for future in as_completed(futures):  
            file_path = futures[future]
            try:
                future.result()
            except Exception as exc:
                print(f'{file_path} generated an exception: {exc}')

    end_time = time.time()
    print(f"\nProcessed {total_files} PNG files in {end_time - start_time:.2f} seconds.")

if __name__ == "__main__":
    main()
    