"File copying example"

try:
    with open('bronx.jpg', 'rb') as rf:
        with open("bronx_copy.jpg", "wb") as wf:
            chunk_size = 4096  # 4KB
            rf_chunk = rf.read(chunk_size)
            while rf_chunk:
                wf.write(rf_chunk)
                rf_chunk = rf.read(chunk_size)
    print("File copied successfully.")
except PermissionError:
    print("Permission denied: You do not have permission to read or write to the file.")
except FileNotFoundError:
    print("The file 'bronx.jpg' does not exist. Please check the file path.")
except IOError as e:
    print(f"An I/O error occurred: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
