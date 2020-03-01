import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ('chicago', 'new york city', 'washington')
    while True:
        city = input('Please choose city from Chicago, New York City or Washington: ').lower()
        if city in cities:
              break

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ('all', 'january', 'february', 'march', 'april', 'may', 'june')
    while True:
        month = input('Please enter the desired month from all or January thru June: ').lower()
        if month in months:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    week_days = ('all', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday')
    while True:
        day = input('Please enter desired day of week from all or Sunday thru Saturday: ').lower()
        if day in week_days:
            break

    print('-'*40)

    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    Note to project evaluator: function extracted from practice problem #3, Load and Filter Data Set
    """
    # Create dataframe from data
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('\nThe most common month is', common_month)
    # TO DO: display the most common day of week
    common_day_of_week = df['day_of_week'].mode()[0]
    print('\nThe most common day of week is', common_day_of_week)

    # TO DO: display the most common start hour
    common_start_hour = df['hour'].mode()[0]
    print('\nThe most common start hour is', common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('\nThe most commonly used start station is', common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('\nThe most commonly used end station is', common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    common_start_end_station = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print('\n The most frequent start-end station combination is:\n', common_start_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('\nThe total travel time is', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('\nThe mean travel time is', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('\nThe user types are:\n',user_types)

    # TO DO: Display counts of gender

    while 'Gender' == True:
        genders = df['Gender'].value_counts()

        print('\nThe gender count is:', genders)

    # TO DO: Display earliest, most recent, and most common year of birth
    while 'Birth Year' == True:
        birth_year = df['Birth Year']
        youngest = birth_year.max()
        oldest = birth_year.min()
        most_common_BY = birth_year.mode()[0]
        print('\nThe most recent birth year is:', youngest)
        print('\nThe earliest birth year is:', oldest)
        print('\nThe most common birth year is:', most_common_BY)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_raw_data(df):
    """Displays 5 raw data rows at a time."""
    x = 5
    y = 10
    while True:
        raw_display = input('\nWould you like to see 5 rows of raw data? Enter yes or no.\n')
        if raw_display.lower() != 'yes':
            break
        print(df.head())

        # Ask for additional 5 rows, if not then we exit the display_raw_data function
        while True:
            more_rows = input('\nLike to see 5 more rows of raw data? Enter yes or no.\n')
            if more_rows.lower() != 'yes':
                break
            print(df[x:y])
            x += 5
            y = x + 5
        break




def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        display_raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
