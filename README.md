# RecruitmentTask

A python script made for recruitment task. 
All The dataset required for this script  is located at /data subfolder.


### Requirements 

- Python 3.10 or higher
- Third-party libraries: 
    - sqlite3
    - argparse
## Usage
Run the script from the shell (project directory as a working directory). 

Here are the example of commands to execute different actions. 

### Commands:
- **python script.py print-all-accounts --login <login> --password <password>**
- **python script.py print-oldest-account --login <login> --password <password>**
- **python script.py group-by-age --login <login> --password <password>**
- **python script.py print-children --login <login> --password <password>**
- **python script.py find-similar-children-by-age --login <login> --password <password>**

### Examples: 
    # Print the number of all valid accounts
    python script.py print-all-accounts --login 555123456 --password sASfC1234

    # Print information about the oldest account
    python script.py print-oldest-account --login 555123456 --password sASfC1234

    #Print all and group children by age
    python script.py group-by-age --login 555123456 --password sASfC1234

    # Display information about the user's children
    python script.py print-children --login 555123456 --password sASfC1234

    # Find users with similar children by age
    python script.py find-similar-children-by-age --login 555123456 --password sASfC1234

## To do
- tests
- comments and code refactor
- sqlite3 database integration (done)

## Contact Information
Dawid Pawłowicz \
dpavlovisch.business@gmail.com