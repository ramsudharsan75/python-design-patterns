import time


def time_it(func):
    def wrapper():
        start = time.time()
        result = func()
        end = time.time()
        print(f"{func.__name__} took {end - start} seconds")
        return result

    return wrapper


@time_it
def some_op():
    print("Starting op")
    time.sleep(1)
    print("Done")
    return 123


if __name__ == "__main__":
    some_op()
