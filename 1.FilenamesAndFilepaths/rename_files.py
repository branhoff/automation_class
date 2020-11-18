# import modules we'll need
import datetime
import os

def get_curr_month_name():
    """
    Pulls current month as long form name i.e. "January"
    """
    today = datetime.date.today()
    curr_month = today.strftime("%B")
    return curr_month
  
# Function to rename multiple files 
def main(): 
  
    for filename in os.listdir("1.FilenamesAndFilepaths\\work_files"):
        print(filename)

    # What we have:
    # We can currently iterate through a list of filenames, but we still need to change
    # the names of the "filename" variable. We should remember that strings are immutable
    # so we can't just tell python to cut out the "October" in the filename and replace it with November.

    # REMEMBER YOU CAN GOOGLE
    
    # Steps to think about:
    # 1. Need to convert the "filename" into something that is mutable (an object that can be changed) i.e. a list
    # 2. Change the part of the mutable that represents "October" to "November"
    # 3. Convert that mutable back to a normal string like before, but now with the correct name
    # 4. Change the current ACTUAL name of the file to our new name

    # TRY GOOGLING "how to change string to list in python"
    #              "how to create new folder in python"
    #              "how to copy files in python"
    #              "how to rename files in python"


# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 