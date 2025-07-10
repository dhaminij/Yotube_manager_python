def candy_gaurd(func):
    def wrapper(age):
        if age>=5:
            print("yes")
            func(age)
        else:
            print("no")
    return wrapper