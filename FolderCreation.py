import os

def folderCreation(soNumber, packageType, abreviation ):
    # Get the path to the desktop
    packageFolder = os.path.join(os.path.join(os.environ['USERPROFILE']), 'PackageCompile')

    if packageType.lower() == "tank":
        header = "TA"
    elif packageType.lower() == "ua":
        header = "UA"
    elif packageType.lower() == "clamp":
        header = "CLAMP"

    # Define the name of the new folder
    folder_name = 'SO' + soNumber + '-' + packageType.upper()
    list_folder_name = 'SO' + soNumber + '-' + header + '-' + abreviation + '-PDF-DXF'

    # Create the new folder
    new_folder_path = os.path.join(packageFolder, folder_name)
    list_folder_path = os.path.join(new_folder_path, list_folder_name)

    # Print the path for debugging
    print(f"Package folder path: {new_folder_path}")

    # Check if the folder already exists
    if not os.path.exists(new_folder_path):
        os.makedirs(new_folder_path) 

    if not os.path.exists(list_folder_path):
        os.makedirs(list_folder_path)


    return list_folder_path, new_folder_path