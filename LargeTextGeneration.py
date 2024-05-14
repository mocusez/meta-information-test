def generate_text_file(file_name, target_size_mb=100):
    target_size = target_size_mb * 1024 * 1024
    base_string = "Hello, World!"
    content = ""
    
    while len(content.encode('utf-8')) < target_size:
        content += base_string

    with open(file_name, 'w') as file:
        file.write(content[:target_size])
        
    print(f"Generated text file '{file_name}' with size approximately {target_size_mb} MB.")

generate_text_file("100M.txt")