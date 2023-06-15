to_check = [2.0, 2.1, 34.34, 34.00]

for item in to_check:

    if item % 1 == 0:
        is_whole = "yes"
    else:
        is_whole = "no"

    print(f"{item} is an integer? {is_whole}")
