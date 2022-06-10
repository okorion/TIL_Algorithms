def drome(list_numbers):
    reverse_lst_num = list_numbers[::-1]

    if list_numbers == reverse_lst_num:
        return 'yes'
    else:
        return 'no'


while True:
    a = input()

    if a == '0':
        break
    else:
        print(drome(a))
