import os
import shutil

def create(path: str, extension: str) -> str:
    folder_name: str = extension[1:]
    folder_path: str = os.path.join(path, folder_name)
    
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        
    return folder_path

def sort_files(source_path: str):
    for root_dir, sub_dir, filenames in os.walk(source_path):
        for filename in filenames:
            file_path: str = os.path.join(root_dir, filename)
            extension: str = os.path.splitext(filename)[1]
            
            if extension:
                target_folder: str = create(source_path, extension)
                target_path: str = os.path.join(target_folder, filename)
                
                shutil.move(file_path, target_path)
                
        
def remove_empty_folders(source_path: str):
    for root_dir, sub_dir, filenames in os.walk(source_path, topdown=False):
        for current_dir in sub_dir:
            folder_path: str = os.path.join(root_dir, current_dir)
            
            if not os.listdir(folder_path):
                os.rmdir(folder_path)

def main():
    user_input: str = input('Provide a filepath to sort: ')
    
    if os.path.exists(path=user_input):
        sort_files(user_input)
        remove_empty_folders(user_input)
        print('Your files have been Sorted!')
    else:
        print('Invalid path, please provide a valid file path')


if __name__ == '__main__':
    main()




