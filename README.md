
This script was created to search for Pacemaker transition files in the current directory.

The script is searching for files starting with "pe-input" and end with ".bz2".
The files will be sorted on natural basis and a Python list will be created.
The elements of the list wil be used to execute "crm_simulate -x <element>" and the status
of the Pacemaker cluster will be shown in a formatted output in the console.



https://github.com/amach4/pacemaker/assets/23736066/8d925f8e-b521-4fdf-86dc-3b03f9742d4a

