import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('/workspace/boilerplate-demographic-data-analyzer/adult.data.csv')

    # How many people of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()
    
    # What is the average age of men?
    average_age_men = df[df['sex'] == 'Male']['age'].mean()
    # What is the average age of female?
    average_age_women = df[df['sex'] == 'Female']['age'].mean()

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = (df['education'] == 'Bachelors').sum() / df.shape[0] * 100

    # What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    # What percentage of people without advanced education make more than 50K?
    lower_education_rich = (lower_education['salary'] == '>50K').sum() / lower_education.shape[0] * 100
    higher_education_rich = (higher_education['salary'] == '>50K').sum() / higher_education.shape[0] * 100

    # What is the minimum number of hours a person works per week?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = (num_min_workers['salary'] == '>50K').sum() / num_min_workers.shape[0] * 100

    # What country has the highest percentage of people that earn >50K and what is that percentage?
    highest_earning_country = (df[df['salary'] == '>50K']['native-country'].value_counts() / df['native-country'].value_counts()).idxmax()
    highest_earning_country_percentage = (df[df['salary'] == '>50K']['native-country'].value_counts() / df['native-country'].value_counts()).max() * 100

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().idxmax()

    if print_data:
        print("each race by number:\n", race_count)
        print("male average age:", round(average_age_men, 1))
        print("female average age:", round(average_age_women, 1))
        print("persons with Bachelors degrees by percentage:", round(percentage_bachelors, 1))
        print("persons with higher education that earn >50K by percentage:", round(higher_education_rich, 1))
        print("persons without higher education that earn >50K by percentage:", round(lower_education_rich, 1))
        print("minimum work time:", min_work_hours, "hours/week")
        print("rich persons among those who work fewest hours by percentage:", round(rich_percentage, 1))
        print("Country with the most rich persons by percentage:", highest_earning_country)
        print("country with rich persons who have the highest earnings by percentage:", round(highest_earning_country_percentage, 1))
        print("Top occupation in India that earns >50K:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': round(average_age_men, 1),
        'average_age_women': round(average_age_women, 1),
        'percentage_bachelors': round(percentage_bachelors, 1),
        'higher_education_rich': round(higher_education_rich, 1),
        'lower_education_rich': round(lower_education_rich, 1),
        'min_work_hours': min_work_hours,
        'rich_percentage': round(rich_percentage, 1),
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': round(highest_earning_country_percentage, 1),
        'top_IN_occupation': top_IN_occupation
    }

# Uncomment the line below to run the code and see the results
calculate_demographic_data()
