import random

def generating_random_numbers(count, start, end):
    """Generate a list of unique random numbers within a given range."""
    return random.sample(range(start, end + 1), count)

# To Generate 10 unique random numbers between 1 and 100
random_numbers = generating_random_numbers(10, 1, 100)

print("Random Numbers:", " ".join(map(str, random_numbers)))
