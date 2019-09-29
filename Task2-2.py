n = int(input('Введите значение n: '))
distance_from_home = 0
all_distance = 0
for i in range(1,n+1):
    all_distance += 1/i
    distance_from_home += (-1)**(i+1)/i
print('Общее растояние, которое прошел мужчина составляет:', round(all_distance,2),'км')
print('Расстояние между мужчиной и домом, где его жена, составляет:', round(distance_from_home,2),'км')