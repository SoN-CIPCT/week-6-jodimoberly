web_users = ["Vivian","John","Johneen","Tom","Yolanda"]
print(web_users)
new_users = ["John","Tom","Cole","Keaton","Sophia"]
print(new_users)
for user in new_users:
   if user in web_users:
     print(f"{user}: This user is already in use. Please choose a different user name.")
   else:
     print(f"{user}: This user name is available")

#  web_users = ["Vivian","John", "Johneen","Tom", "Yolanda"]
#  print(web_users)
#  new_users = ["John","Tom", "Cole", "Keaton", "Sophia"]
# print(new_users)

#  for user in new_users:
#     if user in web_users:
#         print(f"{user}: This user is already in use. Please choose a different user name.")
#    else: 
#        print(f"{user}: This user name is available")


#create a dictornary of cities

# #create a dictornary of cities
# cities = {}

# cities["Madrid"] = {"Country": "Spain",
#                     "Population": 3400000,
#                     "Fact": "Has the worlds oldest restaurant"}
# cities["Tokyo"] = {"Country" : "Japan",
#                        "Population" : 37000000,
#                     "Fact": "Most Michelin-starred restaurants"}
# cities["Sydney"] = {"Country": "Australia",
#                        "Population": 5557200,
#                        "Fact" : "First tocelebrate New Year"}

# for city, info in cities.items():
#    print(f"City: {city}")
#    print(f"Country: {info['Country']}")
#    print(f"Population: {info['Population']}")
#    print(f"Fact: {info['Fact']}")
#    print () """