


def valid_pnr(pnumber):
    """
    Validates a person number, takes 'pnumber' as a string and returns True or False as boolean
    :param pnumber:
    :return:
    """
    pnumber = pnumber.replace("-", "")
    pnumber = pnumber.replace("+", "")
    if(len(pnumber) != 10 or pnumber.isdigit() != True):
        return False

    ctrl_num = pnumber[-1:]
    nine_first = pnumber[:-1]
    numbers_product = ""
    nine_first_sum = 0

    for i in range(len(nine_first)):
        if i % 2 == 0:
            numbers_product += str(int(nine_first[i]) * 2)
        else:
            numbers_product += nine_first[i]
    for i in range(len(numbers_product)):
        nine_first_sum  += int(numbers_product[i])

    #if control number is valid
    if (nine_first_sum  + int(ctrl_num)) % 10 == 0:
        return True
    else:
        return False


print valid_pnr("970603-2050")