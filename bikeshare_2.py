import time
import pandas as pd


# Colors functions
def prRed(skk): print("\033[91m{}\033[00m".format(skk))


def prCyan(skk): print("\033[96m{}\033[00m".format(skk))


def prGreen(skk): print("\033[92m{}\033[00m".format(skk))


# To deal with the files easier
CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """Returns the City(str) and month(str) and day(str)."""

    print('Hello! Let\'s explore some US bike-share data!\n')

    # ------------------------ City Choice ---------------------------------

    while True:
        # Get user input for city
        prGreen('Which city do you want to explore?')
        city = input('-Chicago\t-New York City\t-Washington\n')
        city = city.lower().strip()

        # Checking user input
        if city in ['chicago', 'new york city', 'washington']:
            break

        # If the user did not enter the correct string
        else:
            prRed('This is not a city, Try again!!\n')

    # ------------------------ Month & Day Choices ---------------------------------

    while True:
        try:
            # get user filter
            prGreen('Do you like to apply a filter?\t(please enter the number)')
            filters = int(input('1.No filter\t\t2.By month\t\t3.By day\t\t4.Both\n'))

        # If the user did not enter an integer
        except ValueError:
            prRed('Not a number, Try again!!\n')

        # Did not catch a ValueError
        else:
            if filters in [1, 2, 3, 4]:
                # initial value
                month = 'None'
                day = 'None'
                if filters in [2, 4]:
                    month = months()
                if filters in [3, 4]:
                    day = days()
                break

            # If the user did not enter the correct integer
            else:
                prRed('Not a valid number, Try again!!\n')

    # ------------------------ Stats Choice ---------------------------------

    while True:
        try:
            # get user filter
            prGreen('\nWhich Stats Data Do You Want To See? (please enter a number)')
            stats_choice = int(
                input('1.Frequent times\t2.Popular stations\t3.Trip durations\t4.Users stats\t5.All stats\n'))

        # If the user did not enter an integer
        except ValueError:
            prRed('Not a number, Try again!!\n')

        # Did not catch a ValueError
        else:
            if stats_choice in [1, 2, 3, 4, 5]:
                break

            # If the user did not enter the correct integer
            else:
                prRed('Not a valid number, Try again!!\n')

    print('-' * 40)
    return city, month, day, stats_choice


def months():
    """Converting the user input from an integer to a string
       Returns month(str)"""

    while True:
        try:
            # get user filter for the month
            prGreen('Pick a month?\t(please enter a number)')
            p = int(input('1.January\t\t2.February\t\t3.March\t\t4.April\t\t5.May\t\t6.June\n'))

        # If the user did not enter an integer
        except ValueError:
            prRed('Not a number, Try again!!\n')

        # Did not catch a ValueError
        else:
            if p in [1, 2, 3, 4, 5, 6]:
                if p == 1:
                    return 'January'
                elif p == 2:
                    return 'February'
                elif p == 3:
                    return 'March'
                elif p == 4:
                    return 'April'
                elif p == 5:
                    return 'May'
                elif p == 6:
                    return 'June'
                break

            # If the user did not enter the correct integer
            else:
                prRed('Not a valid number, Try again!!\n')


def days():
    """ Converting the user input from an integer to a string
        Returns day(str)"""

    while True:
        try:
            # get user filter for day
            prGreen('Pick a day of week?\t(please enter a number)')
            p = int(input('1.Sunday\t\t2.Monday\t\t3.Tuesday\t\t4.Wednesday\t\t5.Thursday\t\t6.Friday\t\t7.Saturday\n'))

        # If the user did not enter an integer
        except ValueError:
            prRed('Not a number, Try again!!\n')

        # Did not catch a ValueError
        else:
            if p in [1, 2, 3, 4, 5, 6, 7]:
                if p == 1:
                    return 'Sunday'
                elif p == 2:
                    return 'Monday'
                elif p == 3:
                    return 'Tuesday'
                elif p == 4:
                    return 'Wednesday'
                elif p == 5:
                    return 'Thursday'
                elif p == 6:
                    return 'Friday'
                elif p == 7:
                    return 'Saturday'
                break

            # If the user did not enter the correct integer
            else:
                prRed('Not a valid number, Try again!!\n')


def stats(stats_choice, df, city, h):
    """Filtering the request of the user
       Arguments: stats_choice(int), df(DataFrame), city(str), h(int)"""

    if stats_choice in [1, 5]:
        time_stats(df, h)
    if stats_choice in [2, 5]:
        station_stats(df, h)
    if stats_choice in [3, 5]:
        trip_duration_stats(df)
    if stats_choice in [4, 5]:
        user_stats(df, city, h)


