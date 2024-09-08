# ends with = boolean value

str = "I like coding"

# will print true if this matches or it will print false
print(str.endswith("ing"))
# True

# -------------------

# Capitalize - like starting of the senctance and it will make a new str and wont effect it 
print(str.capitalize())
# I like coding

# -------------------
# replace 
example = "I am studying python"

print(example.replace("am", "like"))
# I like studying python


# -------------------
# find -  will return index of char or a word
print(example.find("a"))
# 2