# This program creates the database schemas for the TU database,
# and populates the database with data extracted from the TU JSON file.
from urllib.request import urlopen
from urllib.error import URLError, HTTPError
import json
import ssl
import sqlite3


# Main function that calls the 2 functions to create and populate the database.
# Do NOT modify.
def main():
    create_database()
    insert_records()


# This function creates the tables for the database, nps_parks.db
# The DROP TABLE statements delete the tables if they exist.
# This is important if you need to re-run this program to re-create the database
#  -- if you try to re-create the tables without deleting first, an error will occur.
# Do NOT modify.
def create_database():
    drop_participants_table_sql = 'DROP TABLE IF EXISTS "PARTICIPANTS";'
    create_participants_table_sql = '''
    CREATE TABLE PARTICIPANTS
    ( 
     Id                      VARCHAR(100) NOT NULL,
     FirstName             VARCHAR(100) NOT NULL,
     LastName               VARCHAR(100) NOT NULL,
     Gender           VARCHAR(100) NOT NULL,
     BirthDate        VARCHAR(100) NOT NULL,
     EventCost        VARCHAR(100) NOT NULL, 
     TransactionTotal VARCHAR(100) NOT NULL,
     AddressPostalCode       VARCHAR(100)  NOT NULL,
     Location                VARCHAR(100)  NOT NULL,
     Year                    VARCHAR(100) NOT NULL,
     ProgramName             VARCHAR(100) NOT NULL,
     PrimaryKey              VARCHAR(100) NOT NULL, 
     
     
     
    PRIMARY KEY (PrimaryKey));
    '''
    try:
        dbname = 'youth_programs.db'
        db = sqlite3.connect(dbname)
        cursor = db.cursor()
        # Drop (delete) the tables if they exist
        cursor.execute(drop_participants_table_sql)

        # Create the table definitions
        cursor.execute(create_participants_table_sql)
        db.commit()  # save the changes
        db.close()  # close the database
    except sqlite3.IntegrityError as err:
        print('Integrity Error:', err)
    except sqlite3.OperationalError as err:
        print('Operational Error:', err)
    except sqlite3.Error as err:
        print('Error:', err)


def insert_da2017middle_school_tournament_records():
    try:
        dbname = 'youth_programs.db'
        db = sqlite3.connect(dbname)
        cursor = db.cursor()

        # ssl._create_default_https_context = ssl._create_unverified_context
        participants_file = '/Users/alex/Desktop/TU Youth Program CSVs/Durham Academy Programs/DA2017MiddleSchoolTournament.json'
        input_file = open(participants_file, 'r', encoding="utf8")
        participants_content = input_file.read()
        # The JSON parser returns a dictionary. The data that describes the parks is located in the 'data' entry.
        participants_dictionary = json.loads(participants_content)

        for participant in participants_dictionary:
            player_id = str(participant['id'])
            first_name = participant['first_name']
            last_name = participant['last_name']
            gender = participant['gender']
            birth_date = str(participant['birth_date'])
            event_cost = str(participant['event_cost'])
            transaction_total = str(participant['transaction_total'])
            address_postal_code = str(participant['postal_code'])
            location = "Durham Academy"
            year = "2017"
            program_name = "DA2017MiddleSchoolTournament"
            primary_key = player_id + program_name
            # Constructs the SQL query to insert park information into the database
            park_sql = 'INSERT OR IGNORE INTO PARTICIPANTS VALUES ("' + player_id + '","' + first_name + '", " ' + last_name + '","' + gender + '","' + birth_date + '","' + event_cost + '","' + transaction_total + '","' + address_postal_code + '","' + location + '","' + year + '","' + program_name + '","' + primary_key + '") '
            cursor.execute(park_sql)
            print(park_sql)

        db.commit()  # save the changes
        db.close()  # close the database
    except ValueError as err:
        print('An error occurred trying to decode the json text')
        print(err)
    except KeyError as err:
        print('Key not in data source')
        print(err)
    except HTTPError as err:
        print('Server could not fulfill the request.')
        print(err)
    except URLError as err:
        print('Failed to reach a server.')
        print(err)
    except sqlite3.IntegrityError as err:
        print('Integrity Error:', err)
    except sqlite3.OperationalError as err:
        print('Operational Error:', err)
    except sqlite3.Error as err:
        print('Error:', err)
    except Exception as err:
        print('An error occurred: ', err)


def insert_da2018middle_school_tournament_records():
    try:
        dbname = 'youth_programs.db'
        db = sqlite3.connect(dbname)
        cursor = db.cursor()

        # ssl._create_default_https_context = ssl._create_unverified_context
        participants_file = '/Users/alex/Desktop/TU Youth Program CSVs/Durham Academy Programs/DA2018MiddleSchoolTournament.json'
        input_file = open(participants_file, 'r', encoding="utf8")
        participants_content = input_file.read()
        # The JSON parser returns a dictionary. The data that describes the parks is located in the 'data' entry.
        participants_dictionary = json.loads(participants_content)

        for participant in participants_dictionary:
            player_id = str(participant['id'])
            first_name = participant['first_name']
            last_name = participant['last_name']
            gender = participant['gender']
            birth_date = str(participant['birth_date'])
            event_cost = str(participant['event_cost'])
            transaction_total = str(participant['transaction_total'])
            address_postal_code = str(participant['postal_code'])
            location = "Durham Academy"
            year = "2018"
            program_name = "DA2018MiddleSchoolTournament"
            primary_key = player_id + program_name
            # Constructs the SQL query to insert park information into the database
            park_sql = 'INSERT OR IGNORE INTO PARTICIPANTS VALUES ("' + player_id + '","' + first_name + '", " ' + last_name + '","' + gender + '","' + birth_date + '","' + event_cost + '","' + transaction_total + '","' + address_postal_code + '","' + location + '","' + year + '","' + program_name + '","' + primary_key + '") '
            cursor.execute(park_sql)
            print(park_sql)

        db.commit()  # save the changes
        db.close()  # close the database
    except ValueError as err:
        print('An error occurred trying to decode the json text')
        print(err)
    except KeyError as err:
        print('Key not in data source')
        print(err)
    except HTTPError as err:
        print('Server could not fulfill the request.')
        print(err)
    except URLError as err:
        print('Failed to reach a server.')
        print(err)
    except sqlite3.IntegrityError as err:
        print('Integrity Error:', err)
    except sqlite3.OperationalError as err:
        print('Operational Error:', err)
    except sqlite3.Error as err:
        print('Error:', err)
    except Exception as err:
        print('An error occurred: ', err)


def insert_lee2018hat_tournament_records():
    try:
        dbname = 'youth_programs.db'
        db = sqlite3.connect(dbname)
        cursor = db.cursor()

        # ssl._create_default_https_context = ssl._create_unverified_context
        participants_file = '/Users/alex/Desktop/TU Youth Program CSVs/Lee Fields/Lee2018HatTournament.json'
        input_file = open(participants_file, 'r', encoding="utf8")
        participants_content = input_file.read()
        # The JSON parser returns a dictionary. The data that describes the parks is located in the 'data' entry.
        participants_dictionary = json.loads(participants_content)

        for participant in participants_dictionary:
            player_id = str(participant['id'])
            first_name = participant['first_name']
            last_name = participant['last_name']
            gender = participant['gender']
            birth_date = str(participant['birth_date'])
            event_cost = str(participant['event_cost'])
            transaction_total = str(participant['transaction_total'])
            address_postal_code = str(participant['postal_code'])
            location = "Lee"
            year = "2018"
            program_name = "Lee2018HatTournament"
            primary_key = player_id + program_name
            # Constructs the SQL query to insert park information into the database
            park_sql = 'INSERT OR IGNORE INTO PARTICIPANTS VALUES ("' + player_id + '","' + first_name + '", " ' + last_name + '","' + gender + '","' + birth_date + '","' + event_cost + '","' + transaction_total + '","' + address_postal_code + '","' + location + '","' + year + '","' + program_name + '","' + primary_key + '") '
            cursor.execute(park_sql)
            print(park_sql)

        db.commit()  # save the changes
        db.close()  # close the database
    except ValueError as err:
        print('An error occurred trying to decode the json text')
        print(err)
    except KeyError as err:
        print('Key not in data source')
        print(err)
    except HTTPError as err:
        print('Server could not fulfill the request.')
        print(err)
    except URLError as err:
        print('Failed to reach a server.')
        print(err)
    except sqlite3.IntegrityError as err:
        print('Integrity Error:', err)
    except sqlite3.OperationalError as err:
        print('Operational Error:', err)
    except sqlite3.Error as err:
        print('Error:', err)
    except Exception as err:
        print('An error occurred: ', err)


def insert_kiwanis2017learn_to_compete_records():
    try:
        dbname = 'youth_programs.db'
        db = sqlite3.connect(dbname)
        cursor = db.cursor()

        # ssl._create_default_https_context = ssl._create_unverified_context
        participants_file = '/Users/alex/Desktop/TU Youth Program CSVs/Kiwanis Park/Kiwanis2017SpringLearnToCompete.json'
        input_file = open(participants_file, 'r', encoding="utf8")
        participants_content = input_file.read()
        # The JSON parser returns a dictionary. The data that describes the parks is located in the 'data' entry.
        participants_dictionary = json.loads(participants_content)

        for participant in participants_dictionary:
            player_id = str(participant['id'])
            first_name = participant['first_name']
            last_name = participant['last_name']
            gender = participant['gender']
            birth_date = str(participant['birth_date'])
            event_cost = str(participant['event_cost'])
            transaction_total = str(participant['transaction_total'])
            address_postal_code = str(participant['postal_code'])
            location = "Kiwanis"
            year = "2017"
            program_name = "Kiwanis2017LearnToCompete"
            primary_key = player_id + program_name
            # Constructs the SQL query to insert park information into the database
            park_sql = 'INSERT OR IGNORE INTO PARTICIPANTS VALUES ("' + player_id + '","' + first_name + '", " ' + last_name + '","' + gender + '","' + birth_date + '","' + event_cost + '","' + transaction_total + '","' + address_postal_code + '","' + location + '","' + year + '","' + program_name + '","' + primary_key + '") '
            cursor.execute(park_sql)
            print(park_sql)

        db.commit()  # save the changes
        db.close()  # close the database
    except ValueError as err:
        print('An error occurred trying to decode the json text')
        print(err)
    except KeyError as err:
        print('Key not in data source')
        print(err)
    except HTTPError as err:
        print('Server could not fulfill the request.')
        print(err)
    except URLError as err:
        print('Failed to reach a server.')
        print(err)
    except sqlite3.IntegrityError as err:
        print('Integrity Error:', err)
    except sqlite3.OperationalError as err:
        print('Operational Error:', err)
    except sqlite3.Error as err:
        print('Error:', err)
    except Exception as err:
        print('An error occurred: ', err)


def insert_kiwanis2017learn_to_play_records():
    try:
        dbname = 'youth_programs.db'
        db = sqlite3.connect(dbname)
        cursor = db.cursor()

        # ssl._create_default_https_context = ssl._create_unverified_context
        participants_file = '/Users/alex/Desktop/TU Youth Program CSVs/Kiwanis Park/Kiwanis2017SpringLearnToPlay.json'
        input_file = open(participants_file, 'r', encoding="utf8")
        participants_content = input_file.read()
        # The JSON parser returns a dictionary. The data that describes the parks is located in the 'data' entry.
        participants_dictionary = json.loads(participants_content)

        for participant in participants_dictionary:
            player_id = str(participant['id'])
            first_name = participant['first_name']
            last_name = participant['last_name']
            gender = participant['gender']
            birth_date = str(participant['birth_date'])
            event_cost = str(participant['event_cost'])
            transaction_total = str(participant['transaction_total'])
            address_postal_code = str(participant['postal_code'])
            location = "Kiwanis"
            year = "2017"
            program_name = "Kiwanis2017LearnToPlay"
            primary_key = player_id + program_name
            # Constructs the SQL query to insert park information into the database
            park_sql = 'INSERT OR IGNORE INTO PARTICIPANTS VALUES ("' + player_id + '","' + first_name + '", " ' + last_name + '","' + gender + '","' + birth_date + '","' + event_cost + '","' + transaction_total + '","' + address_postal_code + '","' + location + '","' + year + '","' + program_name + '","' + primary_key + '") '
            cursor.execute(park_sql)
            print(park_sql)

        db.commit()  # save the changes
        db.close()  # close the database
    except ValueError as err:
        print('An error occurred trying to decode the json text')
        print(err)
    except KeyError as err:
        print('Key not in data source')
        print(err)
    except HTTPError as err:
        print('Server could not fulfill the request.')
        print(err)
    except URLError as err:
        print('Failed to reach a server.')
        print(err)
    except sqlite3.IntegrityError as err:
        print('Integrity Error:', err)
    except sqlite3.OperationalError as err:
        print('Operational Error:', err)
    except sqlite3.Error as err:
        print('Error:', err)
    except Exception as err:
        print('An error occurred: ', err)


def insert_kiwanis2022learn_to_play_records():
    try:
        dbname = 'youth_programs.db'
        db = sqlite3.connect(dbname)
        cursor = db.cursor()

        # ssl._create_default_https_context = ssl._create_unverified_context
        participants_file = '/Users/alex/Desktop/TU Youth Program CSVs/Kiwanis Park/Kiwanis2022SpringLearnToPlay.json'
        input_file = open(participants_file, 'r', encoding="utf8")
        participants_content = input_file.read()
        # The JSON parser returns a dictionary. The data that describes the parks is located in the 'data' entry.
        participants_dictionary = json.loads(participants_content)

        for participant in participants_dictionary:
            player_id = str(participant['id'])
            first_name = participant['first_name']
            last_name = participant['last_name']
            gender = participant['gender']
            birth_date = str(participant['birth_date'])
            event_cost = str(participant['event_cost'])
            transaction_total = str(participant['transaction_total'])
            address_postal_code = str(participant['postal_code'])
            location = "Kiwanis"
            year = "2022"
            program_name = "Kiwanis2022LearnToPlay"
            primary_key = player_id + program_name
            # Constructs the SQL query to insert park information into the database
            park_sql = 'INSERT OR IGNORE INTO PARTICIPANTS VALUES ("' + player_id + '","' + first_name + '", " ' + last_name + '","' + gender + '","' + birth_date + '","' + event_cost + '","' + transaction_total + '","' + address_postal_code + '","' + location + '","' + year + '","' + program_name + '","' + primary_key + '") '
            cursor.execute(park_sql)
            print(park_sql)

        db.commit()  # save the changes
        db.close()  # close the database
    except ValueError as err:
        print('An error occurred trying to decode the json text')
        print(err)
    except KeyError as err:
        print('Key not in data source')
        print(err)
    except HTTPError as err:
        print('Server could not fulfill the request.')
        print(err)
    except URLError as err:
        print('Failed to reach a server.')
        print(err)
    except sqlite3.IntegrityError as err:
        print('Integrity Error:', err)
    except sqlite3.OperationalError as err:
        print('Operational Error:', err)
    except sqlite3.Error as err:
        print('Error:', err)
    except Exception as err:
        print('An error occurred: ', err)


def insert_kiwanis2022rec_league():
    try:
        dbname = 'youth_programs.db'
        db = sqlite3.connect(dbname)
        cursor = db.cursor()

        # ssl._create_default_https_context = ssl._create_unverified_context
        participants_file = '/Users/alex/Desktop/TU Youth Program CSVs/Kiwanis Park/Kiwanis2022SpringRecLeague.json'
        input_file = open(participants_file, 'r', encoding="utf8")
        participants_content = input_file.read()
        # The JSON parser returns a dictionary. The data that describes the parks is located in the 'data' entry.
        participants_dictionary = json.loads(participants_content)

        for participant in participants_dictionary:
            player_id = str(participant['id'])
            first_name = participant['first_name']
            last_name = participant['last_name']
            gender = participant['gender']
            birth_date = str(participant['birth_date'])
            event_cost = str(participant['event_cost'])
            transaction_total = str(participant['transaction_total'])
            address_postal_code = str(participant['postal_code'])
            location = "Kiwanis"
            year = "2022"
            program_name = "Kiwanis2022RecLeague"
            primary_key = player_id + program_name
            # Constructs the SQL query to insert park information into the database
            park_sql = 'INSERT OR IGNORE INTO PARTICIPANTS VALUES ("' + player_id + '","' + first_name + '", " ' + last_name + '","' + gender + '","' + birth_date + '","' + event_cost + '","' + transaction_total + '","' + address_postal_code + '","' + location + '","' + year + '","' + program_name + '","' + primary_key + '") '
            cursor.execute(park_sql)
            print(park_sql)

        db.commit()  # save the changes
        db.close()  # close the database
    except ValueError as err:
        print('An error occurred trying to decode the json text')
        print(err)
    except KeyError as err:
        print('Key not in data source')
        print(err)
    except HTTPError as err:
        print('Server could not fulfill the request.')
        print(err)
    except URLError as err:
        print('Failed to reach a server.')
        print(err)
    except sqlite3.IntegrityError as err:
        print('Integrity Error:', err)
    except sqlite3.OperationalError as err:
        print('Operational Error:', err)
    except sqlite3.Error as err:
        print('Error:', err)
    except Exception as err:
        print('An error occurred: ', err)


