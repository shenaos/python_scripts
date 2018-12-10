



def purify(x):
    even_numbers = []
    for i in x:
        if i % 2 == 0:
            even_numbers.append(i)
    
    print(even_numbers)
    return even_numbers


purify([1,2,3])                