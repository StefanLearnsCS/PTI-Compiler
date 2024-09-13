import os

def folderCreation(soNumber, packageType):
    # Get the path to the desktop
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'PackageCompile')

    # Define the name of the new folder
    folder_name = 'SO' + soNumber + '-' + packageType

    # Create the new folder
    new_folder_path = os.path.join(desktop, folder_name)

    # Print the path for debugging
    print(f"Package folder path: {new_folder_path}")

    # Check if the folder already exists
    if not os.path.exists(new_folder_path):
        os.makedirs(new_folder_path)
        print(f"Folder '{folder_name}' created at: {new_folder_path}")
    else:
        print(f"Folder '{folder_name}' already exists at: {new_folder_path}")

folderCreation('20216', 'Tank')