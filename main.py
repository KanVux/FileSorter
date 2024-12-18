import os
import shutil

TARGET_DIR = r"C:\Users\hak68\Downloads"

default_file_struct = {
    "Images": ["png", "jpg", "jpeg", "webp", "gif"],
    "Documents": {
        "Word": ["doc", "docx"],
        "PDFs": ["pdf"],
        "Txt": ["txt"],
        "Excel": ["xls", "xlsx"],
        "PowerPoint": ["ppt", "pptx"],
    },
    "Scripts": {
        "Python": ["py", "ipynb"],
        "C": "c",
        "C++": "cpp",
        "Java": ["jar", "java"],
        "Websites": ["php", "css", "html"]
    },
    "Videos": ["mp4", "avi", "mkv", "mov", "wmv"],
    "Archives": ["zip", "7zip", "rar", "tar", "gz"],
    "Others": []
}

file_struct = default_file_struct
def add_file_struct():
    global file_struct
    input_name = input("Enter your directory name (press Enter without text or type \"exit\" to cancel): ")
    if not os.path.isdir(os.path.join(TARGET_DIR, input_name)):
        print(f"Created \"{input_name}\" directory")
    else:
        print("Directory existed! Please choose a diffent name!")
        return
    if not input_name or input_name == "exit":
        return
    
    input_folder_creation = input(f"Do you want to create a subdirectory for \"{input_name}\"? (Y/N) (Default = No): ")
    if not input_folder_creation or input_folder_creation == "N":
        file_struct[input_name] = []

          
        input_types = set(input(f"Enter your file types for \"{input_name}\" (seperate by a comma (,)): ")
                                    .replace(" ", "").split(','))
        for type in input_types:
            if type not in get_all_type(file_struct):
                if type != "":
                    print(type) # only add new type of file
                    print(f"Added type \"{type}\"")
                else: print("Type cannot be empty")
            else:
                print(f"\"{type}\" type had already exists")
                   



def get_extenstion(file=""):
    extension = os.path.splitext(file)[1].split('.')[-1]
    return extension

def check_file_type(extension, file_struct):
    for category, types in file_struct.items():
        if isinstance(types, dict):
            for subcategory, subtypes in types.items():
                if extension in subtypes:
                    return f"{category}/{subcategory}"
        elif isinstance(types, list):
            if extension in types:
                return category
    return "Others"

def create_dir(target_dir, file_struct):
    for dir in file_struct:
        if not os.path.isdir(os.path.join(target_dir, dir)):
            os.mkdir(os.path.join(target_dir, dir))
            print(f"Create Folder \"{dir}\" Successfully!")
        else:
            print(f"Directory \"{dir}\" already exists!")

    for key, value in file_struct.items():
        if isinstance(value, dict):
            for folder in value.items():
                subfolder = f"{key}/{folder[0]}"
                if not os.path.isdir(os.path.join(target_dir, subfolder)):
                    os.mkdir(os.path.join(target_dir, subfolder))            
                    print(f"Create Folder \"{subfolder}\" Successfully!")
                else: print(f"Subdirectory \"{subfolder}\" already exists!")


def sort_file(target_dir, file_struct):
    for file in os.listdir(target_dir):
        if file not in list(file_struct.keys()):
            destination_dir = os.path.join(target_dir, check_file_type(get_extenstion(file), file_struct))
            source_dir = os.path.join(target_dir, file)
            if os.path.isdir(destination_dir):
                shutil.move(source_dir, destination_dir)
                print("File Sorted!!")
            else: 
                print("Error!!!")
def get_all_type(file_struct, types=[]):
    if isinstance(file_struct, dict):
        for value in file_struct.values():
            get_all_type(value,types)
    elif isinstance(file_struct, list):
        for type in file_struct:
            types.append(type)  
    else: 
        types.append(file_struct)  
    return types
   
# print(get_all_type(file_struct))
add_file_struct()
# def main():
#     create_dir(TARGET_DIR, file_struct)
#     sort_file(TARGET_DIR, file_struct)


# if __name__ == "__main__":
#     main()