def insert_meadowmont2017summer_league():
    try:
        dbname = 'youth_programs.db'
        db = sqlite3.connect(dbname)
        cursor = db.cursor()

        # ssl._create_default_https_context = ssl._create_unverified_context
        participants_file = '/Users/alex/Desktop/TU Youth Program CSVs/Meadowmont/Meadowmont2017SummerCompetitiveLeague.json'
        input_file = open(participants_file, 'r', encoding="utf8")
        participants_content = input_file.read()
        # The JSON parser returns a dictionary. The data that describes the parks is located in the 'data' entry.
        participants_dictionary = json.loads(participants_content)

        for participant in participants_dictionary:
            player_id = str(participant['id'])
            first_name = participant['first_name']
            last_name = participant['last_name']
            gender = participant['gender']
            birth_date = str(participant['birth_date'])
            event_cost = str(participant['event_cost'])
            transaction_total = str(participant['transaction_total'])
            address_postal_code = str(participant['postal_code'])
            location = "Meadowmont"
            year = "2017"
            program_name = "Meadowmont2017SummerLeague"
            primary_key = player_id + program_name
            # Constructs the SQL query to insert park information into the database
            park_sql = 'INSERT OR IGNORE INTO PARTICIPANTS VALUES ("' + player_id + '","' + first_name + '", " ' + last_name + '","' + gender + '","' + birth_date + '","' + event_cost + '","' + transaction_total + '","' + address_postal_code + '","' + location + '","' + year + '","' + program_name + '","' + primary_key + '") '
            cursor.execute(park_sql)
            print(park_sql)

        db.commit()  # save the changes
        db.close()  # close the database
    except ValueError as err:
        print('An error occurred trying to decode the json text')
        print(err)
    except KeyError as err:
        print('Key not in data source')
        print(err)
    except HTTPError as err:
        print('Server could not fulfill the request.')
        print(err)
    except URLError as err:
        print('Failed to reach a server.')
        print(err)
    except sqlite3.IntegrityError as err:
        print('Integrity Error:', err)
    except sqlite3.OperationalError as err:
        print('Operational Error:', err)
    except sqlite3.Error as err:
        print('Error:', err)
    except Exception as err:
        print('An error occurred: ', err)


def insert_meadowmont2022learn_to_play():
    try:
        dbname = 'youth_programs.db'
        db = sqlite3.connect(dbname)
        cursor = db.cursor()

        # ssl._create_default_https_context = ssl._create_unverified_context
        participants_file = '/Users/alex/Desktop/TU Youth Program CSVs/Meadowmont/Meadowmont2022SpringLearnToPlay.json'
        input_file = open(participants_file, 'r', encoding="utf8")
        participants_content = input_file.read()
        # The JSON parser returns a dictionary. The data that describes the parks is located in the 'data' entry.
        participants_dictionary = json.loads(participants_content)

        for participant in participants_dictionary:
            player_id = str(participant['id'])
            first_name = participant['first_name']
            last_name = participant['last_name']
            gender = participant['gender']
            birth_date = str(participant['birth_date'])
            event_cost = str(participant['event_cost'])
            transaction_total = str(participant['transaction_total'])
            address_postal_code = str(participant['postal_code'])
            location = "Meadowmont"
            year = "2022"
            program_name = "Meadowmont2022LearnToPlay"
            primary_key = player_id + program_name
            # Constructs the SQL query to insert park information into the database
            park_sql = 'INSERT OR IGNORE INTO PARTICIPANTS VALUES ("' + player_id + '","' + first_name + '", " ' + last_name + '","' + gender + '","' + birth_date + '","' + event_cost + '","' + transaction_total + '","' + address_postal_code + '","' + location + '","' + year + '","' + program_name + '","' + primary_key + '") '
            cursor.execute(park_sql)
            print(park_sql)

        db.commit()  # save the changes
        db.close()  # close the database
    except ValueError as err:
        print('An error occurred trying to decode the json text')
        print(err)
    except KeyError as err:
        print('Key not in data source')
        print(err)
    except HTTPError as err:
        print('Server could not fulfill the request.')
        print(err)
    except URLError as err:
        print('Failed to reach a server.')
        print(err)
    except sqlite3.IntegrityError as err:
        print('Integrity Error:', err)
    except sqlite3.OperationalError as err:
        print('Operational Error:', err)
    except sqlite3.Error as err:
        print('Error:', err)
    except Exception as err:
        print('An error occurred: ', err)


def insert_miller2017learn_to_play():
    try:
        dbname = 'youth_programs.db'
        db = sqlite3.connect(dbname)
        cursor = db.cursor()

        # ssl._create_default_https_context = ssl._create_unverified_context
        participants_file = '/Users/alex/Desktop/TU Youth Program CSVs/Miller Field/Miller2017FallLearnToPlay.json'
        input_file = open(participants_file, 'r', encoding="utf8")
        participants_content = input_file.read()
        # The JSON parser returns a dictionary. The data that describes the parks is located in the 'data' entry.
        participants_dictionary = json.loads(participants_content)

        for participant in participants_dictionary:
            player_id = str(participant['id'])
            first_name = participant['first_name']
            last_name = participant['last_name']
            gender = participant['gender']
            birth_date = str(participant['birth_date'])
            event_cost = str(participant['event_cost'])
            transaction_total = str(participant['transaction_total'])
            address_postal_code = str(participant['postal_code'])
            location = "Miller"
            year = "2017"
            program_name = "Miller2017LearnToPlay"
            primary_key = player_id + program_name
            # Constructs the SQL query to insert park information into the database
            park_sql = 'INSERT OR IGNORE INTO PARTICIPANTS VALUES ("' + player_id + '","' + first_name + '", " ' + last_name + '","' + gender + '","' + birth_date + '","' + event_cost + '","' + transaction_total + '","' + address_postal_code + '","' + location + '","' + year + '","' + program_name + '","' + primary_key + '") '
            cursor.execute(park_sql)
            print(park_sql)

        db.commit()  # save the changes
        db.close()  # close the database
    except ValueError as err:
        print('An error occurred trying to decode the json text')
        print(err)
    except KeyError as err:
        print('Key not in data source')
        print(err)
    except HTTPError as err:
        print('Server could not fulfill the request.')
        print(err)
    except URLError as err:
        print('Failed to reach a server.')
        print(err)
    except sqlite3.IntegrityError as err:
        print('Integrity Error:', err)
    except sqlite3.OperationalError as err:
        print('Operational Error:', err)
    except sqlite3.Error as err:
        print('Error:', err)
    except Exception as err:
        print('An error occurred: ', err)


def insert_miller2017learn_to_compete():
    try:
        dbname = 'youth_programs.db'
        db = sqlite3.connect(dbname)
        cursor = db.cursor()

        # ssl._create_default_https_context = ssl._create_unverified_context
        participants_file = '/Users/alex/Desktop/TU Youth Program CSVs/Miller Field/Miller2017FallLearnToCompete.json'
        input_file = open(participants_file, 'r', encoding="utf8")
        participants_content = input_file.read()
        # The JSON parser returns a dictionary. The data that describes the parks is located in the 'data' entry.
        participants_dictionary = json.loads(participants_content)

        for participant in participants_dictionary:
            player_id = str(participant['id'])
            first_name = participant['first_name']
            last_name = participant['last_name']
            gender = participant['gender']
            birth_date = str(participant['birth_date'])
            event_cost = str(participant['event_cost'])
            transaction_total = str(participant['transaction_total'])
            address_postal_code = str(participant['postal_code'])
            location = "Miller"
            year = "2017"
            program_name = "Miller2017LearnToCompete"
            primary_key = player_id + program_name
            # Constructs the SQL query to insert park information into the database
            park_sql = 'INSERT OR IGNORE INTO PARTICIPANTS VALUES ("' + player_id + '","' + first_name + '", " ' + last_name + '","' + gender + '","' + birth_date + '","' + event_cost + '","' + transaction_total + '","' + address_postal_code + '","' + location + '","' + year + '","' + program_name + '","' + primary_key + '") '
            cursor.execute(park_sql)
            print(park_sql)

        db.commit()  # save the changes
        db.close()  # close the database
    except ValueError as err:
        print('An error occurred trying to decode the json text')
        print(err)
    except KeyError as err:
        print('Key not in data source')
        print(err)
    except HTTPError as err:
        print('Server could not fulfill the request.')
        print(err)
    except URLError as err:
        print('Failed to reach a server.')
        print(err)
    except sqlite3.IntegrityError as err:
        print('Integrity Error:', err)
    except sqlite3.OperationalError as err:
        print('Operational Error:', err)
    except sqlite3.Error as err:
        print('Error:', err)
    except Exception as err:
        print('An error occurred: ', err)


def insert_miller2018wolfpack_tournament():
    try:
        dbname = 'youth_programs.db'
        db = sqlite3.connect(dbname)
        cursor = db.cursor()

        # ssl._create_default_https_context = ssl._create_unverified_context
        participants_file = '/Users/alex/Desktop/TU Youth Program CSVs/Miller Field/Miller2018WolfpackTournament.json'
        input_file = open(participants_file, 'r', encoding="utf8")
        participants_content = input_file.read()
        # The JSON parser returns a dictionary. The data that describes the parks is located in the 'data' entry.
        participants_dictionary = json.loads(participants_content)

        for participant in participants_dictionary:
            player_id = str(participant['id'])
            first_name = participant['first_name']
            last_name = participant['last_name']
            gender = participant['gender']
            birth_date = str(participant['birth_date'])
            event_cost = str(participant['event_cost'])
            transaction_total = str(participant['transaction_total'])
            address_postal_code = str(participant['postal_code'])
            location = "Miller"
            year = "2018"
            program_name = "Miller2018WolfpackTournament"
            primary_key = player_id + program_name
            # Constructs the SQL query to insert park information into the database
            park_sql = 'INSERT OR IGNORE INTO PARTICIPANTS VALUES ("' + player_id + '","' + first_name + '", " ' + last_name + '","' + gender + '","' + birth_date + '","' + event_cost + '","' + transaction_total + '","' + address_postal_code + '","' + location + '","' + year + '","' + program_name + '","' + primary_key + '") '
            cursor.execute(park_sql)
            print(park_sql)

        db.commit()  # save the changes
        db.close()  # close the database
    except ValueError as err:
        print('An error occurred trying to decode the json text')
        print(err)
    except KeyError as err:
        print('Key not in data source')
        print(err)
    except HTTPError as err:
        print('Server could not fulfill the request.')
        print(err)
    except URLError as err:
        print('Failed to reach a server.')
        print(err)
    except sqlite3.IntegrityError as err:
        print('Integrity Error:', err)
    except sqlite3.OperationalError as err:
        print('Operational Error:', err)
    except sqlite3.Error as err:
        print('Error:', err)
    except Exception as err:
        print('An error occurred: ', err)


def insert_miller2019wolfpack_tournament():
    try:
        dbname = 'youth_programs.db'
        db = sqlite3.connect(dbname)
        cursor = db.cursor()

        # ssl._create_default_https_context = ssl._create_unverified_context
        participants_file = '/Users/alex/Desktop/TU Youth Program CSVs/Miller Field/Miller2019WolfpackTournament.json'
        input_file = open(participants_file, 'r', encoding="utf8")
        participants_content = input_file.read()
        # The JSON parser returns a dictionary. The data that describes the parks is located in the 'data' entry.
        participants_dictionary = json.loads(participants_content)

        for participant in participants_dictionary:
            player_id = str(participant['id'])
            first_name = participant['first_name']
            last_name = participant['last_name']
            gender = participant['gender']
            birth_date = str(participant['birth_date'])
            event_cost = str(participant['event_cost'])
            transaction_total = str(participant['transaction_total'])
            address_postal_code = str(participant['postal_code'])
            location = "Miller"
            year = "2019"
            program_name = "Miller2019WolfpackTournament"
            primary_key = player_id + program_name
            # Constructs the SQL query to insert park information into the database
            park_sql = 'INSERT OR IGNORE INTO PARTICIPANTS VALUES ("' + player_id + '","' + first_name + '", " ' + last_name + '","' + gender + '","' + birth_date + '","' + event_cost + '","' + transaction_total + '","' + address_postal_code + '","' + location + '","' + year + '","' + program_name + '","' + primary_key + '") '
            cursor.execute(park_sql)
            print(park_sql)

        db.commit()  # save the changes
        db.close()  # close the database
    except ValueError as err:
        print('An error occurred trying to decode the json text')
        print(err)
    except KeyError as err:
        print('Key not in data source')
        print(err)
    except HTTPError as err:
        print('Server could not fulfill the request.')
        print(err)
    except URLError as err:
        print('Failed to reach a server.')
        print(err)
    except sqlite3.IntegrityError as err:
        print('Integrity Error:', err)
    except sqlite3.OperationalError as err:
        print('Operational Error:', err)
    except sqlite3.Error as err:
        print('Error:', err)
    except Exception as err:
        print('An error occurred: ', err)


def insert_miller2019middle_school_championship():
    try:
        dbname = 'youth_programs.db'
        db = sqlite3.connect(dbname)
        cursor = db.cursor()

        # ssl._create_default_https_context = ssl._create_unverified_context
        participants_file = '/Users/alex/Desktop/TU Youth Program CSVs/Miller Field/Miller2019MiddleSchoolChampionship.json'
        input_file = open(participants_file, 'r', encoding="utf8")
        participants_content = input_file.read()
        # The JSON parser returns a dictionary. The data that describes the parks is located in the 'data' entry.
        participants_dictionary = json.loads(participants_content)

        for participant in participants_dictionary:
            player_id = str(participant['id'])
            first_name = participant['first_name']
            last_name = participant['last_name']
            gender = participant['gender']
            birth_date = str(participant['birth_date'])
            event_cost = str(participant['event_cost'])
            transaction_total = str(participant['transaction_total'])
            address_postal_code = str(participant['postal_code'])
            location = "Miller"
            year = "2019"
            program_name = "Miller2019MiddleSchoolChampionship"
            primary_key = player_id + program_name
            # Constructs the SQL query to insert park information into the database
            park_sql = 'INSERT OR IGNORE INTO PARTICIPANTS VALUES ("' + player_id + '","' + first_name + '", " ' + last_name + '","' + gender + '","' + birth_date + '","' + event_cost + '","' + transaction_total + '","' + address_postal_code + '","' + location + '","' + year + '","' + program_name + '","' + primary_key + '") '
            cursor.execute(park_sql)
            print(park_sql)

        db.commit()  # save the changes
        db.close()  # close the database
    except ValueError as err:
        print('An error occurred trying to decode the json text')
        print(err)
    except KeyError as err:
        print('Key not in data source')
        print(err)
    except HTTPError as err:
        print('Server could not fulfill the request.')
        print(err)
    except URLError as err:
        print('Failed to reach a server.')
        print(err)
    except sqlite3.IntegrityError as err:
        print('Integrity Error:', err)
    except sqlite3.OperationalError as err:
        print('Operational Error:', err)
    except sqlite3.Error as err:
        print('Error:', err)
    except Exception as err:
        print('An error occurred: ', err)


def insert_miller2020middle_school_championship():
    try:
        dbname = 'youth_programs.db'
        db = sqlite3.connect(dbname)
        cursor = db.cursor()

        # ssl._create_default_https_context = ssl._create_unverified_context
        participants_file = '/Users/alex/Desktop/TU Youth Program CSVs/Miller Field/Miller2020MiddleSchoolChampionship.json'
        input_file = open(participants_file, 'r', encoding="utf8")
        participants_content = input_file.read()
        # The JSON parser returns a dictionary. The data that describes the parks is located in the 'data' entry.
        participants_dictionary = json.loads(participants_content)

        for participant in participants_dictionary:
            player_id = str(participant['id'])
            first_name = participant['first_name']
            last_name = participant['last_name']
            gender = participant['gender']
            birth_date = str(participant['birth_date'])
            event_cost = str(participant['event_cost'])
            transaction_total = str(participant['transaction_total'])
            address_postal_code = str(participant['postal_code'])
            location = "Miller"
            year = "2020"
            program_name = "Miller2020MiddleSchoolChampionship"
            primary_key = player_id + program_name
            # Constructs the SQL query to insert park information into the database
            park_sql = 'INSERT OR IGNORE INTO PARTICIPANTS VALUES ("' + player_id + '","' + first_name + '", " ' + last_name + '","' + gender + '","' + birth_date + '","' + event_cost + '","' + transaction_total + '","' + address_postal_code + '","' + location + '","' + year + '","' + program_name + '","' + primary_key + '") '
            cursor.execute(park_sql)
            print(park_sql)

        db.commit()  # save the changes
        db.close()  # close the database
    except ValueError as err:
        print('An error occurred trying to decode the json text')
        print(err)
    except KeyError as err:
        print('Key not in data source')
        print(err)
    except HTTPError as err:
        print('Server could not fulfill the request.')
        print(err)
    except URLError as err:
        print('Failed to reach a server.')
        print(err)
    except sqlite3.IntegrityError as err:
        print('Integrity Error:', err)
    except sqlite3.OperationalError as err:
        print('Operational Error:', err)
    except sqlite3.Error as err:
        print('Error:', err)
    except Exception as err:
        print('An error occurred: ', err)


