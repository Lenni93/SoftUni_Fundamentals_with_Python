country_name = input().split(", ")
capital_name = input().split(", ")

county_information = {country_name[i]: capital_name[i] for i in range(len(country_name))}

for country_name, capital_name in county_information.items():
    print(f'{country_name} -> {capital_name}')