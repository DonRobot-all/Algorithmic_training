combination = '1020'
'1000 9000 0100 0900 0010 0090 0001 0009'

for i in range(4):
    for new_number in [-1, 1]:
        new_num = (int(combination[i]) + new_number) % 10
        new_combination = (combination[:i] + str(new_num) + combination[i+1:])
        print(new_combination)

        # () + new_num + (***)
        # (*) + new_num + (**)
        # (**) + new_num + (*)
        # (***) + new_num + ()


word = 'hit'
'git jit yit tit'
for i in range(len(word)):
    for char in range(26):
        new_combination = word[:i] + chr(97 + char) + word[i+1:]
        print(new_combination)


# print(chr(ord('a') + 2))