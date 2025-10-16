def fizzbuzz(rules):
    for i in range(1, 101):
        output = ""
        for key, word in rules.items():
            if i % int(key) == 0:
                output += word
        print(output or i)


fizzbuzz({"3": "Fizz", "5": "Buzz"})

fizzbuzz({"4": "Fizz", "9": "Buzz", "12": "Lazz"})