def insert_miller2022middle_school_championship():
    try:
        dbname = 'youth_programs.db'
        db = sqlite3.connect(dbname)
        cursor = db.cursor()

        # ssl._create_default_https_context = ssl._create_unverified_context
        participants_file = '/Users/alex/Desktop/TU Youth Program CSVs/Miller Field/Miller2022MiddleSchoolChampionship.json'
        input_file = open(participants_file, 'r', encoding="utf8")
        participants_content = input_file.read()
        # The JSON parser returns a dictionary. The data that describes the parks is located in the 'data' entry.
        participants_dictionary = json.loads(participants_content)

        for participant in participants_dictionary:
            player_id = str(participant['id'])
            first_name = participant['first_name']
            last_name = participant['last_name']
            gender = participant['gender']
            birth_date = str(participant['birth_date'])
            event_cost = str(participant['event_cost'])
            transaction_total = str(participant['transaction_total'])
            address_postal_code = str(participant['postal_code'])
            location = "Miller"
            year = "2022"
            program_name = "Miller2022MiddleSchoolChampionship"
            primary_key = player_id + program_name
            # Constructs the SQL query to insert park information into the database
            park_sql = 'INSERT OR IGNORE INTO PARTICIPANTS VALUES ("' + player_id + '","' + first_name + '", " ' + last_name + '","' + gender + '","' + birth_date + '","' + event_cost + '","' + transaction_total + '","' + address_postal_code + '","' + location + '","' + year + '","' + program_name + '","' + primary_key + '") '
            cursor.execute(park_sql)
            print(park_sql)

        db.commit()  # save the changes
        db.close()  # close the database
    except ValueError as err:
        print('An error occurred trying to decode the json text')
        print(err)
    except KeyError as err:
        print('Key not in data source')
        print(err)
    except HTTPError as err:
        print('Server could not fulfill the request.')
        print(err)
    except URLError as err:
        print('Failed to reach a server.')
        print(err)
    except sqlite3.IntegrityError as err:
        print('Integrity Error:', err)
    except sqlite3.OperationalError as err:
        print('Operational Error:', err)
    except sqlite3.Error as err:
        print('Error:', err)
    except Exception as err:
        print('An error occurred: ', err)


def insert_herndon2017learn_to_compete():
    try:
        dbname = 'youth_programs.db'
        db = sqlite3.connect(dbname)
        cursor = db.cursor()

        # ssl._create_default_https_context = ssl._create_unverified_context
        participants_file = '/Users/alex/Desktop/TU Youth Program CSVs/Herndon Park/Herndon2017FallLearnToCompete.json'
        input_file = open(participants_file, 'r', encoding="utf8")
        participants_content = input_file.read()
        # The JSON parser returns a dictionary. The data that describes the parks is located in the 'data' entry.
        participants_dictionary = json.loads(participants_content)

        for participant in participants_dictionary:
            player_id = str(participant['id'])
            first_name = participant['first_name']
            last_name = participant['last_name']
            gender = participant['gender']
            birth_date = str(participant['birth_date'])
            event_cost = str(participant['event_cost'])
            transaction_total = str(participant['transaction_total'])
            address_postal_code = str(participant['postal_code'])
            location = "Herndon"
            year = "2017"
            program_name = "Herndon2017LearnToCompete"
            primary_key = player_id + program_name
            # Constructs the SQL query to insert park information into the database
            park_sql = 'INSERT OR IGNORE INTO PARTICIPANTS VALUES ("' + player_id + '","' + first_name + '", " ' + last_name + '","' + gender + '","' + birth_date + '","' + event_cost + '","' + transaction_total + '","' + address_postal_code + '","' + location + '","' + year + '","' + program_name + '","' + primary_key + '") '
            cursor.execute(park_sql)
            print(park_sql)

        db.commit()  # save the changes
        db.close()  # close the database
    except ValueError as err:
        print('An error occurred trying to decode the json text')
        print(err)
    except KeyError as err:
        print('Key not in data source')
        print(err)
    except HTTPError as err:
        print('Server could not fulfill the request.')
        print(err)
    except URLError as err:
        print('Failed to reach a server.')
        print(err)
    except sqlite3.IntegrityError as err:
        print('Integrity Error:', err)
    except sqlite3.OperationalError as err:
        print('Operational Error:', err)
    except sqlite3.Error as err:
        print('Error:', err)
    except Exception as err:
        print('An error occurred: ', err)


def insert_herndon2017learn_to_play():
    try:
        dbname = 'youth_programs.db'
        db = sqlite3.connect(dbname)
        cursor = db.cursor()

        # ssl._create_default_https_context = ssl._create_unverified_context
        participants_file = '/Users/alex/Desktop/TU Youth Program CSVs/Herndon Park/Herndon2017FallLearnToPlay.json'
        input_file = open(participants_file, 'r', encoding="utf8")
        participants_content = input_file.read()
        # The JSON parser returns a dictionary. The data that describes the parks is located in the 'data' entry.
        participants_dictionary = json.loads(participants_content)

        for participant in participants_dictionary:
            player_id = str(participant['id'])
            first_name = participant['first_name']
            last_name = participant['last_name']
            gender = participant['gender']
            birth_date = str(participant['birth_date'])
            event_cost = str(participant['event_cost'])
            transaction_total = str(participant['transaction_total'])
            address_postal_code = str(participant['postal_code'])
            location = "Herndon"
            year = "2017"
            program_name = "Herndon2017LearnToPlay"
            primary_key = player_id + program_name
            # Constructs the SQL query to insert park information into the database
            park_sql = 'INSERT OR IGNORE INTO PARTICIPANTS VALUES ("' + player_id + '","' + first_name + '", " ' + last_name + '","' + gender + '","' + birth_date + '","' + event_cost + '","' + transaction_total + '","' + address_postal_code + '","' + location + '","' + year + '","' + program_name + '","' + primary_key + '") '
            cursor.execute(park_sql)
            print(park_sql)

        db.commit()  # save the changes
        db.close()  # close the database
    except ValueError as err:
        print('An error occurred trying to decode the json text')
        print(err)
    except KeyError as err:
        print('Key not in data source')
        print(err)
    except HTTPError as err:
        print('Server could not fulfill the request.')
        print(err)
    except URLError as err:
        print('Failed to reach a server.')
        print(err)
    except sqlite3.IntegrityError as err:
        print('Integrity Error:', err)
    except sqlite3.OperationalError as err:
        print('Operational Error:', err)
    except sqlite3.Error as err:
        print('Error:', err)
    except Exception as err:
        print('An error occurred: ', err)


def insert_herndon2018learn_to_compete():
    try:
        dbname = 'youth_programs.db'
        db = sqlite3.connect(dbname)
        cursor = db.cursor()

        # ssl._create_default_https_context = ssl._create_unverified_context
        participants_file = '/Users/alex/Desktop/TU Youth Program CSVs/Herndon Park/Herndon2018FallLearnToCompete.json'
        input_file = open(participants_file, 'r', encoding="utf8")
        participants_content = input_file.read()
        # The JSON parser returns a dictionary. The data that describes the parks is located in the 'data' entry.
        participants_dictionary = json.loads(participants_content)

        for participant in participants_dictionary:
            player_id = str(participant['id'])
            first_name = participant['first_name']
            last_name = participant['last_name']
            gender = participant['gender']
            birth_date = str(participant['birth_date'])
            event_cost = str(participant['event_cost'])
            transaction_total = str(participant['transaction_total'])
            address_postal_code = str(participant['postal_code'])
            location = "Herndon"
            year = "2018"
            program_name = "Herndon2018LearnToCompete"
            primary_key = player_id + program_name
            # Constructs the SQL query to insert park information into the database
            park_sql = 'INSERT OR IGNORE INTO PARTICIPANTS VALUES ("' + player_id + '","' + first_name + '", " ' + last_name + '","' + gender + '","' + birth_date + '","' + event_cost + '","' + transaction_total + '","' + address_postal_code + '","' + location + '","' + year + '","' + program_name + '","' + primary_key + '") '
            cursor.execute(park_sql)
            print(park_sql)

        db.commit()  # save the changes
        db.close()  # close the database
    except ValueError as err:
        print('An error occurred trying to decode the json text')
        print(err)
    except KeyError as err:
        print('Key not in data source')
        print(err)
    except HTTPError as err:
        print('Server could not fulfill the request.')
        print(err)
    except URLError as err:
        print('Failed to reach a server.')
        print(err)
    except sqlite3.IntegrityError as err:
        print('Integrity Error:', err)
    except sqlite3.OperationalError as err:
        print('Operational Error:', err)
    except sqlite3.Error as err:
        print('Error:', err)
    except Exception as err:
        print('An error occurred: ', err)


def insert_herndon2018learn_to_play():
    try:
        dbname = 'youth_programs.db'
        db = sqlite3.connect(dbname)
        cursor = db.cursor()

        # ssl._create_default_https_context = ssl._create_unverified_context
        participants_file = '/Users/alex/Desktop/TU Youth Program CSVs/Herndon Park/Herndon2018FallLearnToPlay.json'
        input_file = open(participants_file, 'r', encoding="utf8")
        participants_content = input_file.read()
        # The JSON parser returns a dictionary. The data that describes the parks is located in the 'data' entry.
        participants_dictionary = json.loads(participants_content)

        for participant in participants_dictionary:
            player_id = str(participant['id'])
            first_name = participant['first_name']
            last_name = participant['last_name']
            gender = participant['gender']
            birth_date = str(participant['birth_date'])
            event_cost = str(participant['event_cost'])
            transaction_total = str(participant['transaction_total'])
            address_postal_code = str(participant['postal_code'])
            location = "Herndon"
            year = "2018"
            program_name = "Herndon2018LearnToPlay"
            primary_key = player_id + program_name
            # Constructs the SQL query to insert park information into the database
            park_sql = 'INSERT OR IGNORE INTO PARTICIPANTS VALUES ("' + player_id + '","' + first_name + '", " ' + last_name + '","' + gender + '","' + birth_date + '","' + event_cost + '","' + transaction_total + '","' + address_postal_code + '","' + location + '","' + year + '","' + program_name + '","' + primary_key + '") '
            cursor.execute(park_sql)
            print(park_sql)

        db.commit()  # save the changes
        db.close()  # close the database
    except ValueError as err:
        print('An error occurred trying to decode the json text')
        print(err)
    except KeyError as err:
        print('Key not in data source')
        print(err)
    except HTTPError as err:
        print('Server could not fulfill the request.')
        print(err)
    except URLError as err:
        print('Failed to reach a server.')
        print(err)
    except sqlite3.IntegrityError as err:
        print('Integrity Error:', err)
    except sqlite3.OperationalError as err:
        print('Operational Error:', err)
    except sqlite3.Error as err:
        print('Error:', err)
    except Exception as err:
        print('An error occurred: ', err)


def insert_herndon2018gum():
    try:
        dbname = 'youth_programs.db'
        db = sqlite3.connect(dbname)
        cursor = db.cursor()

        # ssl._create_default_https_context = ssl._create_unverified_context
        participants_file = '/Users/alex/Desktop/TU Youth Program CSVs/Herndon Park/Herndon2018GUM.json'
        input_file = open(participants_file, 'r', encoding="utf8")
        participants_content = input_file.read()
        # The JSON parser returns a dictionary. The data that describes the parks is located in the 'data' entry.
        participants_dictionary = json.loads(participants_content)

        for participant in participants_dictionary:
            player_id = str(participant['id'])
            first_name = participant['first_name']
            last_name = participant['last_name']
            gender = participant['gender']
            birth_date = str(participant['birth_date'])
            event_cost = str(participant['event_cost'])
            transaction_total = str(participant['transaction_total'])
            address_postal_code = str(participant['postal_code'])
            location = "Herndon"
            year = "2018"
            program_name = "Herndon2018GUM"
            primary_key = player_id + program_name
            # Constructs the SQL query to insert park information into the database
            park_sql = 'INSERT OR IGNORE INTO PARTICIPANTS VALUES ("' + player_id + '","' + first_name + '", " ' + last_name + '","' + gender + '","' + birth_date + '","' + event_cost + '","' + transaction_total + '","' + address_postal_code + '","' + location + '","' + year + '","' + program_name + '","' + primary_key + '") '
            cursor.execute(park_sql)
            print(park_sql)

        db.commit()  # save the changes
        db.close()  # close the database
    except ValueError as err:
        print('An error occurred trying to decode the json text')
        print(err)
    except KeyError as err:
        print('Key not in data source')
        print(err)
    except HTTPError as err:
        print('Server could not fulfill the request.')
        print(err)
    except URLError as err:
        print('Failed to reach a server.')
        print(err)
    except sqlite3.IntegrityError as err:
        print('Integrity Error:', err)
    except sqlite3.OperationalError as err:
        print('Operational Error:', err)
    except sqlite3.Error as err:
        print('Error:', err)
    except Exception as err:
        print('An error occurred: ', err)


def insert_herndon2019learn_to_compete():
    try:
        dbname = 'youth_programs.db'
        db = sqlite3.connect(dbname)
        cursor = db.cursor()

        # ssl._create_default_https_context = ssl._create_unverified_context
        participants_file = '/Users/alex/Desktop/TU Youth Program CSVs/Herndon Park/Herndon2019SpringLearnToCompete.json'
        input_file = open(participants_file, 'r', encoding="utf8")
        participants_content = input_file.read()
        # The JSON parser returns a dictionary. The data that describes the parks is located in the 'data' entry.
        participants_dictionary = json.loads(participants_content)

        for participant in participants_dictionary:
            player_id = str(participant['id'])
            first_name = participant['first_name']
            last_name = participant['last_name']
            gender = participant['gender']
            birth_date = str(participant['birth_date'])
            event_cost = str(participant['event_cost'])
            transaction_total = str(participant['transaction_total'])
            address_postal_code = str(participant['postal_code'])
            location = "Herndon"
            year = "2019"
            program_name = "Herndon2019LearnToCompete"
            primary_key = player_id + program_name
            # Constructs the SQL query to insert park information into the database
            park_sql = 'INSERT OR IGNORE INTO PARTICIPANTS VALUES ("' + player_id + '","' + first_name + '", " ' + last_name + '","' + gender + '","' + birth_date + '","' + event_cost + '","' + transaction_total + '","' + address_postal_code + '","' + location + '","' + year + '","' + program_name + '","' + primary_key + '") '
            cursor.execute(park_sql)
            print(park_sql)

        db.commit()  # save the changes
        db.close()  # close the database
    except ValueError as err:
        print('An error occurred trying to decode the json text')
        print(err)
    except KeyError as err:
        print('Key not in data source')
        print(err)
    except HTTPError as err:
        print('Server could not fulfill the request.')
        print(err)
    except URLError as err:
        print('Failed to reach a server.')
        print(err)
    except sqlite3.IntegrityError as err:
        print('Integrity Error:', err)
    except sqlite3.OperationalError as err:
        print('Operational Error:', err)
    except sqlite3.Error as err:
        print('Error:', err)
    except Exception as err:
        print('An error occurred: ', err)


def insert_herndon2019learn_to_compete_girls():
    try:
        dbname = 'youth_programs.db'
        db = sqlite3.connect(dbname)
        cursor = db.cursor()

        # ssl._create_default_https_context = ssl._create_unverified_context
        participants_file = '/Users/alex/Desktop/TU Youth Program CSVs/Herndon Park/Herndon2019SpringLearnToCompeteGirls.json'
        input_file = open(participants_file, 'r', encoding="utf8")
        participants_content = input_file.read()
        # The JSON parser returns a dictionary. The data that describes the parks is located in the 'data' entry.
        participants_dictionary = json.loads(participants_content)

        for participant in participants_dictionary:
            player_id = str(participant['id'])
            first_name = participant['first_name']
            last_name = participant['last_name']
            gender = participant['gender']
            birth_date = str(participant['birth_date'])
            event_cost = str(participant['event_cost'])
            transaction_total = str(participant['transaction_total'])
            address_postal_code = str(participant['postal_code'])
            location = "Herndon"
            year = "2019"
            program_name = "Herndon2019LearnToCompeteGirls"
            primary_key = player_id + program_name
            # Constructs the SQL query to insert park information into the database
            park_sql = 'INSERT OR IGNORE INTO PARTICIPANTS VALUES ("' + player_id + '","' + first_name + '", " ' + last_name + '","' + gender + '","' + birth_date + '","' + event_cost + '","' + transaction_total + '","' + address_postal_code + '","' + location + '","' + year + '","' + program_name + '","' + primary_key + '") '
            cursor.execute(park_sql)
            print(park_sql)

        db.commit()  # save the changes
        db.close()  # close the database
    except ValueError as err:
        print('An error occurred trying to decode the json text')
        print(err)
    except KeyError as err:
        print('Key not in data source')
        print(err)
    except HTTPError as err:
        print('Server could not fulfill the request.')
        print(err)
    except URLError as err:
        print('Failed to reach a server.')
        print(err)
    except sqlite3.IntegrityError as err:
        print('Integrity Error:', err)
    except sqlite3.OperationalError as err:
        print('Operational Error:', err)
    except sqlite3.Error as err:
        print('Error:', err)
    except Exception as err:
        print('An error occurred: ', err)


