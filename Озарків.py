import random
user = input("Ваш вибір: (к) Камінь, (п) Папір, (н) Ножиці: ")
comp = random.choice(['к', 'п', 'н'])
print("Комп'ютер обрав:", comp)



if user == comp:
    print("нічия")
elif (user == 'к' and comp == 'н') or \
     (user == 'н' and comp == 'п') or \
     (user == 'п' and comp == 'к'):
    print("ви виграли!")
else:
    print("комп'ютер виграв")