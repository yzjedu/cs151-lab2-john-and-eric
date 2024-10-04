# Programmers: [Your Name]
# Course: CS151, [Instructor's name]
# Due Date: 9/XX/2024
# Lab Assignment: 2
# Problem Statement: This program computes the change in population of a country over time.
# Data In: birth rate, death rate, migration rate, current population, number of years into the future of a nation
# Data Out:  Future population, and whether it has increased, decreased, or remaind the same

# Display purpose of the program
print('_' * 75)
print('This program computes the change in population of a country over time.')
print('_' * 75)
print()

# Store variable to represent number of seconds per year
SECONDSS_PER_YEAR = 31536000

# Prompt user to enter data for the nation.
birth_rate = float(input('\t How many seconds between births? '))
death_rate = float(input('\t How many seconds between deaths? '))
migration_rate = float(input('\t How many seconds between immigrations? '))
current_population = float(input('\t What is the current population? '))
future_years = float(input('\t How many years in the future? '))

# Calculate future population
future_population = (
                     ((SECONDSS_PER_YEAR / birth_rate) - 
                      (SECONDSS_PER_YEAR / death_rate) +
                      (SECONDSS_PER_YEAR / migration_rate)
                     ) * future_years
                    ) + current_population

future_population = int(future_population)

# Output future population to user
print ('\t The population in', int(future_years), 'year/s will be', future_population)

# Determine whether future population has decreased, increased, or remained the same
if future_population > current_population:
    print('\t The population increased.')
elif future_population < current_population:
    print('\t The population decreased.')
else:
    print('\t The population remains same.')

# Thank user for using the program
print('_' * 75)
print('Thank you for using my simple program')
print('_' * 75)