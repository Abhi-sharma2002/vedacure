def get_odd_numbers(max_num):
    odd_numbers = []
    for num in range(1,max_num + 1):
        if num % 2 != 0:
            odd_numbers.append(num)
            return odd_numbers
            max_num = int(input("enter the maximum number: "))
            odd_numbers = get_odd_numbers(max_num)
            print("odd numbers between 1 and",max_num, ":" ,odd_numbers)