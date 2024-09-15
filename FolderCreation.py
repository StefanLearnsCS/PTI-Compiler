import os

def folderCreation(soNumber, packageType):
    # Get the path to the desktop
    packageFolder = os.path.join(os.path.join(os.environ['USERPROFILE']), 'PackageCompile')

    # Define the name of the new folder
    folder_name = 'SO' + soNumber + '-' + packageType
    ss_folder_name = 'SO' + soNumber + '-SS-PDF-DXF'
    pp_folder_name = 'SO' + soNumber + '-PP-PDF-DXF'

    # Create the new folder
    new_folder_path = os.path.join(packageFolder, folder_name)
    SS_folder_path = os.path.join(new_folder_path, ss_folder_name)
    PP_folder_path = os.path.join(new_folder_path, pp_folder_name)

    # Print the path for debugging
    print(f"Package folder path: {new_folder_path}")

    # Check if the folder already exists
    if not os.path.exists(new_folder_path):
        os.makedirs(new_folder_path)
        os.makedirs(SS_folder_path)
        os.makedirs(PP_folder_path)
        print(f"Folder '{folder_name}' created at: {new_folder_path}")
    else:
        print(f"Folder '{folder_name}' already exists at: {new_folder_path}")

    return SS_folder_path, PP_folder_path, new_folder_path