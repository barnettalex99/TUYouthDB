# Queries for the TU YOUTH DATABASE
import sqlite3
import os

db = None


def main():
    global db
    try:
        dbname = 'youth_programs.db'
        if os.path.exists(dbname):  # does this database file exist?
            db = sqlite3.connect(dbname)  # connect to the database

            #query_total_locations()
            #query_one_location_by_num_programs()
            #query_participants_by_location()
            # query_locations_by_gender()

            db.close()  # close the database
        else:
            print('Error:', dbname, 'does not exist')

    except sqlite3.IntegrityError as err:
        print('Integrity Error:', err)
    except sqlite3.OperationalError as err:
        print('Operational Error:', err)
    except sqlite3.Error as err:
        print('Error:', err)


def query_total_locations():
    # Prompts for the state to list all the total locations with Youth Programs.
    # Continues prompting if the user enters no value.
    cursor = db.cursor()
    total_program_count = 0
    # Construct the query that incorporates the user's selection, and display formatted results.
    state_sql = "SELECT DISTINCT Location FROM Participants "
    print(state_sql)
    cursor.execute(state_sql)
    records = cursor.fetchall()
    for recs in records:
        total_program_count = total_program_count + 1
    print(' Total Locations Used: ' + str(total_program_count))
    for rec in records:
        print(rec)


def query_one_location_by_num_programs():
    # Prompts for the state to list all the National Parks in this state.
    # Continues prompting if the user enters no value.
    cursor = db.cursor()
    location_input = ""
    program_count = 0
    while location_input == "":
        location_input = input("Find programs in this location: ")
    # Construct the query that incorporates the user's selection, and display formatted results.
    state_sql = "SELECT DISTINCT ProgramName FROM Participants WHERE location LIKE '%" + location_input + "%' "
    print(state_sql)
    cursor.execute(state_sql)
    records = cursor.fetchall()
    for recs in records:
        program_count = program_count + 1
    print(str(program_count) + ' Programs with the location: ' + location_input)
    for rec in records:
        print(rec)


def query_participants_by_location():
    cursor = db.cursor()
    participant_per_location_input = ""
    participant_count = 0
    while participant_per_location_input == "":
        participant_per_location_input = input("Find participants in this location: ")
    participant_per_location_sql = "SELECT PrimaryKey, FirstName, LastName FROM Participants WHERE location LIKE '%" + participant_per_location_input + "%' "
    print(participant_per_location_sql)
    cursor.execute(participant_per_location_sql)
    records = cursor.fetchall()
    for recs in records:
        participant_count = participant_count + 1
    print(str(participant_count) + ' Programs with the location: ' + participant_per_location_input)
    for rec in records:
        print(rec)

def query_locations_by_gender():
    cursor = db.cursor()
    gender_location_input = ""
    participant_count = 0
    female_count = 0
    while gender_location_input == "":
        gender_location_input = input("Find gender distribution in this location: ")
    # Construct the query that incorporates the user's selection, and display formatted results.
    state_sql = "SELECT PrimaryKey, Gender FROM Participants WHERE location LIKE '%" + gender_location_input + "%' "
    print(state_sql)
    cursor.execute(state_sql)
    records = cursor.fetchall()
    for rec in records:
        print(rec)

main()
