### Algorithm for Lab2:

1. **Output** the purpose of the program: "This program computes the change in population of a country over time.
2. **Initialize** constant `SECONDS_PER_YEAR` to `31536000` (number of seconds in a year).


1. Prompt user to enter the birth rate (number of seconds between births) and store it in `birth_rate`.
1. Prompt user to enter the death rate (number of seconds between deaths) and store it in `death_rate`.
1. Prompt user to enter the migration rate (number of seconds between immigrations) and store it in `migration_rate`.
1. Prompt user to enter the current population and store it in `current_population`.
1. Prompt user to enter the number of years in the future for the prediction and store it in `future_years`.

4. **Calculate** the future population using the formula: `$future\_population = (((SECONDS_PER_YEAR / birth_rate) -
                      (SECONDS_PER_YEAR / death_rate) +
                      (SECONDS_PER_YEAR / migration_rate)
                     ) * future_years
                    ) + current_population$`

4. Convert `future_population` to an integer.
5. **Output** the future population: Output "The population in `future_years` year(s) will be `future_population`."

6. **Determine** the population change:
7.  **If** `future_population` is greater than `current_population`:
    1. Output "The population increased."
1. **Otherwise if** `future_population` is less than `current_population`:
    1. Output "The population decreased."
1. **Otherwise**:
    1. Output "The population remains the same."
7. **End** program:Output "Thank you for using my simple program."
