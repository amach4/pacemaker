
This script was created to search for Pacemaker transition files in the current directory.

After you started the script you can Enter: **p** (previous) or **n** (next) or **c** (cancel) to open
the **p**revious or **n**ext file or **c**ancel the script execution.

The script is searching for files starting with "pe-input" and end with ".bz2".
The files will be sorted on natural basis and a Python list will be created.
The elements of the list wil be used to execute "crm_simulate -x <element>" and the status
of the Pacemaker cluster will be shown in a formatted output in the console.




https://github.com/amach4/pacemaker/assets/23736066/a06b1f64-d4c3-4600-bde0-62999e4d9224



