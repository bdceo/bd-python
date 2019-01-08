import time
import pandas as pd

CITY_DATA = {'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv'}
support_months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
support_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']


def get_input(tips, err, support_input):
    """
    Asks user to input some keywords for analyze.

    Returns:
        (str) input - support input
    """
    info = input(tips).lower()
    while info not in support_input:
        print(err, info)
        info = input(tips).lower()
    return info


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    # city = input('Would you like to see data for Chicago, New York, or Washington?').lower()
    # while CITY_DATA.get(city) is None:
    #     print('Sorry! city not support :', city)
    #     city = input('Would you like to see data for Chicago, New York, or Washington?').lower()
    city = get_input('Would you like to see data for Chicago, New York, or Washington?',
                     'Sorry! city not support :', CITY_DATA.keys())

    # get user input for month (all, january, february, ... , june)
    # month = input('Which month? all, january, february, ... , june?').lower()
    # while (month != 'all') & (month not in support_months):
    # while month not in (support_months + ['all']):
    #     print('Sorry! month not support :', month)
    #     month = input('Which month? all, january, february, ... , june?').lower()
    month = get_input('Which month? all, january, february, ... , june?',
                      'Sorry! month not support :', (support_months + ['all']))

    # get user input for day of week (all, monday, tuesday, ... sunday)
    # day = input('Which day? all, monday, tuesday, ... sunday?').lower()
    # while (day != 'all') & (day not in support_days):
    # while day not in (support_days + ['all']):
    #     print('Sorry! day not support:', day)
    #     day = input('Which day? all, monday, tuesday, ... sunday?').lower()
    day = get_input('Which day? all, monday, tuesday, ... sunday?',
                    'Sorry! day not support:', (support_days + ['all']))

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
    """
    df = pd.read_csv(CITY_DATA.get(city))
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['dayofweek'] = df['Start Time'].dt.dayofweek
    if month != 'all':
        month = support_months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        day = support_days.index(day)
        df = df[df['dayofweek'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    month = df['month'].mode()[0]
    print('the most common month:', support_months[month-1].title())

    # display the most common day of week
    day = df['dayofweek'].mode()[0]
    print('the most common day of week:', support_days[day].title())

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    hour = df['hour'].mode()[0]
    print('the most common start hour:', hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print('the most commonly used start station:', start_station)

    # display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print('the most commonly used end station:', end_station)

    # display most frequent combination of start station and end station trip
    # df['Trip Line'] = 'from ' + df['Start Station'] + ' to ' + df['End Station']
    # trip_line = df['Trip Line'].mode()[0]
    # print('most frequent combination of start station and end station trip:', trip_line)
    top_line = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print("The most frequent combination of start station and end station trip is {} to {}"
          .format(top_line[0], top_line[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total = df['Trip Duration'].sum()
    print('total travel time(seconds):', total)

    # display mean travel time
    mean = df['Trip Duration'].mean()
    print('mean travel time(seconds):', mean)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('counts of user types:\n', user_types)

    # Display counts of gender
    if 'Gender' in df:
        genders = df['Gender'].value_counts()
        print('counts of gender:\n', genders)
    else:
        print('data has no Gender')

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest = df['Birth Year'].min()
        recent = df['Birth Year'].max()
        common = df['Birth Year'].mode()[0]
        print('earliest year is {}, most recent year is {}, and most common year is {}'
              .format(earliest, recent, common))
    else:
        print('data has no Birth Year')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()

