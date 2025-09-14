dict_of_choice = {'Life' : 2, 'is' : 2, 'the': 2, 'greatest': 1, 'thing' : 1}
freq = 2
ser = 0
for key in dict_of_choice:
    if dict_of_choice[key] == freq:
        ser = ser + 1

print("Frequency of Freq is : " + str(ser))