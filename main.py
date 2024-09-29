# Programmed by John Elehwany and Eric Thomas
# Loyola CS151, Professor Zee
# Due Date: 9/25/24
# Lab Assignment: 02

# This program determines the change in population by asking for the seconds between birth, death, and immigration. It also asks for the current population and future projection years. With this info, it calculates whether the population has increased or decreased within the given amount of future years.

# DATA IN

print("""
Change in Population Calculator
""")

# Asks the user to input the amount of seconds in between each birth of someone
SecondsBetweenBirth = int(input('Input the number of seconds between each birth: '))
# Asks the user to input the amount of seconds in between each death of someone
SecondsBetweenDeath = int(input('Input the number of seconds between each death: '))
# Asks the user to input the amount of seconds in between each immigration
SecondsBetweenImmigration = int(input('Input the number of seconds between each immigration: '))
# Asks the user to input the current population of the country
CurrentPopulation = int(input('Input the current population: '))
# Asks the user to input the number of years in the future projections
FutureProjectionYears = int(input('Input the number of future projection years: '))


# PROCESSING

# Total seconds value; calculated by the future projection years multiplied by the number of seconds in a year
total_seconds = (FutureProjectionYears * 365 * 24 * 60 * 60)
# Total births value; done by dividing the total seconds by the seconds between each birth
total_births = (total_seconds / SecondsBetweenBirth)
# Total deaths value; done by dividing the total seconds by the seconds between each death
total_deaths = (total_seconds / SecondsBetweenDeath)
# Total immigrations value; done by dividing the total seconds by the seconds between each immigration
total_immigration = (total_seconds / SecondsBetweenImmigration)

# Future population value; Adds the total births and immigration to the current population, then subtracts the deaths
future_population = (CurrentPopulation + (total_births + total_immigration) - total_deaths)
# Population change; Future population minus current population
population_change = future_population - CurrentPopulation

# OUTPUT

# Checks for positive or negative change, and outputs the increase in population, as well as the future population
if population_change > 0:
    print("""
    The population increased by""", int(population_change), "and the future population will be", int(future_population))
elif population_change < 0:
    print("""
    The population decreased by""", int(-population_change), "and the future population will be", int(future_population))

