import os
import shutil
import time

def backupfiles():
    deleted_folder_count=0
    deleted_files_count=0

    path="/Users/asd/Desktop/root_folder"
    days=1
    seconds=time.time()-(days*24*60*60)
    if os.path.exists(path):
        for root_folder,folders,files in os.walk(path):
            if seconds>=get_file_or_folder_age(root_folder):
                remove_folder(root_folder)
                deleted_folder_count+=1
                break
            else :
                for folder in folders:
                    folder_path =os.path.join(root_folder,folders)
                    if seconds>=get_file_or_folder_age(folder_path):
                        remove_folder(folder_path)
                        deleted_folder_count+=1
                for  file in files:
                    file_path=os.path.join(root_folder,files)    
                    if seconds>=get_file_or_folder_age(file_path):
                        remove_file(file_path)
                        deleted_files_count+=1
    else :
        print(f'"{path}"is not found')
        deleted_files_count+=1
    print(f"total folder deleted: {deleted_folder_count}")     
    print(f"total files deleted: {deleted_files_count}")      

def remove_folder(path):
    if not shutil.rmtree(path):
        print(f"{path} is removed succesfully")
           
    else:
        print(f"{path} unable to removed..")
def remove_file(path):
    if not os.remove(path):
        print(f"{path} is removed succesfully")  
    else:
        print(f"{path} unable to removed..")   

def get_file_or_folder_age(path):
    ctime=os.stat(path).st_ctime
    return ctime
if __name__=="__main__":
    backupfiles()

