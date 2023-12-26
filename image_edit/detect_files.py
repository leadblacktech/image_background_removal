import os 
import time 

folder_path = 'image'
state_file = "folder_state.txt"
check_interval = 30 

while True: 
    if os.listdir(folder_path):
        with open(state_file, 'w') as file:
            file.write('foundFiles=True') 
            print('Folder is not empty')
        break
    else:
        with open(state_file, 'w') as file:
            file.write('foundFiles=False') 
            print('Folder is empty')
            time.sleep(check_interval)
        continue