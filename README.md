# RecruitmentTask

A python script made for recruitment task, 
the task requirements are listed in requirements.md
All The dataset required for this script  is located at /data sub folder.
The test data is located at /testdata sub folder. 


### Requirements 

- Python 3.10 or higher
- Third-party libraries: 
    - sqlite3
    - argparse
    - pytest
## Usage
Run the script from the shell (project directory as a working directory). 

If you want to run the tests:  
 - Create virtual environment 
```bash
  python -m venv venv
```
 - Activate virtual environment
```bash
  source ./venv/bin/activate
```
- install requirements 
```bash
  pip install -r requirements.txt
```

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

##
If you want to only create database, you run this command:   
```bash
 python script.py create_database
```
In case you want to use the database pass the ``--use_database`` flag
### Example: 
```bash
 python script.py --use_database print-children --login zeverett@example.org --password n@8AymNdC*
```

## To do
- tests (done; might add more, more complex; setup workflow testing )
- comments and code refactor (not everywhere)
- sqlite3 database integration (done)

## Miscellaneous 
__For possible further project development__:
 - make it as a REST web app where you can add/edit/delete users

## Contact Information
Dawid Pawłowicz \
dpavlovisch.business@gmail.com