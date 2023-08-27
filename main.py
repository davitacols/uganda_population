import csv

def calculate_fund_and_earnings(age, education, monthly_earnings):
    if age > 50 and education in ["High School", "Primary School"]:
        government_fund = 1000
    else:
        government_fund = 0
    passive_earnings = monthly_earnings * 12
    return government_fund + passive_earnings

def calculate_age_group_totals(data):
    age_groups = {
        "0-18": 0,
        "19-21": 0,
        "22-29": 0,
        "30-45": 0,
        "46-60": 0,
        "60+": 0
    }
    for person in data:
        age = int(person["Age"])
        if age <= 18:
            age_groups["0-18"] += 1
        elif 19 <= age <= 21:
            age_groups["19-21"] += 1
        elif 22 <= age <= 29:
            age_groups["22-29"] += 1
        elif 30 <= age <= 45:
            age_groups["30-45"] += 1
        elif 46 <= age <= 60:
            age_groups["46-60"] += 1
        else:
            age_groups["60+"] += 1
    return age_groups

def main():
    with open("uganda_population.csv", mode="r") as csvfile:
        reader = csv.DictReader(csvfile)
        eligible_for_gov_fund = []
        eligible_for_seed_fund = []
        females_by_age_groups = {
            "0-18": 0,
            "19-21": 0,
            "22-29": 0,
            "30-45": 0,
            "46-60": 0,
            "60+": 0
        }
        males_by_age_groups = {
            "0-18": 0,
            "19-21": 0,
            "22-29": 0,
            "30-45": 0,
            "46-60": 0,
            "60+": 0
        }
        unicef_program = []

        for row in reader:
            age = int(row["Age"])
            gender = row["Gender"]
            education = row["Education Level"]
            monthly_earnings = float(row["Monthly Earnings (USD Est)"])
            is_unemployed = row["Occupation"] == "Unemployed"

            # Task 1: Filter and calculate Government Fund and Passive Earnings
            total_earnings = calculate_fund_and_earnings(age, education, monthly_earnings)
            if total_earnings > 0:
                eligible_for_gov_fund.append((row, total_earnings))

            # Task 2: Filter for the Government Seed Fund
            if is_unemployed and monthly_earnings == 0:
                eligible_for_seed_fund.append(row)

            # Task 3: Calculate totals of Females and Males in different age groups
            if gender == "Female":
                females_by_age_groups = calculate_age_group_totals(reader)
            elif gender == "Male":
                males_by_age_groups = calculate_age_group_totals(reader)

            # Task 4: Filter females under 21 for UNICEF Sanitary Towels Program
            if gender == "Female" and age < 21:
                unicef_program.append(row)

    # Task 5: Print out the results
    print("Government Fund for the Elderly:")
    for person, total_earnings in eligible_for_gov_fund:
        print(f"Person: {person['Name']}, Total Earnings: ${total_earnings:.2f}")

    print("\nGovernment Seed Fund:")
    for person in eligible_for_seed_fund:
        print(f"Person: {person['Name']}")

    print("\nFemales by Age Groups:")
    for age_group, count in females_by_age_groups.items():
        print(f"{age_group}: {count}")

    print("\nMales by Age Groups:")
    for age_group, count in males_by_age_groups.items():
        print(f"{age_group}: {count}")

    print("\nFemales under 21 for UNICEF Sanitary Towels Program:")
    for person in unicef_program:
        print(f"Person: {person['Name']}")

if __name__ == "__main__":
    main()
