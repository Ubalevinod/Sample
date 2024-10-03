def sum_of_ten_numbers():
    total = 0
    for i in range(10):
        while True:
            try:
                num = float(input(f"Enter number {i + 1}: "))
                total += num
                break
            except ValueError:
                print("Please enter a valid number.")
    
    print(f"The sum of the 10 numbers is: {total}")

if __name__ == "__main__":
    sum_of_ten_numbers()
