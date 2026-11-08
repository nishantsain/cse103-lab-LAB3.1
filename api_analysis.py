import json
import urllib.request

# Public API URL
url = "https://jsonplaceholder.typicode.com/users"

# Fetch data from API
with urllib.request.urlopen(url) as response:
    data = json.loads(response.read().decode("utf-8"))

# Display total number of users
print("Total Users:", len(data))

# Display user details
print("\nUser Details:")

for user in data:
    print("ID:", user["id"])
    print("Name:", user["name"])
    print("Email:", user["email"])
    print("City:", user["address"]["city"])
    print("-" * 30)

# Analyze user data
cities = set(user["address"]["city"] for user in data)

print("\nUnique Cities:", len(cities))
print("Cities:", cities)

# Save JSON data into a file
with open("users.json", "w") as file:
    json.dump(data, file, indent=4)

print("\nJSON data saved successfully!")