def insert_herndon2019learn_to_play():
    try:
        dbname = 'youth_programs.db'
        db = sqlite3.connect(dbname)
        cursor = db.cursor()

        # ssl._create_default_https_context = ssl._create_unverified_context
        participants_file = '/Users/alex/Desktop/TU Youth Program CSVs/Herndon Park/Herndon2019SpringLearnToPlay.json'
        input_file = open(participants_file, 'r', encoding="utf8")
        participants_content = input_file.read()
        # The JSON parser returns a dictionary. The data that describes the parks is located in the 'data' entry.
        participants_dictionary = json.loads(participants_content)

        for participant in participants_dictionary:
            player_id = str(participant['id'])
            first_name = participant['first_name']
            last_name = participant['last_name']
            gender = participant['gender']
            birth_date = str(participant['birth_date'])
            event_cost = str(participant['event_cost'])
            transaction_total = str(participant['transaction_total'])
            address_postal_code = str(participant['postal_code'])
            location = "Herndon"
            year = "2019"
            program_name = "Herndon2019LearnToPlay"
            primary_key = player_id + program_name
            # Constructs the SQL query to insert park information into the database
            park_sql = 'INSERT OR IGNORE INTO PARTICIPANTS VALUES ("' + player_id + '","' + first_name + '", " ' + last_name + '","' + gender + '","' + birth_date + '","' + event_cost + '","' + transaction_total + '","' + address_postal_code + '","' + location + '","' + year + '","' + program_name + '","' + primary_key + '") '
            cursor.execute(park_sql)
            print(park_sql)

        db.commit()  # save the changes
        db.close()  # close the database
    except ValueError as err:
        print('An error occurred trying to decode the json text')
        print(err)
    except KeyError as err:
        print('Key not in data source')
        print(err)
    except HTTPError as err:
        print('Server could not fulfill the request.')
        print(err)
    except URLError as err:
        print('Failed to reach a server.')
        print(err)
    except sqlite3.IntegrityError as err:
        print('Integrity Error:', err)
    except sqlite3.OperationalError as err:
        print('Operational Error:', err)
    except sqlite3.Error as err:
        print('Error:', err)
    except Exception as err:
        print('An error occurred: ', err)


def insert_hank_anderson2017learn_to_play():
    try:
        dbname = 'youth_programs.db'
        db = sqlite3.connect(dbname)
        cursor = db.cursor()

        # ssl._create_default_https_context = ssl._create_unverified_context
        participants_file = '/Users/alex/Desktop/TU Youth Program CSVs/Hank Anderson Park/HankAnderson2017FallLearnToPlay.json'
        input_file = open(participants_file, 'r', encoding="utf8")
        participants_content = input_file.read()
        # The JSON parser returns a dictionary. The data that describes the parks is located in the 'data' entry.
        participants_dictionary = json.loads(participants_content)

        for participant in participants_dictionary:
            player_id = str(participant['id'])
            first_name = participant['first_name']
            last_name = participant['last_name']
            gender = participant['gender']
            birth_date = str(participant['birth_date'])
            event_cost = str(participant['event_cost'])
            transaction_total = str(participant['transaction_total'])
            address_postal_code = str(participant['postal_code'])
            location = "Hank Anderson"
            year = "2017"
            program_name = "HankAnderson2017LearnToPlay"
            primary_key = player_id + program_name
            # Constructs the SQL query to insert park information into the database
            park_sql = 'INSERT OR IGNORE INTO PARTICIPANTS VALUES ("' + player_id + '","' + first_name + '", " ' + last_name + '","' + gender + '","' + birth_date + '","' + event_cost + '","' + transaction_total + '","' + address_postal_code + '","' + location + '","' + year + '","' + program_name + '","' + primary_key + '") '
            cursor.execute(park_sql)
            print(park_sql)

        db.commit()  # save the changes
        db.close()  # close the database
    except ValueError as err:
        print('An error occurred trying to decode the json text')
        print(err)
    except KeyError as err:
        print('Key not in data source')
        print(err)
    except HTTPError as err:
        print('Server could not fulfill the request.')
        print(err)
    except URLError as err:
        print('Failed to reach a server.')
        print(err)
    except sqlite3.IntegrityError as err:
        print('Integrity Error:', err)
    except sqlite3.OperationalError as err:
        print('Operational Error:', err)
    except sqlite3.Error as err:
        print('Error:', err)
    except Exception as err:
        print('An error occurred: ', err)


def insert_hank_anderson2018learn_to_play_fall():
    try:
        dbname = 'youth_programs.db'
        db = sqlite3.connect(dbname)
        cursor = db.cursor()

        # ssl._create_default_https_context = ssl._create_unverified_context
        participants_file = '/Users/alex/Desktop/TU Youth Program CSVs/Hank Anderson Park/HankAnderson2018FallLearnToPlay.json'
        input_file = open(participants_file, 'r', encoding="utf8")
        participants_content = input_file.read()
        # The JSON parser returns a dictionary. The data that describes the parks is located in the 'data' entry.
        participants_dictionary = json.loads(participants_content)

        for participant in participants_dictionary:
            player_id = str(participant['id'])
            first_name = participant['first_name']
            last_name = participant['last_name']
            gender = participant['gender']
            birth_date = str(participant['birth_date'])
            event_cost = str(participant['event_cost'])
            transaction_total = str(participant['transaction_total'])
            address_postal_code = str(participant['postal_code'])
            location = "Hank Anderson"
            year = "2018"
            program_name = "HankAnderson2018LearnToPlayFall"
            primary_key = player_id + program_name
            # Constructs the SQL query to insert park information into the database
            park_sql = 'INSERT OR IGNORE INTO PARTICIPANTS VALUES ("' + player_id + '","' + first_name + '", " ' + last_name + '","' + gender + '","' + birth_date + '","' + event_cost + '","' + transaction_total + '","' + address_postal_code + '","' + location + '","' + year + '","' + program_name + '","' + primary_key + '") '
            cursor.execute(park_sql)
            print(park_sql)

        db.commit()  # save the changes
        db.close()  # close the database
    except ValueError as err:
        print('An error occurred trying to decode the json text')
        print(err)
    except KeyError as err:
        print('Key not in data source')
        print(err)
    except HTTPError as err:
        print('Server could not fulfill the request.')
        print(err)
    except URLError as err:
        print('Failed to reach a server.')
        print(err)
    except sqlite3.IntegrityError as err:
        print('Integrity Error:', err)
    except sqlite3.OperationalError as err:
        print('Operational Error:', err)
    except sqlite3.Error as err:
        print('Error:', err)
    except Exception as err:
        print('An error occurred: ', err)


def insert_hank_anderson2018learn_to_play_spring():
    try:
        dbname = 'youth_programs.db'
        db = sqlite3.connect(dbname)
        cursor = db.cursor()

        # ssl._create_default_https_context = ssl._create_unverified_context
        participants_file = '/Users/alex/Desktop/TU Youth Program CSVs/Hank Anderson Park/HankAnderson2018SpringLearnToPlay.json'
        input_file = open(participants_file, 'r', encoding="utf8")
        participants_content = input_file.read()
        # The JSON parser returns a dictionary. The data that describes the parks is located in the 'data' entry.
        participants_dictionary = json.loads(participants_content)

        for participant in participants_dictionary:
            player_id = str(participant['id'])
            first_name = participant['first_name']
            last_name = participant['last_name']
            gender = participant['gender']
            birth_date = str(participant['birth_date'])
            event_cost = str(participant['event_cost'])
            transaction_total = str(participant['transaction_total'])
            address_postal_code = str(participant['postal_code'])
            location = "Hank Anderson"
            year = "2018"
            program_name = "HankAnderson2018LearnToPlaySpring"
            primary_key = player_id + program_name
            # Constructs the SQL query to insert park information into the database
            park_sql = 'INSERT OR IGNORE INTO PARTICIPANTS VALUES ("' + player_id + '","' + first_name + '", " ' + last_name + '","' + gender + '","' + birth_date + '","' + event_cost + '","' + transaction_total + '","' + address_postal_code + '","' + location + '","' + year + '","' + program_name + '","' + primary_key + '") '
            cursor.execute(park_sql)
            print(park_sql)

        db.commit()  # save the changes
        db.close()  # close the database
    except ValueError as err:
        print('An error occurred trying to decode the json text')
        print(err)
    except KeyError as err:
        print('Key not in data source')
        print(err)
    except HTTPError as err:
        print('Server could not fulfill the request.')
        print(err)
    except URLError as err:
        print('Failed to reach a server.')
        print(err)
    except sqlite3.IntegrityError as err:
        print('Integrity Error:', err)
    except sqlite3.OperationalError as err:
        print('Operational Error:', err)
    except sqlite3.Error as err:
        print('Error:', err)
    except Exception as err:
        print('An error occurred: ', err)


def insert_hank_anderson2018learn_to_compete():
    try:
        dbname = 'youth_programs.db'
        db = sqlite3.connect(dbname)
        cursor = db.cursor()

        # ssl._create_default_https_context = ssl._create_unverified_context
        participants_file = '/Users/alex/Desktop/TU Youth Program CSVs/Hank Anderson Park/HankAnderson2018SpringLearnToCompete.json'
        input_file = open(participants_file, 'r', encoding="utf8")
        participants_content = input_file.read()
        # The JSON parser returns a dictionary. The data that describes the parks is located in the 'data' entry.
        participants_dictionary = json.loads(participants_content)

        for participant in participants_dictionary:
            player_id = str(participant['id'])
            first_name = participant['first_name']
            last_name = participant['last_name']
            gender = participant['gender']
            birth_date = str(participant['birth_date'])
            event_cost = str(participant['event_cost'])
            transaction_total = str(participant['transaction_total'])
            address_postal_code = str(participant['postal_code'])
            location = "Hank Anderson"
            year = "2018"
            program_name = "HankAnderson2018LearnToCompete"
            primary_key = player_id + program_name
            # Constructs the SQL query to insert park information into the database
            park_sql = 'INSERT OR IGNORE INTO PARTICIPANTS VALUES ("' + player_id + '","' + first_name + '", " ' + last_name + '","' + gender + '","' + birth_date + '","' + event_cost + '","' + transaction_total + '","' + address_postal_code + '","' + location + '","' + year + '","' + program_name + '","' + primary_key + '") '
            cursor.execute(park_sql)
            print(park_sql)

        db.commit()  # save the changes
        db.close()  # close the database
    except ValueError as err:
        print('An error occurred trying to decode the json text')
        print(err)
    except KeyError as err:
        print('Key not in data source')
        print(err)
    except HTTPError as err:
        print('Server could not fulfill the request.')
        print(err)
    except URLError as err:
        print('Failed to reach a server.')
        print(err)
    except sqlite3.IntegrityError as err:
        print('Integrity Error:', err)
    except sqlite3.OperationalError as err:
        print('Operational Error:', err)
    except sqlite3.Error as err:
        print('Error:', err)
    except Exception as err:
        print('An error occurred: ', err)


def insert_hank_anderson2021learn_to_play():
    try:
        dbname = 'youth_programs.db'
        db = sqlite3.connect(dbname)
        cursor = db.cursor()

        # ssl._create_default_https_context = ssl._create_unverified_context
        participants_file = '/Users/alex/Desktop/TU Youth Program CSVs/Hank Anderson Park/HankAnderson2021FallLearnToPlay.json'
        input_file = open(participants_file, 'r', encoding="utf8")
        participants_content = input_file.read()
        # The JSON parser returns a dictionary. The data that describes the parks is located in the 'data' entry.
        participants_dictionary = json.loads(participants_content)

        for participant in participants_dictionary:
            player_id = str(participant['id'])
            first_name = participant['first_name']
            last_name = participant['last_name']
            gender = participant['gender']
            birth_date = str(participant['birth_date'])
            event_cost = str(participant['event_cost'])
            transaction_total = str(participant['transaction_total'])
            address_postal_code = str(participant['postal_code'])
            location = "Hank Anderson"
            year = "2021"
            program_name = "HankAnderson2021LearnToPlay"
            primary_key = player_id + program_name
            # Constructs the SQL query to insert park information into the database
            park_sql = 'INSERT OR IGNORE INTO PARTICIPANTS VALUES ("' + player_id + '","' + first_name + '", " ' + last_name + '","' + gender + '","' + birth_date + '","' + event_cost + '","' + transaction_total + '","' + address_postal_code + '","' + location + '","' + year + '","' + program_name + '","' + primary_key + '") '
            cursor.execute(park_sql)
            print(park_sql)

        db.commit()  # save the changes
        db.close()  # close the database
    except ValueError as err:
        print('An error occurred trying to decode the json text')
        print(err)
    except KeyError as err:
        print('Key not in data source')
        print(err)
    except HTTPError as err:
        print('Server could not fulfill the request.')
        print(err)
    except URLError as err:
        print('Failed to reach a server.')
        print(err)
    except sqlite3.IntegrityError as err:
        print('Integrity Error:', err)
    except sqlite3.OperationalError as err:
        print('Operational Error:', err)
    except sqlite3.Error as err:
        print('Error:', err)
    except Exception as err:
        print('An error occurred: ', err)


def insert_hank_anderson2021rec_league():
    try:
        dbname = 'youth_programs.db'
        db = sqlite3.connect(dbname)
        cursor = db.cursor()

        # ssl._create_default_https_context = ssl._create_unverified_context
        participants_file = '/Users/alex/Desktop/TU Youth Program CSVs/Hank Anderson Park/HankAnderson2021FallRecLeague.json'
        input_file = open(participants_file, 'r', encoding="utf8")
        participants_content = input_file.read()
        # The JSON parser returns a dictionary. The data that describes the parks is located in the 'data' entry.
        participants_dictionary = json.loads(participants_content)

        for participant in participants_dictionary:
            player_id = str(participant['id'])
            first_name = participant['first_name']
            last_name = participant['last_name']
            gender = participant['gender']
            birth_date = str(participant['birth_date'])
            event_cost = str(participant['event_cost'])
            transaction_total = str(participant['transaction_total'])
            address_postal_code = str(participant['postal_code'])
            location = "Hank Anderson"
            year = "2021"
            program_name = "HankAnderson2021RecLeague"
            primary_key = player_id + program_name
            # Constructs the SQL query to insert park information into the database
            park_sql = 'INSERT OR IGNORE INTO PARTICIPANTS VALUES ("' + player_id + '","' + first_name + '", " ' + last_name + '","' + gender + '","' + birth_date + '","' + event_cost + '","' + transaction_total + '","' + address_postal_code + '","' + location + '","' + year + '","' + program_name + '","' + primary_key + '") '
            cursor.execute(park_sql)
            print(park_sql)

        db.commit()  # save the changes
        db.close()  # close the database
    except ValueError as err:
        print('An error occurred trying to decode the json text')
        print(err)
    except KeyError as err:
        print('Key not in data source')
        print(err)
    except HTTPError as err:
        print('Server could not fulfill the request.')
        print(err)
    except URLError as err:
        print('Failed to reach a server.')
        print(err)
    except sqlite3.IntegrityError as err:
        print('Integrity Error:', err)
    except sqlite3.OperationalError as err:
        print('Operational Error:', err)
    except sqlite3.Error as err:
        print('Error:', err)
    except Exception as err:
        print('An error occurred: ', err)


def insert_cedar_falls_2018_gum():
    try:
        dbname = 'youth_programs.db'
        db = sqlite3.connect(dbname)
        cursor = db.cursor()

        # ssl._create_default_https_context = ssl._create_unverified_context
        participants_file = '/Users/alex/Desktop/TU Youth Program CSVs/Cedar Falls/CedarFalls2018GUM.json'
        input_file = open(participants_file, 'r', encoding="utf8")
        participants_content = input_file.read()
        # The JSON parser returns a dictionary. The data that describes the parks is located in the 'data' entry.
        participants_dictionary = json.loads(participants_content)

        for participant in participants_dictionary:
            player_id = str(participant['id'])
            first_name = participant['first_name']
            last_name = participant['last_name']
            gender = participant['gender']
            birth_date = str(participant['birth_date'])
            event_cost = str(participant['event_cost'])
            transaction_total = str(participant['transaction_total'])
            address_postal_code = str(participant['postal_code'])
            location = "Cedar Falls"
            year = "2018"
            program_name = "CedarFalls2018GUM"
            primary_key = player_id + program_name
            # Constructs the SQL query to insert park information into the database
            park_sql = 'INSERT OR IGNORE INTO PARTICIPANTS VALUES ("' + player_id + '","' + first_name + '", " ' + last_name + '","' + gender + '","' + birth_date + '","' + event_cost + '","' + transaction_total + '","' + address_postal_code + '","' + location + '","' + year + '","' + program_name + '","' + primary_key + '") '
            cursor.execute(park_sql)
            print(park_sql)

        db.commit()  # save the changes
        db.close()  # close the database
    except ValueError as err:
        print('An error occurred trying to decode the json text')
        print(err)
    except KeyError as err:
        print('Key not in data source')
        print(err)
    except HTTPError as err:
        print('Server could not fulfill the request.')
        print(err)
    except URLError as err:
        print('Failed to reach a server.')
        print(err)
    except sqlite3.IntegrityError as err:
        print('Integrity Error:', err)
    except sqlite3.OperationalError as err:
        print('Operational Error:', err)
    except sqlite3.Error as err:
        print('Error:', err)
    except Exception as err:
        print('An error occurred: ', err)


