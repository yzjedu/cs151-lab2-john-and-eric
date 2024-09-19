[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/cjPA34Da)
# Lab2
Grade EMRN  
Due: Before the next lab

## Purpose 

This lab gives you practice with input, output, math, writing algorithms and test cases, and using human computer interaction's usability guidelines for your input and output. You will use your decision making skills to state of the population increased or decreased.

## Problem
Every country has a change in population over time, either up or down. Population change is primarily due to three causes: births, deaths, and immigration. Create a program that will determine the expected population in the future (a certain number of years away) for a country based on a current population amount if you are given (1) how often someone is born (in seconds), (2) how often someone dies (in seconds), and (3) how often a new immigrant joins the country (in seconds).

## Details
Your program must work for ANY country, with ANY non-zero rate of change.

An example to help you understand the problem, the U.S. Census provides information on its web page (http://www.census.gov/popclock/) about the current U.S. population as well as approximate rates of change over time. The rates of change are as follows:  
* There is a new birth every 8 seconds
* There is a death every 12 seconds
* There is a new immigrant every 126 seconds.

Your calculations should assume that there are always 365 days in a year.

Your program must ask for the following as *input*: the birth rate in terms of how many seconds between births, the death rate in seconds, the rate of new immigrants in seconds, the current population, and how many years into the future the user wants to know the population.

Your program must give the expected population in the future as an integer as output. (Keep results as floats until after all calculations have been performed, as otherwise your answer will be incorrect.)

Your program will state if the population has increased or decreased. 

As an example, running the program with the numbers provided above might look like:
```
> How many seconds between births? 8
> How many seconds between deaths? 12
> How many seconds between immigrations? 126
> What is the current population? 333100360
> How many years in the future? 5
> The US population in 5 years will be 340921788
> The population increased
```

## Reminders  

1. Follow good programming practices.
2. Follow the process below, including meeting all detailed requirements.
3. Always output a statement of the purpose of the program at the beginning.
4. Properly use variables, input, math, and output.
5. Complete a set of test cases, and use them to test that your program works correctly. Fix any errors.
6. Remember to perform pair programming. When ½ the code is written, or ½ of class is over, switch drivers.

## Process 
0.  Notify your instructor if you find any discrepancies on the `README.md` file.    
1.	Make sure you understand the problem you are being asked to solve. A key aspect to understanding the problem is figuring out what exactly you need to calculate.
2. **HINT:** You will need to figure out how many births, deaths, and immigrants have joined the country in a given year. You may find it useful to calculate how many seconds are in a year, store it in a variable, and then use that value when necessary in your calculations. 
3.	Write a set of 5 test cases in `test_cases.xlsx` – you should include the example from above as one of your test cases. Think back to last week’s lab for the other types of test cases you should include. Don't forget that a population may not always increase over time. Follow the same format as Lab 1’s test cases.
4.	Write an algorithm for your calculations in `algorithm.docx`. Make sure you follow all requirements. Use a calculator to test your algorithm with the test case values to make sure it solves the problem correctly. Show your algorithm to the lab instructor and get his/her approval BEFORE you start writing code.
5.	Use the `main.py` Python file, and follow your approved algorithm to write your code. You should assume that all input are floats.
6.	Fix syntax errors: Run your program and fix any errors that appear.
7.	Test: Once your code runs, and you think it’s complete, test it using your test cases -- run, give the input as input, and see if you get the right output.
8.	Make sure you’ve created a human-readable essay (i.e. your program). Did you follow the code readability guidelines from Class Notes #3? If not, fix your code so that it is readable. You should have comments above each chunk of code!
9.	Make sure you’ve used good Usability – have you followed the usability guidelines from the HCI class (Notes #5) for your input and output?
10.	Include an updated version of the intro comments from `Lab 0` at the very top of your Python file. Almost every line should change! 
11.	Once you are done in lab, make sure you commit and push or your instructor won't be able to view it.

## What to Submit in GitHub:

1. Completed `main.py` file  
2. `algorithm.docx`
3. An Excel file with your test cases.  
    - Edit the `test_cases.xlsx` file with Excel software 
    - If it can open then ok. Otherwise
      - Right click on `test_cases.xlsx` -> Open In -> Associated Application
4. `RD1.docx` -> Reflection for Drive 1
5. `RD2.docx` -> Reflection for Drive 2

**As a reminder, reflections count toward your participation grade.**

Type the Reflection INSIDE the respective Word file and addressing the following questions:

 - Objective:
   - What were you supposed to learn/accomplish?

 - Procedure:
   - What steps were followed and what techniques did you use to solve the problem?
   - What were the Key concepts explored?

 - Results:
   - Did your results match what you expected to get? 
   - Did you try using various test cases, or extreme test cases?
  
 - Reflection:
   - What challenges did you encounter? 
   - How did you follow the first 3 rules of programming?
   - Did you overcome them, and how? 
   - Any key takeaways? 
   - Do you think you learned what you were supposed to learn for this lab? 
   - What was it like working with your partner?