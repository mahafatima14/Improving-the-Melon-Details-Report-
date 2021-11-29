"""Print out all the melons in our inventory."""



from melons import melon_data


def print_melon(melons_data):
    """Print each melon with corresponding attribute information."""


    for melon, attributes in sorted(melon_data.items()):  # .items() combines the values and keys together so we can print both out
        print(f'{melon}: {attributes}')
        print('===================================')
    return 

result = print(print_melon(melon_data))

