To run this locally:

1. Clone the project
2. Open the terminal and navigate to the parent folder of your virtual environment
3. Activate your virtual environment with the command:

      source venv/bin/activate
 
      *you will know this works as you will see (venv) at the start of your command line*

4. Navigate to the source folder within the F20EC_Website folder
5. Make migrations using the command:

      python source/manage.py migrate

6. Run the website using the command:

      python source/manage.py runserver

