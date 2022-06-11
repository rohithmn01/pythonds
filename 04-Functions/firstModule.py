def findIndex(to_search, target):
    for index, value in enumerate(to_search):
        if value == target:
            return True
    else:
        return False