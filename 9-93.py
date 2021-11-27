# Dictionary in List

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(country, visited_times, city_list):
    newdict = {"country": country, "visits": visited_times, "cities": city_list}
    travel_log.append(newdict)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)