import time
valid = False
while not valid:
    all_active_contacts = ['A', 'B', 'C', 'D']
    num_len = len(all_active_contacts)
    input_str = f"{num_len}_{time.time()}"
    hash_pos_val = str(abs(hash(input_str)))
    input_str_2 = f"{time.time()}_{num_len}"
    hash_pos_val += str(abs(hash(input_str_2)))

    fix = ""
    i = 1
    unique = ['0']
    print(hash_pos_val)
    for char in hash_pos_val:
        print(char, ",", unique, ",", fix)
        c = int(char)
        if c > num_len or c == i or str(c) in unique:
            continue
        else:
            i += 1
            fix += char
            unique.append(char)

    print(fix)
    valid = True if len(fix) == num_len else False