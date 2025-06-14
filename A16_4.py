def get_numbers(n: int = 10):
    numbers = []
    count = 1
    while len(numbers) < n:
            value = float(input(f"Enter number {count}/{n}: "))
            numbers.append(value)
            count += 1
        
    return numbers

def write_numbers_to_file(numbers: list[float], filename: str = "numbers.txt"):

    with open(filename, "w") as f:
        for num in numbers:
            f.write(f"{num}\n")
    print(f"Successfully wrote {len(numbers)} numbers to '{filename}'.")


if __name__ == "__main__":
    nums = get_numbers(10)
    write_numbers_to_file(nums)
