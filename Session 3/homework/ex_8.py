def get_even_list(li):
    new_list = []
    for numb in li:
        if numb % 2 == 0:
            new_list.append(numb)
    return new_list

even_list = get_even_list([1, 2, 5, -10, 9, 6])

if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")
