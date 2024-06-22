import random
import time as t

def generate_lottery_numbers(number_count, number_range):
    return random.sample(range(1, number_range + 1), number_count)

def main():
    try:
        number_count = int(input("Enter the number of winner you want: "))
        number_range = int(input("Enter the range of numbers (e.g., 49 for 1 to 49): "))
        
        if number_count > number_range:
            print("Number of lottery numbers cannot be greater than the range.")
            return
        
        lottery_numbers = generate_lottery_numbers(number_count, number_range)
        
        print("Winners Lotery Number are:", lottery_numbers)
        t.sleep(1)
    except ValueError:
        print("Please enter valid integers for both inputs.")
    
if __name__ == "__main__":
    main()
