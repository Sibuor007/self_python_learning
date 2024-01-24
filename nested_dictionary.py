student_data = {
    "Sibuor": {
        "roll_num": 8781,
        "age": 28,
        "Course": "SE"
    },
    "Jemimah": {
        "roll_num": 5278,
        "age": 28,
        "Course": "Accounting"
    }
}

# access using keyname
print(student_data["Sibuor"])
print(student_data["Jemimah"]["roll_num"])

# adding key pair value
student_data["Sibuor"]["phone_no"] = 122333738
print(student_data["Sibuor"])

# deleting value in dict
del student_data["Jemimah"]["Course"]
# use pop function if you want to return the deleted value
print(student_data["Sibuor"].pop("phone_no"))
print(student_data["Jemimah"])
# nesting list within a dictionary
travel_data = {
    "USA": ["New York", "New Jersey", "Oklahoma"],
    "UK": ["Manchester", "London", "Liverpool", "Leicester"]
}
print(travel_data)
print(travel_data["UK"])
