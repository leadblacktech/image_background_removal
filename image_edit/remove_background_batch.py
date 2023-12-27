from rembg import remove
import glob
import os
import time

def process_files():
    files = glob.glob('image/*.JPG')
    for file in files:
        input_path = file
        output_path = input_path.replace("image/", "results/")

        with open(input_path, 'rb') as i:
            with open(output_path, 'wb') as o:
                original_image = i.read()
                output = remove(original_image)
                o.write(output)
        os.remove(input_path)  # Optionally remove the processed file

folder_path = 'image'
state_file = "folder_state.txt"
check_interval = 30

while True:
    if os.listdir(folder_path):
        with open(state_file, 'w') as file:
            file.write('foundFiles=True')
            print('Folder is not empty')
        process_files()  # Process the files function
    else:
        with open(state_file, 'w') as file:
            file.write('foundFiles=False')
            print('Folder is empty')

    time.sleep(check_interval)
    
############################################################################


