#!/usr/bin/env python3
"""More simple dictionary operations"""

TRAVEL_LOG = [
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

def add_new_country(country, visit_count, cities_visited):
    country_dict = {"country": country, "visits": visit_count, "cities": cities_visited}
    TRAVEL_LOG.append(country_dict)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(TRAVEL_LOG)
