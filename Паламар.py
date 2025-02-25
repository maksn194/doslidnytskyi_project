import random

user = input("Виберіть (к) Камінь, (п) Папір, (н) Ножиці: ")
comp = random.choice(['к', 'п', 'н'])
print("Вибір комп'ютера:", comp)


if user == comp:

    print("Нічия!")

elif (user == 'к' and comp == 'н') or \
     (user == 'н' and comp == 'п') or \
     (user == 'п' and comp == 'к'):

    print("Ви виграли!")
else:

    print("Виграв комп'ютер")