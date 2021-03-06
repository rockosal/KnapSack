def read_problem(file_name):
    lines = open(file_name).readlines()

    # get the number of items and total capacity
    tokens = lines[0].split()
    n_items = int(tokens[0])
    capacity = int(tokens[1])
    # file = open("reportfile",'w')
    # file.write(""+n_items.__str__()+" "+capacity.__str__())

    # collect the values and weights of each item
    items = []
    for line in lines[1 : n_items+1]:
        tokens = line.split()
        value = int(tokens[0])
        weight = int(tokens[1])
        item = (value, weight)
        items.append(item)

    # or:
    # n_items, capacity = map(int, lines[0].split())
    # print(items)
    # print capacity and n to file


    return (capacity, items)
