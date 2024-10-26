import sys

def parse_nyt_data(file_path=''):
    """
    Parse the NYT covid database and return a list of tuples. Each tuple describes one entry in the source data set.
    Date: the day on which the record was taken in YYYY-MM-DD format
    County: the county name within the State
    State: the US state for the entry
    Cases: the cumulative number of COVID-19 cases reported in that locality
    Deaths: the cumulative number of COVID-19 death in the locality

    :param file_path: Path to data file
    :return: A List of tuples containing (date, county, state, cases, deaths) information
    """
    # data point list
    data=[]

    # open the NYT file path
    try:
        fin = open(file_path)
    except FileNotFoundError:
        print('File ', file_path, ' not found. Exiting!')
        sys.exit(-1)

    # get rid of the headers
    fin.readline()

    # while not done parsing file
    done = False

    # loop and read file
    while not done:
        line = fin.readline()

        if line == '':
            done = True
            continue

        # format is date,county,state,fips,cases,deaths
        (date,county, state, fips, cases, deaths) = line.rstrip().split(",")

        # clean up the data to remove empty entries
        if cases=='':
            cases=0
        if deaths=='':
            deaths=0

        # convert elements into ints
        try:
            entry = (date,county,state, int(cases), int(deaths))
        except ValueError:
            print('Invalid parse of ', entry)

        # place entries as tuple into list
        data.append(entry)


    return data

def first_question(data):

    """
    # Write code to address the following question: Use print() to display your responses.
    # When was the first positive COVID case in Rockingham County?
    # When was the first positive COVID case in Harrisonburg?
    :return:
    """
    """
    To determine when the first positive COVID case happened in Rockingham county and Harrisonburg city, I went 
    through the data and looked for the first moment where the number of cases was greater than zero for each
    county. Once I found the first case for each county, I printed the result and returned the function.
    """

    # dummy variables
    first_rockingham_VA = None
    first_harrisonburg = None

    # finding the date when the first positive COVID case happened
    for(date,county,state,cases,deaths) in data:

        if county == 'Rockingham' and state == 'Virginia' and cases > 0 and first_rockingham_VA is None:
            first_rockingham_VA = date
            print('') #(aesthetic purposes)
            print('QUESTION 1: The first positive Covid case in Rockingham County, VA was on: ', first_rockingham_VA)

        if county == 'Harrisonburg city' and cases > 0 and first_harrisonburg is None:
            first_harrisonburg = date
            print('') #(aesthetic purposes)
            print('QUESTION 1: The first positive Covid case in Harrisonburg City, VA was on: ', first_harrisonburg)

        if first_rockingham_VA and first_harrisonburg:
            return


def second_question(data):

    """
    # Write code to address the following question: Use print() to display your responses.
    # What day was the greatest number of new daily cases recorded in Harrisonburg?
    # What day was the greatest number of new daily cases recorded in Rockingham County?
    :return:
    """
    """
    I took the cases in the data which fit the geographic location I was looking for, and calculated the new cases 
    every day. Each day's new cases was compared to the previous day to determine the current highest number of new 
    cases in a day
    """

    #dummy variables
    max_cases_rockingham = 0
    max_cases_harrisonburg = 0
    max_date_rockingham = None
    max_date_harrisonburg = None
    prev_cases_rockingham = 0
    prev_cases_harrisonburg = 0

    # calculating new cases
    for (date,county,state,cases,deaths) in data:
        if county == 'Rockingham' and state == 'Virginia':
            new_cases = cases - prev_cases_rockingham # calculating new cases for rockingham county
            if new_cases > max_cases_rockingham:
                max_cases_rockingham = new_cases
                max_date_rockingham = date
            prev_cases_rockingham = cases # updating previous day's cases
        elif county == 'Harrisonburg city':
            new_cases = cases - prev_cases_harrisonburg #calculating new cases for harrisonburg city
            if new_cases > max_cases_harrisonburg:
                max_cases_harrisonburg = new_cases
                max_date_harrisonburg = date
            prev_cases_harrisonburg = cases # updating previous day's cases

    print('')  # (aesthetic purposes)
    print('QUESTION 2: The date with the greatest number of new cases reported in Rockingham County was:', max_date_rockingham)
    print('On', max_date_rockingham, 'there were', max_cases_rockingham, 'cases in Rockingham County')

    print('') #(aesthetic purposes)
    print('QUESTION 2: The date with the greatest number of new cases reported in Harrisonburg was:' , max_date_harrisonburg)
    print('On', max_date_harrisonburg, 'there were', max_cases_harrisonburg, 'cases in Harrisonburg')

    return


