# WAF to print the elements of a list in a single line.


car_list = ["TATA", "BMW", "Mercedes", "Audi", "Suzuki"] 


def listing(list):
    for item in list:
        print(item, end=", ")



listing(car_list)