def insert_cfs2018middle_school_clinic():
    try:
        dbname = 'youth_programs.db'
        db = sqlite3.connect(dbname)
        cursor = db.cursor()

        # ssl._create_default_https_context = ssl._create_unverified_context
        participants_file = '/Users/alex/Desktop/TU Youth Program CSVs/CFS/CFS2018MiddleSchoolClinic.json'
        input_file = open(participants_file, 'r', encoding="utf8")
        participants_content = input_file.read()
        # The JSON parser returns a dictionary. The data that describes the parks is located in the 'data' entry.
        participants_dictionary = json.loads(participants_content)

        for participant in participants_dictionary:
            player_id = str(participant['id'])
            first_name = participant['first_name']
            last_name = participant['last_name']
            gender = participant['gender']
            birth_date = str(participant['birth_date'])
            event_cost = str(participant['event_cost'])
            transaction_total = str(participant['transaction_total'])
            address_postal_code = str(participant['postal_code'])
            location = "CFS"
            year = "2018"
            program_name = "CFS2018MiddleSchoolClinic"
            primary_key = player_id + program_name
            # Constructs the SQL query to insert park information into the database
            park_sql = 'INSERT OR IGNORE INTO PARTICIPANTS VALUES ("' + player_id + '","' + first_name + '", " ' + last_name + '","' + gender + '","' + birth_date + '","' + event_cost + '","' + transaction_total + '","' + address_postal_code + '","' + location + '","' + year + '","' + program_name + '","' + primary_key + '") '
            cursor.execute(park_sql)
            print(park_sql)

        db.commit()  # save the changes
        db.close()  # close the database
    except ValueError as err:
        print('An error occurred trying to decode the json text')
        print(err)
    except KeyError as err:
        print('Key not in data source')
        print(err)
    except HTTPError as err:
        print('Server could not fulfill the request.')
        print(err)
    except URLError as err:
        print('Failed to reach a server.')
        print(err)
    except sqlite3.IntegrityError as err:
        print('Integrity Error:', err)
    except sqlite3.OperationalError as err:
        print('Operational Error:', err)
    except sqlite3.Error as err:
        print('Error:', err)
    except Exception as err:
        print('An error occurred: ', err)


def insert_cfs2017middle_school_clinic():
    try:
        dbname = 'youth_programs.db'
        db = sqlite3.connect(dbname)
        cursor = db.cursor()

        # ssl._create_default_https_context = ssl._create_unverified_context
        participants_file = '/Users/alex/Desktop/TU Youth Program CSVs/CFS/CFS2017MiddleSchoolClinic.json'
        input_file = open(participants_file, 'r', encoding="utf8")
        participants_content = input_file.read()
        # The JSON parser returns a dictionary. The data that describes the parks is located in the 'data' entry.
        participants_dictionary = json.loads(participants_content)

        for participant in participants_dictionary:
            player_id = str(participant['id'])
            first_name = participant['first_name']
            last_name = participant['last_name']
            gender = participant['gender']
            birth_date = str(participant['birth_date'])
            event_cost = str(participant['event_cost'])
            transaction_total = str(participant['transaction_total'])
            address_postal_code = str(participant['postal_code'])
            location = "CFS"
            year = "2017"
            program_name = "CFS2017MiddleSchoolClinic"
            primary_key = player_id + program_name
            # Constructs the SQL query to insert park information into the database
            park_sql = 'INSERT OR IGNORE INTO PARTICIPANTS VALUES ("' + player_id + '","' + first_name + '", " ' + last_name + '","' + gender + '","' + birth_date + '","' + event_cost + '","' + transaction_total + '","' + address_postal_code + '","' + location + '","' + year + '","' + program_name + '","' + primary_key + '") '
            cursor.execute(park_sql)
            print(park_sql)

        db.commit()  # save the changes
        db.close()  # close the database
    except ValueError as err:
        print('An error occurred trying to decode the json text')
        print(err)
    except KeyError as err:
        print('Key not in data source')
        print(err)
    except HTTPError as err:
        print('Server could not fulfill the request.')
        print(err)
    except URLError as err:
        print('Failed to reach a server.')
        print(err)
    except sqlite3.IntegrityError as err:
        print('Integrity Error:', err)
    except sqlite3.OperationalError as err:
        print('Operational Error:', err)
    except sqlite3.Error as err:
        print('Error:', err)
    except Exception as err:
        print('An error occurred: ', err)


def insert_mac2018summer_league():
    try:
        dbname = 'youth_programs.db'
        db = sqlite3.connect(dbname)
        cursor = db.cursor()

        # ssl._create_default_https_context = ssl._create_unverified_context
        participants_file = '/Users/alex/Desktop/TU Youth Program CSVs/MAC Fields/MAC2018SummerLeague.json'
        input_file = open(participants_file, 'r', encoding="utf8")
        participants_content = input_file.read()
        # The JSON parser returns a dictionary. The data that describes the parks is located in the 'data' entry.
        participants_dictionary = json.loads(participants_content)

        for participant in participants_dictionary:
            player_id = str(participant['id'])
            first_name = participant['first_name']
            last_name = participant['last_name']
            gender = participant['gender']
            birth_date = str(participant['birth_date'])
            event_cost = str(participant['event_cost'])
            transaction_total = str(participant['transaction_total'])
            address_postal_code = str(participant['postal_code'])
            location = "MAC"
            year = "2018"
            program_name = "MAC2018SummerLeague"
            primary_key = player_id + program_name
            # Constructs the SQL query to insert park information into the database
            park_sql = 'INSERT OR IGNORE INTO PARTICIPANTS VALUES ("' + player_id + '","' + first_name + '", " ' + last_name + '","' + gender + '","' + birth_date + '","' + event_cost + '","' + transaction_total + '","' + address_postal_code + '","' + location + '","' + year + '","' + program_name + '","' + primary_key + '") '
            cursor.execute(park_sql)
            print(park_sql)

        db.commit()  # save the changes
        db.close()  # close the database
    except ValueError as err:
        print('An error occurred trying to decode the json text')
        print(err)
    except KeyError as err:
        print('Key not in data source')
        print(err)
    except HTTPError as err:
        print('Server could not fulfill the request.')
        print(err)
    except URLError as err:
        print('Failed to reach a server.')
        print(err)
    except sqlite3.IntegrityError as err:
        print('Integrity Error:', err)
    except sqlite3.OperationalError as err:
        print('Operational Error:', err)
    except sqlite3.Error as err:
        print('Error:', err)
    except Exception as err:
        print('An error occurred: ', err)


def insert_laurel_hills_2018_learn_to_play():
    try:
        dbname = 'youth_programs.db'
        db = sqlite3.connect(dbname)
        cursor = db.cursor()

        # ssl._create_default_https_context = ssl._create_unverified_context
        participants_file = '/Users/alex/Desktop/TU Youth Program CSVs/Laurel Hills/LaurelHills2018FallLearnToPlay.json'
        input_file = open(participants_file, 'r', encoding="utf8")
        participants_content = input_file.read()
        # The JSON parser returns a dictionary. The data that describes the parks is located in the 'data' entry.
        participants_dictionary = json.loads(participants_content)

        for participant in participants_dictionary:
            player_id = str(participant['id'])
            first_name = participant['first_name']
            last_name = participant['last_name']
            gender = participant['gender']
            birth_date = str(participant['birth_date'])
            event_cost = str(participant['event_cost'])
            transaction_total = str(participant['transaction_total'])
            address_postal_code = str(participant['postal_code'])
            location = "Laurel Hills"
            year = "2018"
            program_name = "LaurelHills2018FallLearnToPlay"
            primary_key = player_id + program_name
            # Constructs the SQL query to insert park information into the database
            park_sql = 'INSERT OR IGNORE INTO PARTICIPANTS VALUES ("' + player_id + '","' + first_name + '", " ' + last_name + '","' + gender + '","' + birth_date + '","' + event_cost + '","' + transaction_total + '","' + address_postal_code + '","' + location + '","' + year + '","' + program_name + '","' + primary_key + '") '
            cursor.execute(park_sql)
            print(park_sql)

        db.commit()  # save the changes
        db.close()  # close the database
    except ValueError as err:
        print('An error occurred trying to decode the json text')
        print(err)
    except KeyError as err:
        print('Key not in data source')
        print(err)
    except HTTPError as err:
        print('Server could not fulfill the request.')
        print(err)
    except URLError as err:
        print('Failed to reach a server.')
        print(err)
    except sqlite3.IntegrityError as err:
        print('Integrity Error:', err)
    except sqlite3.OperationalError as err:
        print('Operational Error:', err)
    except sqlite3.Error as err:
        print('Error:', err)
    except Exception as err:
        print('An error occurred: ', err)


def insert_laurel_hills2019learn_to_play():
    try:
        dbname = 'youth_programs.db'
        db = sqlite3.connect(dbname)
        cursor = db.cursor()

        # ssl._create_default_https_context = ssl._create_unverified_context
        participants_file = '/Users/alex/Desktop/TU Youth Program CSVs/Laurel Hills/LaurelHills2019SpringLearnToPlay.json'
        input_file = open(participants_file, 'r', encoding="utf8")
        participants_content = input_file.read()
        # The JSON parser returns a dictionary. The data that describes the parks is located in the 'data' entry.
        participants_dictionary = json.loads(participants_content)

        for participant in participants_dictionary:
            player_id = str(participant['id'])
            first_name = participant['first_name']
            last_name = participant['last_name']
            gender = participant['gender']
            birth_date = str(participant['birth_date'])
            event_cost = str(participant['event_cost'])
            transaction_total = str(participant['transaction_total'])
            address_postal_code = str(participant['postal_code'])
            location = "Laurel Hills"
            year = "2019"
            program_name = "LaurelHills2019LearnToPlay"
            primary_key = player_id + program_name
            # Constructs the SQL query to insert park information into the database
            park_sql = 'INSERT OR IGNORE INTO PARTICIPANTS VALUES ("' + player_id + '","' + first_name + '", " ' + last_name + '","' + gender + '","' + birth_date + '","' + event_cost + '","' + transaction_total + '","' + address_postal_code + '","' + location + '","' + year + '","' + program_name + '","' + primary_key + '") '
            cursor.execute(park_sql)
            print(park_sql)

        db.commit()  # save the changes
        db.close()  # close the database
    except ValueError as err:
        print('An error occurred trying to decode the json text')
        print(err)
    except KeyError as err:
        print('Key not in data source')
        print(err)
    except HTTPError as err:
        print('Server could not fulfill the request.')
        print(err)
    except URLError as err:
        print('Failed to reach a server.')
        print(err)
    except sqlite3.IntegrityError as err:
        print('Integrity Error:', err)
    except sqlite3.OperationalError as err:
        print('Operational Error:', err)
    except sqlite3.Error as err:
        print('Error:', err)
    except Exception as err:
        print('An error occurred: ', err)


def insert_east_durham2018learn_to_play():
    try:
        dbname = 'youth_programs.db'
        db = sqlite3.connect(dbname)
        cursor = db.cursor()

        # ssl._create_default_https_context = ssl._create_unverified_context
        participants_file = '/Users/alex/Desktop/TU Youth Program CSVs/East Durham Park/EastDurham2018SpringLearnToPlay.json'
        input_file = open(participants_file, 'r', encoding="utf8")
        participants_content = input_file.read()
        # The JSON parser returns a dictionary. The data that describes the parks is located in the 'data' entry.
        participants_dictionary = json.loads(participants_content)

        for participant in participants_dictionary:
            player_id = str(participant['id'])
            first_name = participant['first_name']
            last_name = participant['last_name']
            gender = participant['gender']
            birth_date = str(participant['birth_date'])
            event_cost = str(participant['event_cost'])
            transaction_total = str(participant['transaction_total'])
            address_postal_code = str(participant['postal_code'])
            location = "East Durham Park"
            year = "2018"
            program_name = "EastDurham2018LearnToPlay"
            primary_key = player_id + program_name
            # Constructs the SQL query to insert park information into the database
            park_sql = 'INSERT OR IGNORE INTO PARTICIPANTS VALUES ("' + player_id + '","' + first_name + '", " ' + last_name + '","' + gender + '","' + birth_date + '","' + event_cost + '","' + transaction_total + '","' + address_postal_code + '","' + location + '","' + year + '","' + program_name + '","' + primary_key + '") '
            cursor.execute(park_sql)
            print(park_sql)

        db.commit()  # save the changes
        db.close()  # close the database
    except ValueError as err:
        print('An error occurred trying to decode the json text')
        print(err)
    except KeyError as err:
        print('Key not in data source')
        print(err)
    except HTTPError as err:
        print('Server could not fulfill the request.')
        print(err)
    except URLError as err:
        print('Failed to reach a server.')
        print(err)
    except sqlite3.IntegrityError as err:
        print('Integrity Error:', err)
    except sqlite3.OperationalError as err:
        print('Operational Error:', err)
    except sqlite3.Error as err:
        print('Error:', err)
    except Exception as err:
        print('An error occurred: ', err)


def insert_east_durham2019learn_to_play():
    try:
        dbname = 'youth_programs.db'
        db = sqlite3.connect(dbname)
        cursor = db.cursor()

        # ssl._create_default_https_context = ssl._create_unverified_context
        participants_file = '/Users/alex/Desktop/TU Youth Program CSVs/East Durham Park/EastDurham2019SpringLearnToPlay.json'
        input_file = open(participants_file, 'r', encoding="utf8")
        participants_content = input_file.read()
        # The JSON parser returns a dictionary. The data that describes the parks is located in the 'data' entry.
        participants_dictionary = json.loads(participants_content)

        for participant in participants_dictionary:
            player_id = str(participant['id'])
            first_name = participant['first_name']
            last_name = participant['last_name']
            gender = participant['gender']
            birth_date = str(participant['birth_date'])
            event_cost = str(participant['event_cost'])
            transaction_total = str(participant['transaction_total'])
            address_postal_code = str(participant['postal_code'])
            location = "East Durham Park"
            year = "2019"
            program_name = "EastDurham2019LearnToPlay"
            primary_key = player_id + program_name
            # Constructs the SQL query to insert park information into the database
            park_sql = 'INSERT OR IGNORE INTO PARTICIPANTS VALUES ("' + player_id + '","' + first_name + '", " ' + last_name + '","' + gender + '","' + birth_date + '","' + event_cost + '","' + transaction_total + '","' + address_postal_code + '","' + location + '","' + year + '","' + program_name + '","' + primary_key + '") '
            cursor.execute(park_sql)
            print(park_sql)

        db.commit()  # save the changes
        db.close()  # close the database
    except ValueError as err:
        print('An error occurred trying to decode the json text')
        print(err)
    except KeyError as err:
        print('Key not in data source')
        print(err)
    except HTTPError as err:
        print('Server could not fulfill the request.')
        print(err)
    except URLError as err:
        print('Failed to reach a server.')
        print(err)
    except sqlite3.IntegrityError as err:
        print('Integrity Error:', err)
    except sqlite3.OperationalError as err:
        print('Operational Error:', err)
    except sqlite3.Error as err:
        print('Error:', err)
    except Exception as err:
        print('An error occurred: ', err)


def insert_heritage2018learn_to_play():
    try:
        dbname = 'youth_programs.db'
        db = sqlite3.connect(dbname)
        cursor = db.cursor()

        # ssl._create_default_https_context = ssl._create_unverified_context
        participants_file = '/Users/alex/Desktop/TU Youth Program CSVs/Heritage High School/Heritage2018FallLearnToPlay.json'
        input_file = open(participants_file, 'r', encoding="utf8")
        participants_content = input_file.read()
        # The JSON parser returns a dictionary. The data that describes the parks is located in the 'data' entry.
        participants_dictionary = json.loads(participants_content)

        for participant in participants_dictionary:
            player_id = str(participant['id'])
            first_name = participant['first_name']
            last_name = participant['last_name']
            gender = participant['gender']
            birth_date = str(participant['birth_date'])
            event_cost = str(participant['event_cost'])
            transaction_total = str(participant['transaction_total'])
            address_postal_code = str(participant['postal_code'])
            location = "Heritage High School"
            year = "2018"
            program_name = "Heritage2018LearnToPlay"
            primary_key = player_id + program_name
            # Constructs the SQL query to insert park information into the database
            park_sql = 'INSERT OR IGNORE INTO PARTICIPANTS VALUES ("' + player_id + '","' + first_name + '", " ' + last_name + '","' + gender + '","' + birth_date + '","' + event_cost + '","' + transaction_total + '","' + address_postal_code + '","' + location + '","' + year + '","' + program_name + '","' + primary_key + '") '
            cursor.execute(park_sql)
            print(park_sql)

        db.commit()  # save the changes
        db.close()  # close the database
    except ValueError as err:
        print('An error occurred trying to decode the json text')
        print(err)
    except KeyError as err:
        print('Key not in data source')
        print(err)
    except HTTPError as err:
        print('Server could not fulfill the request.')
        print(err)
    except URLError as err:
        print('Failed to reach a server.')
        print(err)
    except sqlite3.IntegrityError as err:
        print('Integrity Error:', err)
    except sqlite3.OperationalError as err:
        print('Operational Error:', err)
    except sqlite3.Error as err:
        print('Error:', err)
    except Exception as err:
        print('An error occurred: ', err)


