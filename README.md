# **Explore US Bikeshare Data Project**
---

## **Project overview**
---
- **In this project, we will use Python to explore data related to bike share systems for three major cities in the United States:**

- **Chicago, New York City, and Washington.**

- **writing a code to import the data and answer interesting questions about it by computing descriptive statistics.**

- **writing a script that takes in raw input to create an interactive experience in the terminal to present these statistics.**

---
## **Software requirements**
---
- **Python 3, NumPy, and pandas installed using Anaconda.**
- **A text editor, like Sublime or Atom.**
- **A terminal application (Terminal on Mac and Linux or Cygwin on Windows).**

---
## **The Datasets**
---
**Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same core six (6) columns:**

##### 1. Start Time (e.g., 2017-01-01 00:07:57)
##### 2. End Time (e.g., 2017-01-01 00:20:53)
##### 3. Trip Duration (in seconds - e.g., 776)
##### 4. Start Station (e.g., Broadway & Barry Ave)
##### 5. End Station (e.g., Sedgwick St & North Ave)
##### 6. User Type (Subscriber or Customer)

#### **Chicago and New York City files also have the following two columns:**


#### 7. Gender
#### 8. Birth Year

---
## **Statistics Computed**
---
**The program should help the user to learn about bike share use in Chicago, New York City, and Washington by computing a variety of descriptive statistics.** 

**The code output should provide the following information:**

#### 1. Popular times of travel (i.e., occurs most often in the start time)

- most common month
- most common day of week
- most common hour of day

#### 2. Popular stations and trip

- most common start station
- most common end station
- most common trip from start to end (i.e., most frequent combination of start station and end station)

#### 3. Trip duration

- total travel time
- average travel time

#### 4. User info

- counts of each user type
- counts of each gender (only available for NYC and Chicago)
- earliest, most recent, most common year of birth (only available for NYC and Chicago)

---
## **Files**
---
#### 1. US_Bikeshare.ipynp

#### 2. chicago.csv

#### 3. new_york_city.csv

#### 4. washington.csv

---
## **Interactive Experience**
---
**The code is set up as a script that takes in raw input to create an interactive experience in the terminal that answers questions about the dataset.**

**The experience is interactive because depending on a user's input, the answers to the questions on the previous page will change! There are four questions that will change the answers:**

#### 1. Would you like to see data for Chicago, New York, or Washington?
#### 2. Would you like to filter the data by month, day, or not at all?
#### 3. (If they chose month) Which month - January, February, March, April, May, or June?
#### 4. (If they chose day) Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?


**The answers to the questions above will determine the city and timeframe on which you'll do data analysis.**

>After filtering the dataset, users will see the statistical result of the data, and choose to start again or exit.

---
## **Additional**
---
**The program has additional features:**

#### 1. The user will be given a menu to choose from, To avoid mistyping or misspelling.
#### 2. The program will display the top 5 in each statistics and the user will have the choice to display the next 5 statistics. 
#### 3. Filter for which statistics to display.
#### 4. The filter choosen will be displayed with the output.
#### 5. Using colors for great user experience.

---
## **Code Walkthrough**
---
- **get_filters():** to get the user filter, and to make sure the input is valid

- **months():** The user will enter the number of the month and this function will convert it to the corresponding string.

- **days():** The user will enter the number of 'day of week' and this function will convert it to the corresponding string. 

>- Example: if the user entered 1 then it is Sunday, 2 is monday ..... 7 is Saturday

- **stats():** The user will enter which statistics to display and this function will help us by filtering.

- **load_data():** creating the filtered DataFrame 

- **time_stats(df,h):** Calculating the most common **month**, **day** and **hour**

- **station_stats(df,h):** Calculating the most popular **start station**, **end station** and the **combination** of start and end

- **trip_duration_stats(df):** Calculating the **total and mean** travel time

- **user_stats(df, city, h):**

    - Calculating the count of **user types** for **NYC**, **chicago** and **washington**.

    - Calculating the count of **gender** and calculate the **earliest**, **most recent** and **most common** date of birth for **NYC** and **chicago** only.

- **main():** the main function

    - we get **user filters** to create the appropriate **DataFrame**.

    - **h** is a counter for the **head()**.

    - calling **stats(st, df, city, h)** function with the **DataFrame** and **filters** as **arguments**.

    - **Asking the user** to display the **next 5 data** or to **restart the program**


