from data import randomuser_data
def get_full_names(data: dict) -> list[str]:
    """
    Returns a list of users' full names in 'First Last' format.

    Args:
        data (dict): JSON data containing user records.

    Returns:
        list[str]: List of full names.
    """
    results=data["results"]
    names=[]
    for user in results:
        name=user['name']
        full_name=name['first'] +" "+name['last']
        names.append(full_name)
    return names
def get_users_by_country(data: dict, country: str) -> list[dict]:
    """
    Filters and returns users who live in a specific country.

    Args:
        data (dict): JSON data containing user records.
        country (str): Country name to filter by.

    Returns:
        list[dict]: List of dictionaries containing full name and email of matching users.
    """

    users=[]
    for user in data['results']:
        if user['location']['country'] == country:
            users.append({
                'fullname':user['name']['first']+""+user['name']['last'],
                'email':user
            })
    return users


def count_users_by_gender(data: dict) -> dict:
    """
    Counts the number of users by gender.

    Args:
        data (dict): JSON data containing user records.

    Returns:
        dict: Dictionary with gender as keys and count as values.
    """
    users={}
    erkak=0
    ayol=0
    for i in  data["results"]:
        if i["gender"]=="male":
            erkak+=1
            users["male"]=erkak
        else:
            ayol+=1
            users["female"]=ayol
    return users


def get_emails_of_older_than(data: dict, age: int) -> list[str]:
    """
    Returns a list of emails of users older than the given age.

    Args:
        data (dict): JSON data containing user records.
        age (int): Age threshold.

    Returns:
        list[str]: List of email addresses.
    """
    users=[]
    for i in data["results"]:
        if i['dob']['age']<=age:
            users.append(
                i["email"]
            )
    return users
def sort_users_by_age(data: dict, descending: bool = False) -> list[dict]:
    """
    Sorts users by age in ascending or descending order.

    Args:
        data (dict): JSON data containing user records.
        descending (bool, optional): Whether to sort in descending order. Defaults to False.

    Returns:
        list[dict]: List of users with name and age sorted accordingly.
    """
    pass


def get_usernames_starting_with(data: dict, letter: str) -> list[str]:
    """
    Returns a list of usernames starting with a given letter.

    Args:
        data (dict): JSON data containing user records.
        letter (str): The starting letter to filter usernames.

    Returns:
        list[str]: List of matching usernames.
    """
    uas=[]
    for i in data["results"]:
        cll=i['login']['username']
        if letter == cll[:1]:
           uas.append(cll)
    return uas
def get_average_age(data: dict) -> float:
    """
    Calculates and returns the average age of users.

    Args:
        data (dict): JSON data containing user records.

    Returns:
        float: Average age.
    """
    c=0
    count=0
    for i in data['results']:
        c+=i['dob']['age']
        count+=1
        
    return round(c/count,1)


def group_users_by_nationality(data: dict) -> dict:
    """
    Groups and counts users by their nationality.

    Args:
        data (dict): JSON data containing user records.

    Returns:
        dict: Dictionary with nationality as keys and count as values.
    """
    dct={}
    lst=[]
    for i in data["results"]:
        lst.append(i['nat'])
    for s in lst:
        dct[s]=lst.count(s)
    return dct,lst
def get_all_coordinates(data: dict) -> list[tuple[str, str]]:
    """
    Extracts all users' coordinates as tuples of (latitude, longitude).

    Args:
        data (dict): JSON data containing user records.

    Returns:
        list[tuple[str, str]]: List of coordinate tuples.
    """
    lst=[]
    for i in data['results']:
        lst.append(i['location']['coordinates']['latitude'])
        lst.append(i['location']['coordinates']['longitude'])
    tp=tuple(lst)
    return tp
    pass


def get_oldest_user(data: dict) -> dict:
    """
    Finds and returns the oldest user's name, age, and email.

    Args:
        data (dict): JSON data containing user records.

    Returns:
        dict: Dictionary containing 'name', 'age', and 'email' of the oldest user.
    """
    count=[]
    dct={}
    for i in data['results']:
        dct[i['dob']['age']]=[
            i['name']['first']+i['name']['last'],
            i['dob']['age'],
            i['email']
        ]
        # count.append(i['dob']['age'])
    count=max(dct)
    return dct[count]
        
def find_users_in_timezone(data: dict, offset: str) -> list[dict]:
    """
    Returns users whose timezone offset matches the given value.

    Args:
        data (dict): JSON data containing user records.
        offset (str): Timezone offset (e.g. '+5:30').

    Returns:
        list[dict]: List of users with full name and city.
    """
    for i in data['results']:
        c=i['location']
        if c['timezone']['offset']==offset:
            return i['name']['first']+i['name']['last'],i['email']
def get_registered_before_year(data: dict, year: int) -> list[dict]:
    """
    Returns users who registered before a given year.

    Args:
        data (dict): JSON data containing user records.
        year (int): Year threshold.

    Returns:
        list[dict]: List of users with full name and registration date.
    """
    for i in data['results']:
        c=i['registered']['date']
        if int(c[:4])<year:
            print(f'{"name"} " : "{i["name"]["first"]+i["name"]["last"]},{"registred : "+c}')