def insert_homestead2019learn_to_play():
    try:
        dbname = 'youth_programs.db'
        db = sqlite3.connect(dbname)
        cursor = db.cursor()

        # ssl._create_default_https_context = ssl._create_unverified_context
        participants_file = '/Users/alex/Desktop/TU Youth Program CSVs/Homestead/Homestead2019SpringLearnToPlay.json'
        input_file = open(participants_file, 'r', encoding="utf8")
        participants_content = input_file.read()
        # The JSON parser returns a dictionary. The data that describes the parks is located in the 'data' entry.
        participants_dictionary = json.loads(participants_content)

        for participant in participants_dictionary:
            player_id = str(participant['id'])
            first_name = participant['first_name']
            last_name = participant['last_name']
            gender = participant['gender']
            birth_date = str(participant['birth_date'])
            event_cost = str(participant['event_cost'])
            transaction_total = str(participant['transaction_total'])
            address_postal_code = str(participant['postal_code'])
            location = "Homestead"
            year = "2019"
            program_name = "Homestead2019LearnToPlay"
            primary_key = player_id + program_name
            # Constructs the SQL query to insert park information into the database
            park_sql = 'INSERT OR IGNORE INTO PARTICIPANTS VALUES ("' + player_id + '","' + first_name + '", " ' + last_name + '","' + gender + '","' + birth_date + '","' + event_cost + '","' + transaction_total + '","' + address_postal_code + '","' + location + '","' + year + '","' + program_name + '","' + primary_key + '") '
            cursor.execute(park_sql)
            print(park_sql)

        db.commit()  # save the changes
        db.close()  # close the database
    except ValueError as err:
        print('An error occurred trying to decode the json text')
        print(err)
    except KeyError as err:
        print('Key not in data source')
        print(err)
    except HTTPError as err:
        print('Server could not fulfill the request.')
        print(err)
    except URLError as err:
        print('Failed to reach a server.')
        print(err)
    except sqlite3.IntegrityError as err:
        print('Integrity Error:', err)
    except sqlite3.OperationalError as err:
        print('Operational Error:', err)
    except sqlite3.Error as err:
        print('Error:', err)
    except Exception as err:
        print('An error occurred: ', err)


def insert_wake_forest2019learn_to_play():
    try:
        dbname = 'youth_programs.db'
        db = sqlite3.connect(dbname)
        cursor = db.cursor()

        # ssl._create_default_https_context = ssl._create_unverified_context
        participants_file = '/Users/alex/Desktop/TU Youth Program CSVs/Wake Forest Middle School/WakeForest2019SpringLearnToPlay.json'
        input_file = open(participants_file, 'r', encoding="utf8")
        participants_content = input_file.read()
        # The JSON parser returns a dictionary. The data that describes the parks is located in the 'data' entry.
        participants_dictionary = json.loads(participants_content)

        for participant in participants_dictionary:
            player_id = str(participant['id'])
            first_name = participant['first_name']
            last_name = participant['last_name']
            gender = participant['gender']
            birth_date = str(participant['birth_date'])
            event_cost = str(participant['event_cost'])
            transaction_total = str(participant['transaction_total'])
            address_postal_code = str(participant['postal_code'])
            location = "Wake Forest Middle School"
            year = "2019"
            program_name = "WakeForest2019LearnToPlay"
            primary_key = player_id + program_name
            # Constructs the SQL query to insert park information into the database
            park_sql = 'INSERT OR IGNORE INTO PARTICIPANTS VALUES ("' + player_id + '","' + first_name + '", " ' + last_name + '","' + gender + '","' + birth_date + '","' + event_cost + '","' + transaction_total + '","' + address_postal_code + '","' + location + '","' + year + '","' + program_name + '","' + primary_key + '") '
            cursor.execute(park_sql)
            print(park_sql)

        db.commit()  # save the changes
        db.close()  # close the database
    except ValueError as err:
        print('An error occurred trying to decode the json text')
        print(err)
    except KeyError as err:
        print('Key not in data source')
        print(err)
    except HTTPError as err:
        print('Server could not fulfill the request.')
        print(err)
    except URLError as err:
        print('Failed to reach a server.')
        print(err)
    except sqlite3.IntegrityError as err:
        print('Integrity Error:', err)
    except sqlite3.OperationalError as err:
        print('Operational Error:', err)
    except sqlite3.Error as err:
        print('Error:', err)
    except Exception as err:
        print('An error occurred: ', err)


def insert_cedar_forks2019summer_league_girls():
    try:
        dbname = 'youth_programs.db'
        db = sqlite3.connect(dbname)
        cursor = db.cursor()

        # ssl._create_default_https_context = ssl._create_unverified_context
        participants_file = '/Users/alex/Desktop/TU Youth Program CSVs/Cedar Forks/CedarForks2019SummerLeagueGirls.json'
        input_file = open(participants_file, 'r', encoding="utf8")
        participants_content = input_file.read()
        # The JSON parser returns a dictionary. The data that describes the parks is located in the 'data' entry.
        participants_dictionary = json.loads(participants_content)

        for participant in participants_dictionary:
            player_id = str(participant['id'])
            first_name = participant['first_name']
            last_name = participant['last_name']
            gender = participant['gender']
            birth_date = str(participant['birth_date'])
            event_cost = str(participant['event_cost'])
            transaction_total = str(participant['transaction_total'])
            address_postal_code = str(participant['postal_code'])
            location = "Cedar Forks"
            year = "2019"
            program_name = "CedarForks2019SummerLeagueGirls"
            primary_key = player_id + program_name
            # Constructs the SQL query to insert park information into the database
            park_sql = 'INSERT OR IGNORE INTO PARTICIPANTS VALUES ("' + player_id + '","' + first_name + '", " ' + last_name + '","' + gender + '","' + birth_date + '","' + event_cost + '","' + transaction_total + '","' + address_postal_code + '","' + location + '","' + year + '","' + program_name + '","' + primary_key + '") '
            cursor.execute(park_sql)
            print(park_sql)

        db.commit()  # save the changes
        db.close()  # close the database
    except ValueError as err:
        print('An error occurred trying to decode the json text')
        print(err)
    except KeyError as err:
        print('Key not in data source')
        print(err)
    except HTTPError as err:
        print('Server could not fulfill the request.')
        print(err)
    except URLError as err:
        print('Failed to reach a server.')
        print(err)
    except sqlite3.IntegrityError as err:
        print('Integrity Error:', err)
    except sqlite3.OperationalError as err:
        print('Operational Error:', err)
    except sqlite3.Error as err:
        print('Error:', err)
    except Exception as err:
        print('An error occurred: ', err)


def insert_cedar_forks2019summer_league():
    try:
        dbname = 'youth_programs.db'
        db = sqlite3.connect(dbname)
        cursor = db.cursor()

        # ssl._create_default_https_context = ssl._create_unverified_context
        participants_file = '/Users/alex/Desktop/TU Youth Program CSVs/Cedar Forks/CedarForks2019SummerLeagueEast.json'
        input_file = open(participants_file, 'r', encoding="utf8")
        participants_content = input_file.read()
        # The JSON parser returns a dictionary. The data that describes the parks is located in the 'data' entry.
        participants_dictionary = json.loads(participants_content)

        for participant in participants_dictionary:
            player_id = str(participant['id'])
            first_name = participant['first_name']
            last_name = participant['last_name']
            gender = participant['gender']
            birth_date = str(participant['birth_date'])
            event_cost = str(participant['event_cost'])
            transaction_total = str(participant['transaction_total'])
            address_postal_code = str(participant['postal_code'])
            location = "Cedar Forks"
            year = "2019"
            program_name = "CedarForks2019SummerLeague"
            primary_key = player_id + program_name
            # Constructs the SQL query to insert park information into the database
            park_sql = 'INSERT OR IGNORE INTO PARTICIPANTS VALUES ("' + player_id + '","' + first_name + '", " ' + last_name + '","' + gender + '","' + birth_date + '","' + event_cost + '","' + transaction_total + '","' + address_postal_code + '","' + location + '","' + year + '","' + program_name + '","' + primary_key + '") '
            cursor.execute(park_sql)
            print(park_sql)

        db.commit()  # save the changes
        db.close()  # close the database
    except ValueError as err:
        print('An error occurred trying to decode the json text')
        print(err)
    except KeyError as err:
        print('Key not in data source')
        print(err)
    except HTTPError as err:
        print('Server could not fulfill the request.')
        print(err)
    except URLError as err:
        print('Failed to reach a server.')
        print(err)
    except sqlite3.IntegrityError as err:
        print('Integrity Error:', err)
    except sqlite3.OperationalError as err:
        print('Operational Error:', err)
    except sqlite3.Error as err:
        print('Error:', err)
    except Exception as err:
        print('An error occurred: ', err)


def insert_cedar_forks2021learn_to_play():
    try:
        dbname = 'youth_programs.db'
        db = sqlite3.connect(dbname)
        cursor = db.cursor()

        # ssl._create_default_https_context = ssl._create_unverified_context
        participants_file = '/Users/alex/Desktop/TU Youth Program CSVs/Cedar Forks/CedarForks2021LearnToPlay.json'
        input_file = open(participants_file, 'r', encoding="utf8")
        participants_content = input_file.read()
        # The JSON parser returns a dictionary. The data that describes the parks is located in the 'data' entry.
        participants_dictionary = json.loads(participants_content)

        for participant in participants_dictionary:
            player_id = str(participant['id'])
            first_name = participant['first_name']
            last_name = participant['last_name']
            gender = participant['gender']
            birth_date = str(participant['birth_date'])
            event_cost = str(participant['event_cost'])
            transaction_total = str(participant['transaction_total'])
            address_postal_code = str(participant['postal_code'])
            location = "Cedar Forks"
            year = "2021"
            program_name = "CedarForks2021LearnToPlay"
            primary_key = player_id + program_name
            # Constructs the SQL query to insert park information into the database
            park_sql = 'INSERT OR IGNORE INTO PARTICIPANTS VALUES ("' + player_id + '","' + first_name + '", " ' + last_name + '","' + gender + '","' + birth_date + '","' + event_cost + '","' + transaction_total + '","' + address_postal_code + '","' + location + '","' + year + '","' + program_name + '","' + primary_key + '") '
            cursor.execute(park_sql)
            print(park_sql)

        db.commit()  # save the changes
        db.close()  # close the database
    except ValueError as err:
        print('An error occurred trying to decode the json text')
        print(err)
    except KeyError as err:
        print('Key not in data source')
        print(err)
    except HTTPError as err:
        print('Server could not fulfill the request.')
        print(err)
    except URLError as err:
        print('Failed to reach a server.')
        print(err)
    except sqlite3.IntegrityError as err:
        print('Integrity Error:', err)
    except sqlite3.OperationalError as err:
        print('Operational Error:', err)
    except sqlite3.Error as err:
        print('Error:', err)
    except Exception as err:
        print('An error occurred: ', err)


def insert_cedar_forks2021rec_league():
    try:
        dbname = 'youth_programs.db'
        db = sqlite3.connect(dbname)
        cursor = db.cursor()

        # ssl._create_default_https_context = ssl._create_unverified_context
        participants_file = '/Users/alex/Desktop/TU Youth Program CSVs/Cedar Forks/CedarForks2021RecLeague.json'
        input_file = open(participants_file, 'r', encoding="utf8")
        participants_content = input_file.read()
        # The JSON parser returns a dictionary. The data that describes the parks is located in the 'data' entry.
        participants_dictionary = json.loads(participants_content)

        for participant in participants_dictionary:
            player_id = str(participant['id'])
            first_name = participant['first_name']
            last_name = participant['last_name']
            gender = participant['gender']
            birth_date = str(participant['birth_date'])
            event_cost = str(participant['event_cost'])
            transaction_total = str(participant['transaction_total'])
            address_postal_code = str(participant['postal_code'])
            location = "Cedar Forks"
            year = "2021"
            program_name = "CedarForks2021RecLeague"
            primary_key = player_id + program_name
            # Constructs the SQL query to insert park information into the database
            park_sql = 'INSERT OR IGNORE INTO PARTICIPANTS VALUES ("' + player_id + '","' + first_name + '", " ' + last_name + '","' + gender + '","' + birth_date + '","' + event_cost + '","' + transaction_total + '","' + address_postal_code + '","' + location + '","' + year + '","' + program_name + '","' + primary_key + '") '
            cursor.execute(park_sql)
            print(park_sql)

        db.commit()  # save the changes
        db.close()  # close the database
    except ValueError as err:
        print('An error occurred trying to decode the json text')
        print(err)
    except KeyError as err:
        print('Key not in data source')
        print(err)
    except HTTPError as err:
        print('Server could not fulfill the request.')
        print(err)
    except URLError as err:
        print('Failed to reach a server.')
        print(err)
    except sqlite3.IntegrityError as err:
        print('Integrity Error:', err)
    except sqlite3.OperationalError as err:
        print('Operational Error:', err)
    except sqlite3.Error as err:
        print('Error:', err)
    except Exception as err:
        print('An error occurred: ', err)


def insert_cedar_forks2021ycc():
    try:
        dbname = 'youth_programs.db'
        db = sqlite3.connect(dbname)
        cursor = db.cursor()

        # ssl._create_default_https_context = ssl._create_unverified_context
        participants_file = '/Users/alex/Desktop/TU Youth Program CSVs/Cedar Forks/CedarForks2021YCCs.json'
        input_file = open(participants_file, 'r', encoding="utf8")
        participants_content = input_file.read()
        # The JSON parser returns a dictionary. The data that describes the parks is located in the 'data' entry.
        participants_dictionary = json.loads(participants_content)

        for participant in participants_dictionary:
            player_id = str(participant['id'])
            first_name = participant['first_name']
            last_name = participant['last_name']
            gender = participant['gender']
            birth_date = str(participant['birth_date'])
            event_cost = str(participant['event_cost'])
            transaction_total = str(participant['transaction_total'])
            address_postal_code = str(participant['postal_code'])
            location = "Cedar Forks"
            year = "2021"
            program_name = "CedarForks2021YCCs"
            primary_key = player_id + program_name
            # Constructs the SQL query to insert park information into the database
            park_sql = 'INSERT OR IGNORE INTO PARTICIPANTS VALUES ("' + player_id + '","' + first_name + '", " ' + last_name + '","' + gender + '","' + birth_date + '","' + event_cost + '","' + transaction_total + '","' + address_postal_code + '","' + location + '","' + year + '","' + program_name + '","' + primary_key + '") '
            cursor.execute(park_sql)
            print(park_sql)

        db.commit()  # save the changes
        db.close()  # close the database
    except ValueError as err:
        print('An error occurred trying to decode the json text')
        print(err)
    except KeyError as err:
        print('Key not in data source')
        print(err)
    except HTTPError as err:
        print('Server could not fulfill the request.')
        print(err)
    except URLError as err:
        print('Failed to reach a server.')
        print(err)
    except sqlite3.IntegrityError as err:
        print('Integrity Error:', err)
    except sqlite3.OperationalError as err:
        print('Operational Error:', err)
    except sqlite3.Error as err:
        print('Error:', err)
    except Exception as err:
        print('An error occurred: ', err)


def insert_chapel_hill_bible_church2019summer_league():
    try:
        dbname = 'youth_programs.db'
        db = sqlite3.connect(dbname)
        cursor = db.cursor()

        # ssl._create_default_https_context = ssl._create_unverified_context
        participants_file = '/Users/alex/Desktop/TU Youth Program CSVs/Chapel Hill Bible Church/ChapelHillBibleChurch2019SummerLeagueEast.json'
        input_file = open(participants_file, 'r', encoding="utf8")
        participants_content = input_file.read()
        # The JSON parser returns a dictionary. The data that describes the parks is located in the 'data' entry.
        participants_dictionary = json.loads(participants_content)

        for participant in participants_dictionary:
            player_id = str(participant['id'])
            first_name = participant['first_name']
            last_name = participant['last_name']
            gender = participant['gender']
            birth_date = str(participant['birth_date'])
            event_cost = str(participant['event_cost'])
            transaction_total = str(participant['transaction_total'])
            address_postal_code = str(participant['postal_code'])
            location = "Chapel Hill Bible Church"
            year = "2019"
            program_name = "ChapelHillBibleChurch2019SummerLeague"
            primary_key = player_id + program_name
            # Constructs the SQL query to insert park information into the database
            park_sql = 'INSERT OR IGNORE INTO PARTICIPANTS VALUES ("' + player_id + '","' + first_name + '", " ' + last_name + '","' + gender + '","' + birth_date + '","' + event_cost + '","' + transaction_total + '","' + address_postal_code + '","' + location + '","' + year + '","' + program_name + '","' + primary_key + '") '
            cursor.execute(park_sql)
            print(park_sql)

        db.commit()  # save the changes
        db.close()  # close the database
    except ValueError as err:
        print('An error occurred trying to decode the json text')
        print(err)
    except KeyError as err:
        print('Key not in data source')
        print(err)
    except HTTPError as err:
        print('Server could not fulfill the request.')
        print(err)
    except URLError as err:
        print('Failed to reach a server.')
        print(err)
    except sqlite3.IntegrityError as err:
        print('Integrity Error:', err)
    except sqlite3.OperationalError as err:
        print('Operational Error:', err)
    except sqlite3.Error as err:
        print('Error:', err)
    except Exception as err:
        print('An error occurred: ', err)


