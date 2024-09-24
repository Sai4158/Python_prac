student = {
    "name" : "rahul kumar",
    # This is nested dic
    "subject" : {
        "py" : 74,
        "ewf" : 45,
        "ewf" : 34,
    }
}

print(student)

# {'name': 'rahul kumar', 'subject': {'py': 74, 'ewf': 34}}


# This will print all the key or the heading the dictionary 
print(student.keys())
# dict_keys(['name', 'subject'])



# This will print all the values 
print(student.values())
# dict_values(['rahul kumar', {'py': 74, 'ewf': 34}])


# This is how we can update 
student.update({"City" : "delhi"})
print(student)
