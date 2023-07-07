    


travel_log = [
    {
        "Country":"Afghanistan",
        "Visits":12,
        "Cities":["Logar","Wardak","Kabul","Parwan"]
    },
    {
        "Country":"UK",
        "Visits":3,
        "Cities":["London","Bermingham"]
    }
]

def add_new_country(travel_log_name,name,visits,cities):
    new_country_info = {}
    
    new_country_info["Country"] = name
    new_country_info["Visits"] = visits
    new_country_info["Cities"] = cities
    
    travel_log_name.append(new_country_info)

    return travel_log_name

new_country = add_new_country(travel_log,"USA",4,["New York","LA","Las Vegas","Cleveland"])

print(new_country)
# print(travel_log[0]["Country"])