def insert_pineywood2020modified_skills_academy():
    try:
        dbname = 'youth_programs.db'
        db = sqlite3.connect(dbname)
        cursor = db.cursor()

        # ssl._create_default_https_context = ssl._create_unverified_context
        participants_file = '/Users/alex/Desktop/TU Youth Program CSVs/Pineywood/PineywoodSpringModifiedSkillsAcademy.json'
        input_file = open(participants_file, 'r', encoding="utf8")
        participants_content = input_file.read()
        # The JSON parser returns a dictionary. The data that describes the parks is located in the 'data' entry.
        participants_dictionary = json.loads(participants_content)

        for participant in participants_dictionary:
            player_id = str(participant['id'])
            first_name = participant['first_name']
            last_name = participant['last_name']
            gender = participant['gender']
            birth_date = str(participant['birth_date'])
            event_cost = str(participant['event_cost'])
            transaction_total = str(participant['transaction_total'])
            address_postal_code = str(participant['postal_code'])
            location = "Pineywood"
            year = "2020"
            program_name = "Pineywood2020ModifiedSkillsAcademy"
            primary_key = player_id + program_name
            # Constructs the SQL query to insert park information into the database
            park_sql = 'INSERT OR IGNORE INTO PARTICIPANTS VALUES ("' + player_id + '","' + first_name + '", " ' + last_name + '","' + gender + '","' + birth_date + '","' + event_cost + '","' + transaction_total + '","' + address_postal_code + '","' + location + '","' + year + '","' + program_name + '","' + primary_key + '") '
            cursor.execute(park_sql)
            print(park_sql)

        db.commit()  # save the changes
        db.close()  # close the database
    except ValueError as err:
        print('An error occurred trying to decode the json text')
        print(err)
    except KeyError as err:
        print('Key not in data source')
        print(err)
    except HTTPError as err:
        print('Server could not fulfill the request.')
        print(err)
    except URLError as err:
        print('Failed to reach a server.')
        print(err)
    except sqlite3.IntegrityError as err:
        print('Integrity Error:', err)
    except sqlite3.OperationalError as err:
        print('Operational Error:', err)
    except sqlite3.Error as err:
        print('Error:', err)
    except Exception as err:
        print('An error occurred: ', err)


def insert_old_chapel_hill_rd2021learn_to_play():
    try:
        dbname = 'youth_programs.db'
        db = sqlite3.connect(dbname)
        cursor = db.cursor()

        # ssl._create_default_https_context = ssl._create_unverified_context
        participants_file = '/Users/alex/Desktop/TU Youth Program CSVs/Old Chapel Hill Rd/OCHR2021FallLearnToPlay.json'
        input_file = open(participants_file, 'r', encoding="utf8")
        participants_content = input_file.read()
        # The JSON parser returns a dictionary. The data that describes the parks is located in the 'data' entry.
        participants_dictionary = json.loads(participants_content)

        for participant in participants_dictionary:
            player_id = str(participant['id'])
            first_name = participant['first_name']
            last_name = participant['last_name']
            gender = participant['gender']
            birth_date = str(participant['birth_date'])
            event_cost = str(participant['event_cost'])
            transaction_total = str(participant['transaction_total'])
            address_postal_code = str(participant['postal_code'])
            location = "Old Chapel Hill Rd"
            year = "2021"
            program_name = "OCHR2021LearnToPlay"
            primary_key = player_id + program_name
            # Constructs the SQL query to insert park information into the database
            park_sql = 'INSERT OR IGNORE INTO PARTICIPANTS VALUES ("' + player_id + '","' + first_name + '", " ' + last_name + '","' + gender + '","' + birth_date + '","' + event_cost + '","' + transaction_total + '","' + address_postal_code + '","' + location + '","' + year + '","' + program_name + '","' + primary_key + '") '
            cursor.execute(park_sql)
            print(park_sql)

        db.commit()  # save the changes
        db.close()  # close the database
    except ValueError as err:
        print('An error occurred trying to decode the json text')
        print(err)
    except KeyError as err:
        print('Key not in data source')
        print(err)
    except HTTPError as err:
        print('Server could not fulfill the request.')
        print(err)
    except URLError as err:
        print('Failed to reach a server.')
        print(err)
    except sqlite3.IntegrityError as err:
        print('Integrity Error:', err)
    except sqlite3.OperationalError as err:
        print('Operational Error:', err)
    except sqlite3.Error as err:
        print('Error:', err)
    except Exception as err:
        print('An error occurred: ', err)


def insert_old_chapel_hill_rd2021rec_league():
    try:
        dbname = 'youth_programs.db'
        db = sqlite3.connect(dbname)
        cursor = db.cursor()

        # ssl._create_default_https_context = ssl._create_unverified_context
        participants_file = '/Users/alex/Desktop/TU Youth Program CSVs/Old Chapel Hill Rd/OCHR2021FallRecLeague.json'
        input_file = open(participants_file, 'r', encoding="utf8")
        participants_content = input_file.read()
        # The JSON parser returns a dictionary. The data that describes the parks is located in the 'data' entry.
        participants_dictionary = json.loads(participants_content)

        for participant in participants_dictionary:
            player_id = str(participant['id'])
            first_name = participant['first_name']
            last_name = participant['last_name']
            gender = participant['gender']
            birth_date = str(participant['birth_date'])
            event_cost = str(participant['event_cost'])
            transaction_total = str(participant['transaction_total'])
            address_postal_code = str(participant['postal_code'])
            location = "Old Chapel Hill Rd"
            year = "2021"
            program_name = "OCHR2021RecLeague"
            primary_key = player_id + program_name
            # Constructs the SQL query to insert park information into the database
            park_sql = 'INSERT OR IGNORE INTO PARTICIPANTS VALUES ("' + player_id + '","' + first_name + '", " ' + last_name + '","' + gender + '","' + birth_date + '","' + event_cost + '","' + transaction_total + '","' + address_postal_code + '","' + location + '","' + year + '","' + program_name + '","' + primary_key + '") '
            cursor.execute(park_sql)
            print(park_sql)

        db.commit()  # save the changes
        db.close()  # close the database
    except ValueError as err:
        print('An error occurred trying to decode the json text')
        print(err)
    except KeyError as err:
        print('Key not in data source')
        print(err)
    except HTTPError as err:
        print('Server could not fulfill the request.')
        print(err)
    except URLError as err:
        print('Failed to reach a server.')
        print(err)
    except sqlite3.IntegrityError as err:
        print('Integrity Error:', err)
    except sqlite3.OperationalError as err:
        print('Operational Error:', err)
    except sqlite3.Error as err:
        print('Error:', err)
    except Exception as err:
        print('An error occurred: ', err)


def insert_old_chapel_hill_rd2022learn_to_play():
    try:
        dbname = 'youth_programs.db'
        db = sqlite3.connect(dbname)
        cursor = db.cursor()

        # ssl._create_default_https_context = ssl._create_unverified_context
        participants_file = '/Users/alex/Desktop/TU Youth Program CSVs/Old Chapel Hill Rd/OCHR2022SpringLearnToPlay.json'
        input_file = open(participants_file, 'r', encoding="utf8")
        participants_content = input_file.read()
        # The JSON parser returns a dictionary. The data that describes the parks is located in the 'data' entry.
        participants_dictionary = json.loads(participants_content)

        for participant in participants_dictionary:
            player_id = str(participant['id'])
            first_name = participant['first_name']
            last_name = participant['last_name']
            gender = participant['gender']
            birth_date = str(participant['birth_date'])
            event_cost = str(participant['event_cost'])
            transaction_total = str(participant['transaction_total'])
            address_postal_code = str(participant['postal_code'])
            location = "Old Chapel Hill Rd"
            year = "2022"
            program_name = "OCHR2022LearnToPlay"
            primary_key = player_id + program_name
            # Constructs the SQL query to insert park information into the database
            park_sql = 'INSERT OR IGNORE INTO PARTICIPANTS VALUES ("' + player_id + '","' + first_name + '", " ' + last_name + '","' + gender + '","' + birth_date + '","' + event_cost + '","' + transaction_total + '","' + address_postal_code + '","' + location + '","' + year + '","' + program_name + '","' + primary_key + '") '
            cursor.execute(park_sql)
            print(park_sql)

        db.commit()  # save the changes
        db.close()  # close the database
    except ValueError as err:
        print('An error occurred trying to decode the json text')
        print(err)
    except KeyError as err:
        print('Key not in data source')
        print(err)
    except HTTPError as err:
        print('Server could not fulfill the request.')
        print(err)
    except URLError as err:
        print('Failed to reach a server.')
        print(err)
    except sqlite3.IntegrityError as err:
        print('Integrity Error:', err)
    except sqlite3.OperationalError as err:
        print('Operational Error:', err)
    except sqlite3.Error as err:
        print('Error:', err)
    except Exception as err:
        print('An error occurred: ', err)


def insert_old_chapel_hill_rd2022rec_league():
    try:
        dbname = 'youth_programs.db'
        db = sqlite3.connect(dbname)
        cursor = db.cursor()

        # ssl._create_default_https_context = ssl._create_unverified_context
        participants_file = '/Users/alex/Desktop/TU Youth Program CSVs/Old Chapel Hill Rd/OCHR2022SpringRecLeague.json'
        input_file = open(participants_file, 'r', encoding="utf8")
        participants_content = input_file.read()
        # The JSON parser returns a dictionary. The data that describes the parks is located in the 'data' entry.
        participants_dictionary = json.loads(participants_content)

        for participant in participants_dictionary:
            player_id = str(participant['id'])
            first_name = participant['first_name']
            last_name = participant['last_name']
            gender = participant['gender']
            birth_date = str(participant['birth_date'])
            event_cost = str(participant['event_cost'])
            transaction_total = str(participant['transaction_total'])
            address_postal_code = str(participant['postal_code'])
            location = "Old Chapel Hill Rd"
            year = "2022"
            program_name = "OCHR2022RecLeague"
            primary_key = player_id + program_name
            # Constructs the SQL query to insert park information into the database
            park_sql = 'INSERT OR IGNORE INTO PARTICIPANTS VALUES ("' + player_id + '","' + first_name + '", " ' + last_name + '","' + gender + '","' + birth_date + '","' + event_cost + '","' + transaction_total + '","' + address_postal_code + '","' + location + '","' + year + '","' + program_name + '","' + primary_key + '") '
            cursor.execute(park_sql)
            print(park_sql)

        db.commit()  # save the changes
        db.close()  # close the database
    except ValueError as err:
        print('An error occurred trying to decode the json text')
        print(err)
    except KeyError as err:
        print('Key not in data source')
        print(err)
    except HTTPError as err:
        print('Server could not fulfill the request.')
        print(err)
    except URLError as err:
        print('Failed to reach a server.')
        print(err)
    except sqlite3.IntegrityError as err:
        print('Integrity Error:', err)
    except sqlite3.OperationalError as err:
        print('Operational Error:', err)
    except sqlite3.Error as err:
        print('Error:', err)
    except Exception as err:
        print('An error occurred: ', err)


def insert_old_chapel_hill_rd2020modified_skills_academy():
    try:
        dbname = 'youth_programs.db'
        db = sqlite3.connect(dbname)
        cursor = db.cursor()

        # ssl._create_default_https_context = ssl._create_unverified_context
        participants_file = '/Users/alex/Desktop/TU Youth Program CSVs/Old Chapel Hill Rd/OCHRSpringModifiedSkillsAcademy.json'
        input_file = open(participants_file, 'r', encoding="utf8")
        participants_content = input_file.read()
        # The JSON parser returns a dictionary. The data that describes the parks is located in the 'data' entry.
        participants_dictionary = json.loads(participants_content)

        for participant in participants_dictionary:
            player_id = str(participant['id'])
            first_name = participant['first_name']
            last_name = participant['last_name']
            gender = participant['gender']
            birth_date = str(participant['birth_date'])
            event_cost = str(participant['event_cost'])
            transaction_total = str(participant['transaction_total'])
            address_postal_code = str(participant['postal_code'])
            location = "Old Chapel Hill Rd"
            year = "2020"
            program_name = "OCHR2020ModifiedSkillsAcademy"
            primary_key = player_id + program_name
            # Constructs the SQL query to insert park information into the database
            park_sql = 'INSERT OR IGNORE INTO PARTICIPANTS VALUES ("' + player_id + '","' + first_name + '", " ' + last_name + '","' + gender + '","' + birth_date + '","' + event_cost + '","' + transaction_total + '","' + address_postal_code + '","' + location + '","' + year + '","' + program_name + '","' + primary_key + '") '
            cursor.execute(park_sql)
            print(park_sql)

        db.commit()  # save the changes
        db.close()  # close the database
    except ValueError as err:
        print('An error occurred trying to decode the json text')
        print(err)
    except KeyError as err:
        print('Key not in data source')
        print(err)
    except HTTPError as err:
        print('Server could not fulfill the request.')
        print(err)
    except URLError as err:
        print('Failed to reach a server.')
        print(err)
    except sqlite3.IntegrityError as err:
        print('Integrity Error:', err)
    except sqlite3.OperationalError as err:
        print('Operational Error:', err)
    except sqlite3.Error as err:
        print('Error:', err)
    except Exception as err:
        print('An error occurred: ', err)


def insert_weaver2020modified_skills_academy():
    try:
        dbname = 'youth_programs.db'
        db = sqlite3.connect(dbname)
        cursor = db.cursor()

        # ssl._create_default_https_context = ssl._create_unverified_context
        participants_file = '/Users/alex/Desktop/TU Youth Program CSVs/Weaver st. Park/WeaverModifiedSkillsAcademy.json'
        input_file = open(participants_file, 'r', encoding="utf8")
        participants_content = input_file.read()
        # The JSON parser returns a dictionary. The data that describes the parks is located in the 'data' entry.
        participants_dictionary = json.loads(participants_content)

        for participant in participants_dictionary:
            player_id = str(participant['id'])
            first_name = participant['first_name']
            last_name = participant['last_name']
            gender = participant['gender']
            birth_date = str(participant['birth_date'])
            event_cost = str(participant['event_cost'])
            transaction_total = str(participant['transaction_total'])
            address_postal_code = str(participant['postal_code'])
            location = "Weaver St. Park"
            year = "2020"
            program_name = "Weaver2020ModifiedSkillsAcademy"
            primary_key = player_id + program_name
            # Constructs the SQL query to insert park information into the database
            park_sql = 'INSERT OR IGNORE INTO PARTICIPANTS VALUES ("' + player_id + '","' + first_name + '", " ' + last_name + '","' + gender + '","' + birth_date + '","' + event_cost + '","' + transaction_total + '","' + address_postal_code + '","' + location + '","' + year + '","' + program_name + '","' + primary_key + '") '
            cursor.execute(park_sql)
            print(park_sql)

        db.commit()  # save the changes
        db.close()  # close the database
    except ValueError as err:
        print('An error occurred trying to decode the json text')
        print(err)
    except KeyError as err:
        print('Key not in data source')
        print(err)
    except HTTPError as err:
        print('Server could not fulfill the request.')
        print(err)
    except URLError as err:
        print('Failed to reach a server.')
        print(err)
    except sqlite3.IntegrityError as err:
        print('Integrity Error:', err)
    except sqlite3.OperationalError as err:
        print('Operational Error:', err)
    except sqlite3.Error as err:
        print('Error:', err)
    except Exception as err:
        print('An error occurred: ', err)


def insert_hargraves2021learn_to_play():
    try:
        dbname = 'youth_programs.db'
        db = sqlite3.connect(dbname)
        cursor = db.cursor()

        # ssl._create_default_https_context = ssl._create_unverified_context
        participants_file = '/Users/alex/Desktop/TU Youth Program CSVs/Hargraves/Hargraves2021SummerLearnToPlay.json'
        input_file = open(participants_file, 'r', encoding="utf8")
        participants_content = input_file.read()
        # The JSON parser returns a dictionary. The data that describes the parks is located in the 'data' entry.
        participants_dictionary = json.loads(participants_content)

        for participant in participants_dictionary:
            player_id = str(participant['id'])
            first_name = participant['first_name']
            last_name = participant['last_name']
            gender = participant['gender']
            birth_date = str(participant['birth_date'])
            event_cost = str(participant['event_cost'])
            transaction_total = str(participant['transaction_total'])
            address_postal_code = str(participant['postal_code'])
            location = "Hargraves"
            year = "2021"
            program_name = "Hargraves2021LearnToPlay"
            primary_key = player_id + program_name
            # Constructs the SQL query to insert park information into the database
            park_sql = 'INSERT OR IGNORE INTO PARTICIPANTS VALUES ("' + player_id + '","' + first_name + '", " ' + last_name + '","' + gender + '","' + birth_date + '","' + event_cost + '","' + transaction_total + '","' + address_postal_code + '","' + location + '","' + year + '","' + program_name + '","' + primary_key + '") '
            cursor.execute(park_sql)
            print(park_sql)

        db.commit()  # save the changes
        db.close()  # close the database
    except ValueError as err:
        print('An error occurred trying to decode the json text')
        print(err)
    except KeyError as err:
        print('Key not in data source')
        print(err)
    except HTTPError as err:
        print('Server could not fulfill the request.')
        print(err)
    except URLError as err:
        print('Failed to reach a server.')
        print(err)
    except sqlite3.IntegrityError as err:
        print('Integrity Error:', err)
    except sqlite3.OperationalError as err:
        print('Operational Error:', err)
    except sqlite3.Error as err:
        print('Error:', err)
    except Exception as err:
        print('An error occurred: ', err)


