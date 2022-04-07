#Множество абонентов, не имеющих долгов.
abons = {"Иванов", "Петров", "Васильев", "Антонов"}

debtors = {"Петров", "Антонов"}

non_debtors = abons.difference(debtors)

print(non_debtors)
# {'Васильев', 'Иванов'}
# Находим множество символов, которые встречаются в двух строках одновременно.
a = input("Введите первую строку: ")
b = input("Введите вторую строку: ")

a_set, b_set = set(a), set(b) # используем множественное присваивание

a_and_b = a_set.intersection(b_set)

print(a_and_b)