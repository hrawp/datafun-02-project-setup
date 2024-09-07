


''' This module provides functions for creating a series of project folders. 
There are 5 functions featured in the project.  
Function 4 uses a iterative wait time increase one second each time the while loops runs.
Function 5 is interactive how the path is created with as is, underscores for spaces, lowercase, or both options applied.
'''

#####################################
# Import Modules at the Top
#####################################

# Import moduldes from standand library

from pathlib import Path
import pathlib
import time

# Import local modules
import hrawp_utils

#####################################
# Declare global variables
#####################################

# Create a project path object
project_path = pathlib.Path.cwd()

# Create lists
folder_names = ['data-csv', 'data-excel', 'data-json']
folder_namesshr = ['csv', 'excel', 'json']

#List of Regions
regions = [
    "North America", 
    "South America", 
    "Europe", 
    "Asia", 
    "Africa", 
    "Oceania", 
    "Middle East"
    ]

#A stirng to pass in as a prefix for function 3
prefix = '3data-'

#Variables for function 4 and the amount of time we should delay the creation of folders
duration_secs:int = 3  # duration in seconds

#Variables for function 5 and choosing how show the regions list's format with either lower case, underline instead of spaces, both of these or none of these.
lower = 1
underline = 1
lowinput = None
undinput = None

#####################################
# Define Function 1. For item in Range: Create  folders for a given range (e.g., years).
# Pass in an int for the first year
# Pass in an int for the last year
#####################################

def create_folders_for_range(start_year: int, end_year: int) -> None:

    for year in range(start_year, end_year + 1):
        folder_name = f"{project_path}/{year}"
        Path(folder_name).mkdir(parents=True, exist_ok=True)
        print(f"Created directory: {folder_name}")
        time.sleep(1)
    
  
#####################################
# Define Function Function 2. For Item in List: Develop a function to create folders from a list of names.
# Pass in a list of folder names 
#####################################

def create_folders_from_list(folder_names: list) -> None:
 
    for list in folder_names:
        folder_name = f"{project_path}/{list}"
        Path(folder_name).mkdir(parents=True, exist_ok=True)
        print(f"Created directory: {folder_name}")
        time.sleep(1)

#####################################
# Function 3 is a function to create prefixed folders by 
# transforming a list of names and combining each with a prefix.
# Pass in a list of folder names
# Pass in a prefix ('3data-') to add to each
#####################################

def create_prefixed_folders(folder_list: list, prefix: str) -> None:
   
   for list in folder_list:
        folder_name = f"{project_path}/{prefix}{list}"
        Path(folder_name).mkdir(parents=True, exist_ok=True)
        print(f"Created directory: {folder_name}")
        time.sleep(1)
  

#####################################
# Define Function 4. This functions is to create folders periodically 
# starting at 3 seconds and incrmenting until a break.
# Pass in the wait time in seconds.
# It is intend to use the variable and incrment it up every while loop interation
# so its a variable chaning the wait time and also ending the while loop.
#####################################

def create_folders_periodically(duration_seconds: int) -> None:
   
    while True :
        folder_name = f"{project_path}/WhileLoop{duration_seconds}"
        Path(folder_name).mkdir(parents=True, exist_ok=True)
        print(f"Created directory: {folder_name}")
        duration_seconds += 1
        time.sleep(duration_seconds)
        if duration_seconds > 7:
            break

#####################################
# Function 5. For Item in List: Create folders from a list of names.  Choose to either have each folder name in the list 
# as lower case and undersocres instead of space, just lower case, just underscores, or as is from the list.
# Pass in a list of folder names as a list of regions.
#####################################

def create_folders_from_listr(regions: list,lower: int,underline: int,lowinput: str,undinput: str) -> None:
 
    for list in regions:
        lowinput = input("Press 1 then Enter if you want the folders output to be lowercasae. Else press Enter.")
        if lowinput is "1":
            lower = 1
        else:
            lower = 0
        undinput = input("Press 1 then Enter if you want the folders output to have underlines insted of spaces. Else press Enter.")
        if undinput is "1":
            underline = 1
        else:
            underline = 0
        if lower == 1 and underline == 0:
            folder_name = f"{project_path}/{list.lower()}"
        elif underline == 1 and lower == 0:
            folder_name = f"{project_path}/{list.replace(" ", "_")}"
        elif lower == 1 and underline == 1:
            folder_name = f"{project_path}/{list.lower().replace(" ", "_")}"
        else:
            folder_name = f"{project_path}/{list}"
        Path(folder_name).mkdir(parents=True, exist_ok=True)
        print(f"Created directory: {folder_name}")
        time.sleep(1)
  

#####################################
# Define a main() function for this module.
#####################################

def main() -> None:
    ''' Main function to demonstrate module capabilities. '''

    # Start of main execution
    print("#####################################")
    print("# Starting execution of main()")
    print("#####################################\n")

    # Print get_byline() from imported module
    print(f"Byline: {hrawp_utils.get_byline()}")

    # Call function 1 to create folders for a range (e.g. years)
    create_folders_for_range(start_year=2020, end_year=2023)

    # Call function 2 to create folders given a list
    create_folders_from_list(folder_names)

    # Call function 3 to create folders using comprehension
    create_prefixed_folders(folder_namesshr, prefix)

    # Call function 4 to create folders periodically using while
    create_folders_periodically(duration_secs)

    # Call function 5 to process regions file and set to lowercase and uppercase
    create_folders_from_listr(regions, lower, underline, lowinput, undinput)

    # End of main execution
    print("\n#####################################")
    print("# Completed execution of main()")
    print("#####################################")


#####################################
# Conditional Execution
#####################################

if __name__ == '__main__':
    main()
