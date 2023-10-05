applications = ('Spotify','WhatsApp','Telegram','Xbox','VK Messenger','Mail','Facebook')#Кортеж applications, который содрежит 7 названий виндовс
new_tu = applications[0:3]#Создаем новый кортеж new_tu, состоящий из элементов с индексами от 0 до 2 включительно из исходного кортежа applications
print(new_tu)#Выводим кортеж new_tu
new_tu2 = applications[3:7]#Создаем новый кортеж new_tu2, состоящий из элемента с индексами от 3 до 7 включительно из исходного кортежа applications
print(new_tu2)#Выводим кортеж new_tu2
all_tu = (applications,) + (new_tu,) + (new_tu2,)#Создаем кортеж, который должен содержать все три кортежа включая исходный.
print(all_tu)#Выводим
#1 задание