def load_data(city, month, day):
    """ Loading data to the DataFrame
       Arguments: city(str),month(str),day(str)
       Returns: DataFrame as df(DataFrame)"""

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'None':
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'None':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day]

    return df


def time_stats(df, h):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # -------------- Display the most common month --------------

    # creating a DataFrame
    popular_month = pd.DataFrame(df['month'].value_counts())
    popular_month = popular_month.rename(columns={'month': 'Count'})

    # print
    prCyan('Most Frequent Start month:')
    print(popular_month.head(h), '\n')

    # -------------- Display the most common day of week --------------

    # creating a DataFrame
    popular_day = pd.DataFrame(df['day_of_week'].value_counts())
    popular_day = popular_day.rename(columns={'day_of_week': 'Count'})

    # print
    prCyan('Most Frequent Start day:')
    print(popular_day.head(h), '\n')

    #  -------------- Display the most common start hour --------------

    # creating a DataFrame
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = pd.DataFrame(df['hour'].value_counts())
    popular_hour = popular_hour.rename(columns={'hour': 'Count'})

    # print
    prCyan('Most Frequent Start Hour:')
    print(popular_hour.head(h))

    prGreen("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df, h):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # -------------- Display most commonly used start station --------------

    # creating a DataFrame
    start_station = pd.DataFrame(df['Start Station'].value_counts())
    start_station = start_station.rename(columns={'Start Station': 'Count'})

    # print
    prCyan('Commonly Used Start Station:')
    print(start_station.head(h), '\n')

    # -------------- Display most commonly used end station --------------

    # creating a DataFrame
    end_station = pd.DataFrame(df['End Station'].value_counts())
    end_station = end_station.rename(columns={'End Station': 'Count'})

    # print
    prCyan('Commonly Used End Station:')
    print(end_station.head(h), '\n')

    # -------------- Display most frequent combination of start station and end station trip --------------

    # creating a DataFrame
    df['Combination'] = df['Start Station'] + ' To ' + df['End Station']
    combination = pd.DataFrame(df['Combination'].value_counts())
    combination = combination.rename(columns={'Combination': 'Count'})

    # print
    prCyan('Most Frequent Combination Stations:')
    print(combination.head(h), '\n')

    prGreen("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # -------------- Display total travel time --------------

    # calculating the sum
    total = df['Trip Duration'].sum()

    # print
    prCyan('Total Travel Time:')
    print(total, '\n')

    # -------------- Display mean travel time --------------

    # calculating the mean
    average = df['Trip Duration'].mean()

    # print
    prCyan('Average Travel Time:')
    print(average)

    prGreen("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df, city, h):
    """Displays statistics on bike-share users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    #  -------------- Display counts of user types --------------

    # creating a DataFrame
    user_types = pd.DataFrame(df['User Type'].value_counts())
    user_types = user_types.rename(columns={'User Type': 'Count'})

    # print
    prCyan('User Types:')
    print(user_types, '\n')

    #  -------------- Display counts of gender --------------

    # washington city has no information about the gender and birth year
    if city != 'washington':
        # creating a DataFrame
        gender = pd.DataFrame(df['Gender'].value_counts())
        gender = gender.rename(columns={'Gender': 'Count'})

        # print
        prCyan('Gender:')
        print(gender, '\n')

        #  -------------- Display earliest, most recent, and most common year of birth --------------

        # get the earliest
        earliest = df['Birth Year'].min()

        # print
        prCyan('Earliest Year Of Birth:')
        print(earliest, '\n')

        # get the most recent
        recent = df['Birth Year'].max()

        # print
        prCyan('Most Recent Year Of Birth:')
        print(recent, '\n')

        # creating a DataFrame
        common = pd.DataFrame(df['Birth Year'].value_counts())
        common = common.rename(columns={'Birth Year': 'Count'})

        # print
        prCyan('Most Common Year Of Birth:')
        print(common.head(h))

    prGreen("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def main():
    while True:
        city, month, day, stats_choice = get_filters()
        df = load_data(city, month, day)

        # Using h as a counter
        h = 0
        while True:
            # Increment h to display the next 5 raw data
            h = h + 5

            # Stats filter
            stats(stats_choice, df, city, h)

            # Print filters
            prCyan('\nFiltered by:')
            print('City:', city, '\tMonth:', month, '\tDay:', day, '\tTop ', h)

            # Asking the user to display the next 5 data
            prGreen('\nDo you want to see more 5 lines of raw data?')
            more = input('Enter yes or no.\n')
            if more.lower() != 'yes':
                break

        # Asking the user to restart
        prGreen('\nWould you like to restart?')
        restart = input('Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
