# step 0
import sqlite3

import queries as q

# STEP 1
# Connect to the database
#triple check the spelling of your database filename

connection = sqlite3.connect('rpg_db.sqlite3')

# STEP 2 "Make the cursor"

cursor = connection.cursor()

# step 3 - "Write the Query"

#"query = 'SELECT character_id, name FROM charactercreator_character;'"
#query is moved to the queries.py file

# step 4 - Execute the query and pull the results

# cursor.execute(query)
# results = cursor.fetchall()

results = cursor.execute(q.SELECT_ALL).fetchall()

if __name__ == '__main__':
    print(results[:5])