def third_question(data):

    # Write code to address the following question:Use print() to display your responses.
    # What was the worst 7-day period in either the city or county for new COVID cases?
    # This is the 7-day period where the number of new cases was maximal.
    """"
    I extracted the data from the dataset for each county. Then I created a list of cases in each county (along with
    the date, county and state). Finally, I iterated through each day, calculating new cases for each day and sum all
    the 7-day period, and then compared them to find the highest number of new cases in a 7-day period.
    """

    # data extraction
    rockingham_data = [(date, county, state, cases) for (date, county, state, cases, deaths) in data if county == 'Rockingham' and state == 'Virginia']
    harrisonburg_data = [(date, county, state, cases) for (date, county, state, cases, deaths) in data if county == 'Harrisonburg city']

    # creating function
    def worst_seven_day_period(cases_data):

        # dummy variables
        max_sum = 0
        start_date = None
        end_date = None
        sum_new_cases = 0
        old_new_sum = 0
        case_list = []

        # making my case list
        for (date, county,state,cases) in cases_data:
            case_list.append((date, county, state, cases))

        # determining new cases in 7-day period
        for i in range(len(case_list)):
            if i >= 1:
                new_cases = case_list[i][3] - case_list[i - 1][3]
            else:
                new_cases = case_list[i][3]

            sum_new_cases += new_cases

            # defining the 7-day period
            if i >= 7:
                if i - 7 >= 1:
                    old_new_sum = (case_list[i - 7][3] - case_list[i - 8][3])
                else:
                    old_new_sum = case_list[i - 7][3]
                sum_new_cases -= old_new_sum

            # comparing 7-day periods
            if sum_new_cases > max_sum:
                max_sum = sum_new_cases
                end_date = case_list[i][0]
                start_date = case_list[i-6][0]

        # determining the county results
        county = cases_data[0][1]
        print(''
              '') #(aesthetic purposes)
        print('QUESTION 3: The 7-day period in', county, 'with the highest number of new cases began on' ,start_date, 'and ended on' ,end_date, 'with', max_sum, 'cases')

        return max_sum

    R = worst_seven_day_period(rockingham_data)
    H = worst_seven_day_period(harrisonburg_data)

    # comparing both counties
    if R > H:
        print(''
              '')
        print('QUESTION 3: Rockingham County had the worst 7-day period of new positive COVID cases')
    else:
        print(''
              '')
        print('QUESTION 3: Harrisonburg City had the worst 7-day period of new positive COVID cases')

    return

if __name__ == "__main__":
    data = parse_nyt_data('us-counties.csv')

    # write code to address the following question: Use print() to display your responses.
    # When was the first positive COVID case in Rockingham County?
    # When was the first positive COVID case in Harrisonburg?
    result = first_question(data)


    # write code to address the following question: Use print() to display your responses.
    # What day was the greatest number of new daily cases recorded in Harrisonburg?
    # What day was the greatest number of new daily cases recorded in Rockingham County?
    result_2 = second_question(data)

    # write code to address the following question:Use print() to display your responses.
    # What was the worst seven-day period in either the city or county for new COVID cases?
    # This is the 7-day period where the number of new cases was maximal.
    result_3 = third_question(data)

#SUBMITTED

