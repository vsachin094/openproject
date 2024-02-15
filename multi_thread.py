# Your multiplication function
def multiply(number):
    return number * 2  # or any other operation you want

def main():
    numbers = [1, 2, 3, 4, 5]  # Your list of numbers
    num_threads = 2  # Set the number of threads

    # Create a ThreadPoolExecutor with the desired number of threads
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        # Map the multiplication function to the list of numbers
        results = list(executor.map(multiply, numbers))

    # Results will contain the multiplied values
    print("Results:", results)

if __name__ == "__main__":
    main()
