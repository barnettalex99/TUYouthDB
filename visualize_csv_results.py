import pandas as pd
import matplotlib.pyplot as plt


def main():
     #visualize_num_programs_at_each_location()
    # visualize_num_participants_at_each_location()
     # visualize_avg_num_participants_at_each_location()
     # visualize_percent_female()
    visualize_income_per_location()
    # visualize_income_per_program()
    # visualize_income_per_participant()
    # visualize_percent_paid_per_location()
    # visualize_percent_paid_more_than_cost_per_location()
    # visualize_percent_paid_less_than_cost_per_location()
    # visualize_num_returners_caused_per_location()


def visualize_num_programs_at_each_location():
    programs_at_each_location_file = '/Users/alex/Desktop/TU Youth Program CSVs/Query Results/ProgramsPerLocation.csv'
    programs_at_each_location_data = pd.read_csv(programs_at_each_location_file)
    programs_at_each_location_data.head()
    programs_at_each_location_df = programs_at_each_location_data['Location'].value_counts()
    print(programs_at_each_location_df)
    programs_at_each_location_df.plot(kind='bar')
    plt.tight_layout()
    plt.show()


def visualize_num_participants_at_each_location():
    participants_at_each_location_file = '/Users/alex/Desktop/TU Youth Program CSVs/Query Results/ParticipantsPerLocation.csv'
    participants_at_each_location_data = pd.read_csv(participants_at_each_location_file)
    participants_at_each_location_data.head()
    participants_at_each_location_df = participants_at_each_location_data['Location'].value_counts()
    print(participants_at_each_location_df)
    participants_at_each_location_df.plot(kind='bar')
    plt.tight_layout()
    plt.show()


def visualize_avg_num_participants_at_each_location():
    avg_num_participants_file = '/Users/alex/Desktop/TU Youth Program CSVs/Query Results/ParticipantsPerLocation.csv'
    avg_num_participants_data = pd.read_csv(avg_num_participants_file)
    num_programs = [6, 4, 2, 1, 8, 6, 5, 4, 2, 4, 2, 1, 2, 1, 1, 1, 2, 1, 1, 2,
                    1, 1, 1, 1]
    avg_num_participants_df = avg_num_participants_data['Location'].value_counts()
    num_participants = [960, 333, 287, 247, 237, 171, 154, 154, 137, 121, 85, 83, 67, 31, 30, 30, 29, 27, 20, 15, 10, 6,
                        2, 1]
    avg_num_participants_list = [0] * 24
    i = 0
    while i < len(num_participants):
        avg_num_participants_list[i] = num_participants[i] / num_programs[i]
        i = i + 1
    print(avg_num_participants_df)
    print(avg_num_participants_list)
    plt.bar(avg_num_participants_df.Location, avg_num_participants_list)
    plt.title('Avg Number of Participants Per Location')
    plt.xlabel('Locations')
    plt.ylabel('Average Number of Participants')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()


def visualize_percent_female():
    gender_of_participants_file = '/Users/alex/Desktop/TU Youth Program CSVs/Query Results/GenderDistributionPerLocation.csv'
    gender_of_participants_df = pd.read_csv(gender_of_participants_file)
    gender_of_participants_df.head()
    plt.bar(gender_of_participants_df.Location, gender_of_participants_df.PercentFemale)
    plt.title('Percentage of Female Participation at Each Location')
    plt.xlabel('Locations')
    plt.ylabel('Percentage Female Participation')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()


def visualize_income_per_location():
    income_per_location_file = '/Users/alex/Desktop/TU Youth Program CSVs/Query Results/TransactionTotalPerLocation.csv'
    income_per_location_df = pd.read_csv(income_per_location_file)
    income_per_location_df.head()
    plt.bar(income_per_location_df.Location, income_per_location_df.LocationTotal)
    plt.title('Total Paid At Each Location')
    plt.xlabel('Locations')
    plt.ylabel('Transaction Total')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()


def visualize_income_per_program():
    income_per_program_file = '/Users/alex/Desktop/TU Youth Program CSVs/Query Results/TransactionTotalPerLocation.csv'
    income_per_program_df = pd.read_csv(income_per_program_file)
    income_per_program_df.head()
    plt.bar(income_per_program_df.Location, income_per_program_df.AvgPerProgram)
    plt.title('Avg Paid At Each Location Per Program')
    plt.xlabel('Locations')
    plt.ylabel('Average Transaction Total Per Program')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()


def visualize_income_per_participant():
    income_per_participant_file = '/Users/alex/Desktop/TU Youth Program CSVs/Query Results/TransactionTotalPerParticipant.csv'
    income_per_participant_df = pd.read_csv(income_per_participant_file)
    income_per_participant_df.head()
    plt.bar(income_per_participant_df.Location, income_per_participant_df.AvgPerParticipant)
    plt.title('Avg Paid At Each Location Per Participant')
    plt.xlabel('Locations')
    plt.ylabel('Average Transaction Total Per Participant')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()


def visualize_percent_paid_per_location():
    percent_paid_per_location_file = '/Users/alex/Desktop/TU Youth Program CSVs/Query Results/PercentPaidPerLocation.csv'
    percent_paid_per_location_df = pd.read_csv(percent_paid_per_location_file)
    percent_paid_per_location_df.head()
    plt.bar(percent_paid_per_location_df.Location, percent_paid_per_location_df.PercentPaid)
    plt.title('Percent of Total Event Cost Paid At Each Location')
    plt.xlabel('Locations')
    plt.ylabel('Percent Paid')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()


def visualize_percent_paid_more_than_cost_per_location():
    percent_paid_more_file = '/Users/alex/Desktop/TU Youth Program CSVs/Query Results/NumPaidMoreThanCost.csv'
    percent_paid_more_df = pd.read_csv(percent_paid_more_file)
    percent_paid_more_df.head()
    plt.bar(percent_paid_more_df.Location, percent_paid_more_df.PercentPaidMore)
    plt.title('Percent of Participants That Paid More Than Event Cost At Each Location')
    plt.xlabel('Locations')
    plt.ylabel('Percent Paid More Than Event Cost')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()


def visualize_percent_paid_less_than_cost_per_location():
    percent_paid_less_file = '/Users/alex/Desktop/TU Youth Program CSVs/Query Results/NumPaidLessThanCost.csv'
    percent_paid_less_df = pd.read_csv(percent_paid_less_file)
    percent_paid_less_df.head()
    plt.bar(percent_paid_less_df.Location, percent_paid_less_df.PercentPaidLess)
    plt.title('Percent of Participants That Paid Less Than Event Cost At Each Location')
    plt.xlabel('Locations')
    plt.ylabel('Percent Paid Less Than Event Cost')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()


def visualize_num_returners_caused_per_location():
    returners_caused_file = '/Users/alex/Desktop/TU Youth Program CSVs/Query Results/Returners.csv'
    returners_caused_df = pd.read_csv(returners_caused_file)
    returners_caused_df.head()
    plt.bar(returners_caused_df.Location, returners_caused_df.NumReturners)
    plt.title('Number of Returners That Started at Each Location')
    plt.xlabel('Locations')
    plt.ylabel('Number of Returners')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

main()
