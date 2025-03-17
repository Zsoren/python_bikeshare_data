import pandas as pd
import calendar as cal
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_user_input():
    """
    Gives users prompts to answer questions

    Returns:
        city - the name of the city that the user wants to look at data for
        month_filter - the month the user wants to filter the data buy (can be an empty string)
        day_filter - the day of the week the user wants to filter the data buy (can be an empty string)
    """
    print("Hello! Let's explore some US bikeshare data!")
    
    city = input("\nWould you like to see data for Chicago, New York City, or Washington?\n").lower()
    # checks if the city input was a valid city, and if not, asks user to retry.
    while True:
        if city not in ('chicago', 'new york city', 'washington'):
            city = input("\nOops! Looks like that's not a valid city. Please enter one of these city names: Chicago, New York City, or Washington\n").lower()
        else:
            break

    filter_choice = input('\nWould you like to filter the data by month, day, or not at all? (enter "no" if you don\'t want to filter.\n').lower()
    # checks if the filter input was a valid option, and if not, asks user to retry.
    while True:
        if filter_choice not in ('month', 'day', 'no'):
            filter_choice = input("\nOops! Looks like that's not a valid entry. Please enter one of these filter options: Month, Day, or No\n").lower()
        else:
            break

    # sets empty string for month and day filter in case the user doesn't want to filter by one or the other (or both)
    month_filter = ''
    day_filter = ''

    # changes user prompts depending on if they are filtering by month, day, or none
    if filter_choice == 'month':
        month_filter = input('\nWhich month - January, February, March, April, May, or June?\n').lower()
        # checks if the month option was a valid choice, and if not, asks user to retry.
        while True:
            if month_filter not in ('january', 'february', 'march', 'april', 'may', 'june'):
                month_filter = input("\nOops! Looks like that's not a valid entry. Please enter one of the following months: January, February, March, April, May, or June\n").lower()
            else:
                break
    elif filter_choice == 'day':
        day_filter = input('\nWhich day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?\n').lower()
        # checks if the day option was a valid choice, and if not, asks user to retry.
        while True:
            if day_filter not in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
                day_filter = input("\nOops! Looks like that's not a valid entry. Please enter one of the following days: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday\n").lower()
            else:
                break

    return city, month_filter, day_filter


def filter_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or an empty string to apply no month filter
        (str) day - name of the day of week to filter by, or an empty string to apply no day filter
    Returns:
        df - pandas DataFrame containing city data filtered by month and day
    """
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != '':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df.loc[df['month'] == month]

    # filter by day of week if applicable
    if day != '':
        # filter by day of week to create the new dataframe
        df = df.loc[df['day_of_week'] == day.title()]
    
    return df


def time_stats(df):
    ''' displays stats on most popular times of travel '''
    print('\nTime Stats')

    # most common month calculation
    popular_month = cal.month_abbr[df['month'].mode()[0]]
    print('The most common month to travel is: {}'.format(popular_month))

    # most common day of the week calculation
    popular_day = df['day_of_week'].mode()[0]
    print('The most common day of the week to travel is: {}'.format(popular_day))

    # most common hour of the day calculation
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    time_period = ''
    if popular_hour > 12:
        popular_hour -= 12
        time_period = 'p.m.'
    else:
        time_period = 'a.m'
    print('The most common hour of the day to travel is: {} {}'.format(popular_hour, time_period))

def station_stats(df):
    ''' displays stats on most popular stations and trips '''
    print('\nStation Stats')

    # most common start station calculation
    popular_start = df['Start Station'].mode()[0]
    print('The most common start station is: {}'.format(popular_start))

    # most common end station calculation
    popular_end = df['End Station'].mode()[0]
    print('The most common end station is: {}'.format(popular_end))

    # most common full trip calculation
    df['Trip'] = df['Start Station'] + ' to ' + df['End Station']
    popular_trip = df['Trip'].mode()[0]
    print('The most common trip from start to end is: {}'.format(popular_trip))


def trip_stats(df):
    ''' displays stats on trip duration '''
    print('\nTrip Stats')

    # total travel time calculation
    total_travel_time = df['Trip Duration'].sum()
    total_days = total_travel_time // 86400
    total_hours = (total_travel_time % 86400) // 3600
    total_minutes = ((total_travel_time % 86400) % 3600) // 60
    total_seconds = (((total_travel_time % 86400) % 3600) % 60) % 60
    print('The total travel time of users was: {} days {} hours {} minutes and {} seconds'.format(total_days, total_hours, total_minutes, total_seconds))

    # average travel time calculation
    avg_travel_time = df['Trip Duration'].mean()
    avg_minutes = int(avg_travel_time // 60)
    avg_seconds = int((avg_travel_time % 60) % 60)
    print('The average travel time of users was: {} minutes and {} seconds'.format(avg_minutes, avg_seconds))


def user_stats(df, city):
    ''' displays stats on the app's users '''
    print('\nUser Stats')

    # count of each user type calculation
    user_types = df['User Type'].value_counts()
    subscribers = user_types.iloc[0]
    customers = user_types.iloc[1]
    print('The counts of each user type were {} Subscribers and {} Customers'.format(subscribers, customers))

    # checks if we are looking at data from Chicago or New York City, as these stats are only provided for those cities
    if city in ('chicago', 'new york city'):
        # count of each gender calculation
        genders = df['Gender'].value_counts()
        males = genders.iloc[0]
        females = genders.iloc[1]
        print('The counts of each gender were {} Males and {} Females'.format(males, females))

        # the earliest birth year calculation
        early_birth = int(df['Birth Year'].min())
        print('The earliest birth year of a user was: {}'.format(early_birth))

        # the most recent birth year calculation
        recent_birth = int(df['Birth Year'].max())
        print('The most recent birth year of a user was: {}'.format(recent_birth))

        # the most common birth year calculation
        popular_birth = int(df['Birth Year'].mode()[0])
        print('The most common birth year of a user was: {}'.format(popular_birth))


def raw_data(df):
    '''
    asks the user if they would like to see the raw data. If they do, it provides them with 5 rows of that data. It then asks them if they would like to see more raw data, and will provide it on a positive answer. It loops through this process until receiving a 'no'.
    '''
    see_data = input('\nWould you like to see some raw data? Yes or No?\n').lower()
    while True:
        if see_data not in ('yes', 'no'):
            see_data = input("\nOops! Looks like that's not a valid entry. Please enter Yes or No\n").lower()
        else:
            break

    counter = 0
    while see_data == 'yes':
        print(df.iloc[counter:counter + 5])
        counter += 5

        see_data = input('\nWould you like to see some more raw data? Yes or No?\n').lower()
        while True:
            if see_data not in ('yes', 'no'):
                see_data = input("\nOops! Looks like that's not a valid entry. Please enter Yes or No\n").lower()
            else:
                break


def main_func():
    while True:
        city, month_filter, day_filter = get_user_input()
        df = filter_data(city, month = month_filter, day = day_filter)

        time_stats(df)
        station_stats(df)
        trip_stats(df)
        user_stats(df, city)
        raw_data(df)


        restart = input('\nWould you like to restart? Yes or No?\n').lower()
        while True:
            if restart not in ('yes', 'no'):
                restart = input("\nOops! Looks like that's not a valid entry. Please enter Yes or No\n").lower()
            else:
                break

        if restart.lower() != 'yes':
            break


main_func()