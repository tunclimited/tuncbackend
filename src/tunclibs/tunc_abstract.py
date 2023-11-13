def tunc(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as ex:
            # write into message table here
            print(ex)

    return wrapper
