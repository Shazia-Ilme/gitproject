
This file will be used for documentation purpose of python code.
Features and Description:

1 Database Setup:
    The script establishes a connection to a MySQL database server running locally.
    It drops the existing "yyes" database if it exists, creates a new "yyes" database, and selects it for use.
    It creates a table named "c19_vaccination" with columns: `sno`, `city`, `country`, `affected`, `vaccinated_1dose`, and `vaccinated_2dose`.

2.Menu-driven Interface:
    The script presents a menu-driven interface to the user, allowing them to choose from different options.

3.Add Details (Option 1):
   Users can add details of affected and vaccinated people to the database.
   It takes input for serial number, city, country, number of affected people, number vaccinated with the 1st dose, and number vaccinated with the 2nd dose.

4.Update Details (Option 2):
   Users can update specific details of records in the database.
   Options include updating city, country, affected count, 1st dose count, and 2nd dose count.

5.Display/Search Details (Option 3):
   Users can display all details or search for details of a specific city based on serial number.

6.Show Graphs (Option 4):
   Users can visualize graphs related to affected and vaccinated people.
   Graph options include affected people, 1st dose vaccinations, and 2nd dose vaccinations for a specific country.

7.Exit (Option 5):
   - Users can choose to exit the program.

Notable Points:

 The script uses the `mysql.connector` library for MySQL database interaction.
 It employs the `numpy` and `matplotlib.pyplot` libraries for data manipulation and graph plotting.
 SQL queries are used to interact with the MySQL database for operations such as insertion and updates.
 The script has a menu-driven interface with options to perform various actions.
 It handles database connections and cursor operations within each menu option.
 Basic input validation is performed using `int()` and `input()` functions.

Suggestions:

 The script could benefit from error handling to handle potential exceptions during database operations.
 A more robust menu system or a loop with an exit condition could be implemented for a smoother user experience.
 It's advisable to use parameterized queries to prevent SQL injection vulnerabilities.

This script provides a basic framework for a vaccination survey system, and you can enhance it further based on specific requirements.