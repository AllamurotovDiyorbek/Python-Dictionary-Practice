from data import randomuser_data
from randomusers import (
    get_full_names,
    get_users_by_country,
    count_users_by_gender,
    get_emails_of_older_than,
    get_all_coordinates,
    get_average_age,
    get_oldest_user,
    get_registered_before_year,
    get_usernames_starting_with,
    group_users_by_nationality,
    find_users_in_timezone
    )
def run_functions() -> None:
    """
    Runs and prints results of all data processing functions for demonstration purposes.
    """
    # return "Full Names:", get_full_names(randomuser_data)
    # return f"Get users by country: {get_users_by_country(randomuser_data,country='India')}"
    # return count_users_by_gender(randomuser_data)
    # return get_emails_of_older_than(randomuser_data,int(input("")))
    # return get_usernames_starting_with(randomuser_data,input(""))
    # return get_average_age(randomuser_data)
    # return group_users_by_nationality(randomuser_data)
    # return get_all_coordinates(randomuser_data)
    # return get_oldest_user(randomuser_data)
    # return find_users_in_timezone(randomuser_data,offset='+5:30')
    return get_registered_before_year(randomuser_data,2010)
print(run_functions())