def gen (DOB):
    message = ""
    if DOB < 1945:
        message = "You are part of the silent generation"
    if DOB > 1977 and DOB < 1995:
        message = "You are a millenial"
    if DOB <=1976 and DOB>1965:
        message = "You are part of gen X"
    if DOB <=1964 and DOB>1946:
        message = "You are a baby boomer"
    return message

# print (gen(1983))
