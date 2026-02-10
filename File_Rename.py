import os

def rename_file(folder, file_format):
    """
    Renames files in the given folder that contain the specified file_format.
    Files are renamed sequentially starting from 0.
    
    Parameters:
    folder (str): Path to the target folder
    file_format (str): Substring or extension to filter files (e.g., '.txt')
    """
    try:
        # Change the working directory to the target folder
        os.chdir(folder)
        
        # Get the list of all files in the folder
        file_list = os.listdir(".")
        
        # Counter for renamed files
        n = 0
        
        # Iterate through each file in the folder
        for file in file_list:
            # Check if the file contains the specified format
            if file_format in file:
                # Rename the file to a sequential number + file_format
                os.rename(file, f"{n}{file_format}")
                print(f"Renamed: {file} → {n}{file_format}")  # Beautified output
                n += 1
                
        # If no files were renamed, notify the user
        if n == 0:
            print(f"No files found with format '{file_format}' in {folder}.")
        else:
            print(f"\n✅ Successfully renamed {n} files in '{folder}'.")
    
    except Exception as e:
        # Handle errors gracefully
        print(f"❌ Error: {e}")

rename_file("data", ".txt")