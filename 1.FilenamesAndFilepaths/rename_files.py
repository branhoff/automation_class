# importing os module 
import datetime
import os

def get_curr_month_name():
    """
    Pulls curren month as long form name i.e. "January"
    """
    today = datetime.date.today()
    curr_month = today.strftime("%B")
    return curr_month
  
# Function to rename multiple files 
def main(): 
  
    for filename in os.listdir("1.FilenamesAndFilepaths\\work_files"):
        print(filename)

    # Steps to think about:
    # We can iterate through a list of filenames, but we still need to change
    # the names of the "filename" variable. We should remember that strings are immutable
    # so we can just tell python to cut out the "October" in the filename and replace it with November.
    # 1. Need to conver the "filename" into something that is mutable i.e. a list
    # 2. Change the part of the mutable that represents "October" to "November"
    # 3. Convert that mutable back to a normal string like before, but now with the correct name
    # 4. Change the current actual name of the file to our new name


# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 