def insert_dorthea_dix2021fall_learn_to_play():
    try:
        dbname = 'youth_programs.db'
        db = sqlite3.connect(dbname)
        cursor = db.cursor()

        # ssl._create_default_https_context = ssl._create_unverified_context
        participants_file = '/Users/alex/Desktop/TU Youth Program CSVs/Dorthea Dix/DortheaDix2021FallLearnToPlay.json'
        input_file = open(participants_file, 'r', encoding="utf8")
        participants_content = input_file.read()
        # The JSON parser returns a dictionary. The data that describes the parks is located in the 'data' entry.
        participants_dictionary = json.loads(participants_content)

        for participant in participants_dictionary:
            player_id = str(participant['id'])
            first_name = participant['first_name']
            last_name = participant['last_name']
            gender = participant['gender']
            birth_date = str(participant['birth_date'])
            event_cost = str(participant['event_cost'])
            transaction_total = str(participant['transaction_total'])
            address_postal_code = str(participant['postal_code'])
            location = "Dorthea Dix"
            year = "2021"
            program_name = "DortheaDix2021FallLearnToPlay"
            primary_key = player_id + program_name
            # Constructs the SQL query to insert park information into the database
            park_sql = 'INSERT OR IGNORE INTO PARTICIPANTS VALUES ("' + player_id + '","' + first_name + '", " ' + last_name + '","' + gender + '","' + birth_date + '","' + event_cost + '","' + transaction_total + '","' + address_postal_code + '","' + location + '","' + year + '","' + program_name + '","' + primary_key + '") '
            cursor.execute(park_sql)
            print(park_sql)

        db.commit()  # save the changes
        db.close()  # close the database
    except ValueError as err:
        print('An error occurred trying to decode the json text')
        print(err)
    except KeyError as err:
        print('Key not in data source')
        print(err)
    except HTTPError as err:
        print('Server could not fulfill the request.')
        print(err)
    except URLError as err:
        print('Failed to reach a server.')
        print(err)
    except sqlite3.IntegrityError as err:
        print('Integrity Error:', err)
    except sqlite3.OperationalError as err:
        print('Operational Error:', err)
    except sqlite3.Error as err:
        print('Error:', err)
    except Exception as err:
        print('An error occurred: ', err)


def insert_dorthea_dix2021summer_learn_to_play():
    try:
        dbname = 'youth_programs.db'
        db = sqlite3.connect(dbname)
        cursor = db.cursor()

        # ssl._create_default_https_context = ssl._create_unverified_context
        participants_file = '/Users/alex/Desktop/TU Youth Program CSVs/Dorthea Dix/DortheaDix2021SummerLearnToPlay.json'
        input_file = open(participants_file, 'r', encoding="utf8")
        participants_content = input_file.read()
        # The JSON parser returns a dictionary. The data that describes the parks is located in the 'data' entry.
        participants_dictionary = json.loads(participants_content)

        for participant in participants_dictionary:
            player_id = str(participant['id'])
            first_name = participant['first_name']
            last_name = participant['last_name']
            gender = participant['gender']
            birth_date = str(participant['birth_date'])
            event_cost = str(participant['event_cost'])
            transaction_total = str(participant['transaction_total'])
            address_postal_code = str(participant['postal_code'])
            location = "Dorthea Dix"
            year = "2021"
            program_name = "DortheaDix2021SummerLearnToPlay"
            primary_key = player_id + program_name
            # Constructs the SQL query to insert park information into the database
            park_sql = 'INSERT OR IGNORE INTO PARTICIPANTS VALUES ("' + player_id + '","' + first_name + '", " ' + last_name + '","' + gender + '","' + birth_date + '","' + event_cost + '","' + transaction_total + '","' + address_postal_code + '","' + location + '","' + year + '","' + program_name + '","' + primary_key + '") '
            cursor.execute(park_sql)
            print(park_sql)

        db.commit()  # save the changes
        db.close()  # close the database
    except ValueError as err:
        print('An error occurred trying to decode the json text')
        print(err)
    except KeyError as err:
        print('Key not in data source')
        print(err)
    except HTTPError as err:
        print('Server could not fulfill the request.')
        print(err)
    except URLError as err:
        print('Failed to reach a server.')
        print(err)
    except sqlite3.IntegrityError as err:
        print('Integrity Error:', err)
    except sqlite3.OperationalError as err:
        print('Operational Error:', err)
    except sqlite3.Error as err:
        print('Error:', err)
    except Exception as err:
        print('An error occurred: ', err)


def insert_dorthea_dix2021rec_league():
    try:
        dbname = 'youth_programs.db'
        db = sqlite3.connect(dbname)
        cursor = db.cursor()

        # ssl._create_default_https_context = ssl._create_unverified_context
        participants_file = '/Users/alex/Desktop/TU Youth Program CSVs/Dorthea Dix/DortheaDix2021FallRecLeague.json'
        input_file = open(participants_file, 'r', encoding="utf8")
        participants_content = input_file.read()
        # The JSON parser returns a dictionary. The data that describes the parks is located in the 'data' entry.
        participants_dictionary = json.loads(participants_content)

        for participant in participants_dictionary:
            player_id = str(participant['id'])
            first_name = participant['first_name']
            last_name = participant['last_name']
            gender = participant['gender']
            birth_date = str(participant['birth_date'])
            event_cost = str(participant['event_cost'])
            transaction_total = str(participant['transaction_total'])
            address_postal_code = str(participant['postal_code'])
            location = "Dorthea Dix"
            year = "2021"
            program_name = "DortheaDix2021RecLeague"
            primary_key = player_id + program_name
            # Constructs the SQL query to insert park information into the database
            park_sql = 'INSERT OR IGNORE INTO PARTICIPANTS VALUES ("' + player_id + '","' + first_name + '", " ' + last_name + '","' + gender + '","' + birth_date + '","' + event_cost + '","' + transaction_total + '","' + address_postal_code + '","' + location + '","' + year + '","' + program_name + '","' + primary_key + '") '
            cursor.execute(park_sql)
            print(park_sql)

        db.commit()  # save the changes
        db.close()  # close the database
    except ValueError as err:
        print('An error occurred trying to decode the json text')
        print(err)
    except KeyError as err:
        print('Key not in data source')
        print(err)
    except HTTPError as err:
        print('Server could not fulfill the request.')
        print(err)
    except URLError as err:
        print('Failed to reach a server.')
        print(err)
    except sqlite3.IntegrityError as err:
        print('Integrity Error:', err)
    except sqlite3.OperationalError as err:
        print('Operational Error:', err)
    except sqlite3.Error as err:
        print('Error:', err)
    except Exception as err:
        print('An error occurred: ', err)


def insert_dorthea_dix2022learn_to_play():
    try:
        dbname = 'youth_programs.db'
        db = sqlite3.connect(dbname)
        cursor = db.cursor()

        # ssl._create_default_https_context = ssl._create_unverified_context
        participants_file = '/Users/alex/Desktop/TU Youth Program CSVs/Dorthea Dix/DortheaDixSpringLearnToPlay2022.json'
        input_file = open(participants_file, 'r', encoding="utf8")
        participants_content = input_file.read()
        # The JSON parser returns a dictionary. The data that describes the parks is located in the 'data' entry.
        participants_dictionary = json.loads(participants_content)

        for participant in participants_dictionary:
            player_id = str(participant['id'])
            first_name = participant['first_name']
            last_name = participant['last_name']
            gender = participant['gender']
            birth_date = str(participant['birth_date'])
            event_cost = str(participant['event_cost'])
            transaction_total = str(participant['transaction_total'])
            address_postal_code = str(participant['postal_code'])
            location = "Dorthea Dix"
            year = "2022"
            program_name = "DortheaDix2022LearnToPlay"
            primary_key = player_id + program_name
            # Constructs the SQL query to insert park information into the database
            park_sql = 'INSERT OR IGNORE INTO PARTICIPANTS VALUES ("' + player_id + '","' + first_name + '", " ' + last_name + '","' + gender + '","' + birth_date + '","' + event_cost + '","' + transaction_total + '","' + address_postal_code + '","' + location + '","' + year + '","' + program_name + '","' + primary_key + '") '
            cursor.execute(park_sql)
            print(park_sql)

        db.commit()  # save the changes
        db.close()  # close the database
    except ValueError as err:
        print('An error occurred trying to decode the json text')
        print(err)
    except KeyError as err:
        print('Key not in data source')
        print(err)
    except HTTPError as err:
        print('Server could not fulfill the request.')
        print(err)
    except URLError as err:
        print('Failed to reach a server.')
        print(err)
    except sqlite3.IntegrityError as err:
        print('Integrity Error:', err)
    except sqlite3.OperationalError as err:
        print('Operational Error:', err)
    except sqlite3.Error as err:
        print('Error:', err)
    except Exception as err:
        print('An error occurred: ', err)


def insert_chhs2022learn_to_play():
    try:
        dbname = 'youth_programs.db'
        db = sqlite3.connect(dbname)
        cursor = db.cursor()

        # ssl._create_default_https_context = ssl._create_unverified_context
        participants_file = '/Users/alex/Desktop/TU Youth Program CSVs/Chapel Hill High School/CHHS2022SpringLearnToPlay.json'
        input_file = open(participants_file, 'r', encoding="utf8")
        participants_content = input_file.read()
        # The JSON parser returns a dictionary. The data that describes the parks is located in the 'data' entry.
        participants_dictionary = json.loads(participants_content)

        for participant in participants_dictionary:
            player_id = str(participant['id'])
            first_name = participant['first_name']
            last_name = participant['last_name']
            gender = participant['gender']
            birth_date = str(participant['birth_date'])
            event_cost = str(participant['event_cost'])
            transaction_total = str(participant['transaction_total'])
            address_postal_code = str(participant['postal_code'])
            location = "CHHS"
            year = "2022"
            program_name = "CHHS2022LearnToPlay"
            primary_key = player_id + program_name
            # Constructs the SQL query to insert park information into the database
            park_sql = 'INSERT OR IGNORE INTO PARTICIPANTS VALUES ("' + player_id + '","' + first_name + '", " ' + last_name + '","' + gender + '","' + birth_date + '","' + event_cost + '","' + transaction_total + '","' + address_postal_code + '","' + location + '","' + year + '","' + program_name + '","' + primary_key + '") '
            cursor.execute(park_sql)
            print(park_sql)

        db.commit()  # save the changes
        db.close()  # close the database
    except ValueError as err:
        print('An error occurred trying to decode the json text')
        print(err)
    except KeyError as err:
        print('Key not in data source')
        print(err)
    except HTTPError as err:
        print('Server could not fulfill the request.')
        print(err)
    except URLError as err:
        print('Failed to reach a server.')
        print(err)
    except sqlite3.IntegrityError as err:
        print('Integrity Error:', err)
    except sqlite3.OperationalError as err:
        print('Operational Error:', err)
    except sqlite3.Error as err:
        print('Error:', err)
    except Exception as err:
        print('An error occurred: ', err)


def insert_chhs2022rec_league():
    try:
        dbname = 'youth_programs.db'
        db = sqlite3.connect(dbname)
        cursor = db.cursor()

        # ssl._create_default_https_context = ssl._create_unverified_context
        participants_file = '/Users/alex/Desktop/TU Youth Program CSVs/Chapel Hill High School/CHHS2022RecLeague.json'
        input_file = open(participants_file, 'r', encoding="utf8")
        participants_content = input_file.read()
        # The JSON parser returns a dictionary. The data that describes the parks is located in the 'data' entry.
        participants_dictionary = json.loads(participants_content)

        for participant in participants_dictionary:
            player_id = str(participant['id'])
            first_name = participant['first_name']
            last_name = participant['last_name']
            gender = participant['gender']
            birth_date = str(participant['birth_date'])
            event_cost = str(participant['event_cost'])
            transaction_total = str(participant['transaction_total'])
            address_postal_code = str(participant['postal_code'])
            location = "CHHS"
            year = "2022"
            program_name = "CHHS2022RecLeague"
            primary_key = player_id + program_name
            # Constructs the SQL query to insert park information into the database
            park_sql = 'INSERT OR IGNORE INTO PARTICIPANTS VALUES ("' + player_id + '","' + first_name + '", " ' + last_name + '","' + gender + '","' + birth_date + '","' + event_cost + '","' + transaction_total + '","' + address_postal_code + '","' + location + '","' + year + '","' + program_name + '","' + primary_key + '") '
            cursor.execute(park_sql)
            print(park_sql)

        db.commit()  # save the changes
        db.close()  # close the database
    except ValueError as err:
        print('An error occurred trying to decode the json text')
        print(err)
    except KeyError as err:
        print('Key not in data source')
        print(err)
    except HTTPError as err:
        print('Server could not fulfill the request.')
        print(err)
    except URLError as err:
        print('Failed to reach a server.')
        print(err)
    except sqlite3.IntegrityError as err:
        print('Integrity Error:', err)
    except sqlite3.OperationalError as err:
        print('Operational Error:', err)
    except sqlite3.Error as err:
        print('Error:', err)
    except Exception as err:
        print('An error occurred: ', err)


def insert_kestrel_heights2019after_school_clinic():
    try:
        dbname = 'youth_programs.db'
        db = sqlite3.connect(dbname)
        cursor = db.cursor()

        # ssl._create_default_https_context = ssl._create_unverified_context
        participants_file = '/Users/alex/Desktop/TU Youth Program CSVs/Kestrel Heights Elementary/KestrelHeights2019AfterSchoolClinic.json'
        input_file = open(participants_file, 'r', encoding="utf8")
        participants_content = input_file.read()
        # The JSON parser returns a dictionary. The data that describes the parks is located in the 'data' entry.
        participants_dictionary = json.loads(participants_content)

        for participant in participants_dictionary:
            player_id = str(participant['id'])
            first_name = participant['first_name']
            last_name = participant['last_name']
            gender = participant['gender']
            birth_date = str(participant['birth_date'])
            event_cost = str(participant['event_cost'])
            transaction_total = str(participant['transaction_total'])
            address_postal_code = str(participant['postal_code'])
            location = "Kestrel Heights Elementary"
            year = "2019"
            program_name = "KestrelHeights2019AfterSchoolClinic"
            primary_key = player_id + program_name
            # Constructs the SQL query to insert park information into the database
            park_sql = 'INSERT OR IGNORE INTO PARTICIPANTS VALUES ("' + player_id + '","' + first_name + '", " ' + last_name + '","' + gender + '","' + birth_date + '","' + event_cost + '","' + transaction_total + '","' + address_postal_code + '","' + location + '","' + year + '","' + program_name + '","' + primary_key + '") '
            cursor.execute(park_sql)
            print(park_sql)

        db.commit()  # save the changes
        db.close()  # close the database
    except ValueError as err:
        print('An error occurred trying to decode the json text')
        print(err)
    except KeyError as err:
        print('Key not in data source')
        print(err)
    except HTTPError as err:
        print('Server could not fulfill the request.')
        print(err)
    except URLError as err:
        print('Failed to reach a server.')
        print(err)
    except sqlite3.IntegrityError as err:
        print('Integrity Error:', err)
    except sqlite3.OperationalError as err:
        print('Operational Error:', err)
    except sqlite3.Error as err:
        print('Error:', err)
    except Exception as err:
        print('An error occurred: ', err)


def insert_records():
    insert_da2017middle_school_tournament_records()
    insert_da2018middle_school_tournament_records()
    insert_lee2018hat_tournament_records()
    insert_kiwanis2017learn_to_compete_records()
    insert_kiwanis2017learn_to_play_records()
    insert_kiwanis2022learn_to_play_records()
    insert_kiwanis2022rec_league()
    insert_meadowmont2017summer_league()
    insert_meadowmont2022learn_to_play()
    insert_miller2017learn_to_play()
    insert_miller2017learn_to_compete()
    insert_miller2018wolfpack_tournament()
    insert_miller2019wolfpack_tournament()
    insert_miller2019middle_school_championship()
    insert_miller2020middle_school_championship()
    insert_miller2022middle_school_championship()
    insert_herndon2019learn_to_compete()
    insert_herndon2017learn_to_compete()
    insert_herndon2018gum()
    insert_herndon2019learn_to_compete_girls()
    insert_herndon2019learn_to_play()
    insert_herndon2017learn_to_play()
    insert_herndon2018learn_to_compete()
    insert_herndon2018learn_to_play()
    insert_hank_anderson2021rec_league()
    insert_hank_anderson2021learn_to_play()
    insert_hank_anderson2017learn_to_play()
    insert_hank_anderson2018learn_to_compete()
    insert_hank_anderson2018learn_to_play_spring()
    insert_hank_anderson2018learn_to_play_fall()
    insert_cedar_falls_2018_gum()
    insert_cfs2017middle_school_clinic()
    insert_cfs2018middle_school_clinic()
    insert_mac2018summer_league()
    insert_laurel_hills_2018_learn_to_play()
    insert_laurel_hills2019learn_to_play()
    insert_east_durham2019learn_to_play()
    insert_east_durham2018learn_to_play()
    insert_heritage2018learn_to_play()
    insert_homestead2019learn_to_play()
    insert_wake_forest2019learn_to_play()
    insert_cedar_forks2019summer_league_girls()
    insert_cedar_forks2021ycc()
    insert_cedar_forks2021learn_to_play()
    insert_cedar_forks2021rec_league()
    insert_cedar_forks2019summer_league()
    insert_chapel_hill_bible_church2019summer_league()
    insert_pineywood2020modified_skills_academy()
    insert_old_chapel_hill_rd2022learn_to_play()
    insert_old_chapel_hill_rd2021learn_to_play()
    insert_old_chapel_hill_rd2022rec_league()
    insert_old_chapel_hill_rd2021rec_league()
    insert_old_chapel_hill_rd2020modified_skills_academy()
    insert_weaver2020modified_skills_academy()
    insert_hargraves2021learn_to_play()
    insert_dorthea_dix2021fall_learn_to_play()
    insert_dorthea_dix2021summer_learn_to_play()
    insert_dorthea_dix2022learn_to_play()
    insert_dorthea_dix2021rec_league()
    insert_chhs2022learn_to_play()
    insert_chhs2022rec_league()
    insert_kestrel_heights2019after_school_clinic()


main()
