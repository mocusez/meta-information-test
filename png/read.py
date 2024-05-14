import os
import time
from concurrent.futures import ThreadPoolExecutor, as_completed 
from PIL import Image, PngImagePlugin
import os

def png(file_path):
    with Image.open(file_path) as img:
        # 获取PNG图像的元数据字典
        metadata = img.text
        # 打印元数据
        print("Metadata:")
        for key, value in metadata.items():
            print(f"{key}: {value}")
            

def main():
    start_time = time.time()

    png_files = [f for f in os.listdir('.') if f.endswith('.png')]
    total_files = len(png_files)


    with ThreadPoolExecutor(max_workers=os.cpu_count()) as executor: 
        futures = {executor.submit(png, file): file for file in png_files}
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
    