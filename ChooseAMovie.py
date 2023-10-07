from random import choice

films_number =int(input('Из скольки фильмов будем выбирать?   '))

half_list = films_number//2

owl_movies_list = [input(f'Введите {half_list} фильм ').capitalize() for half_list in range(1,half_list+1)]

cat_movies_list = [input(f'Введите {  half_list} фильм ').capitalize() for half_list in range(1, half_list+1)]

owl_movies_list.extend(cat_movies_list)

print(choice(owl_movies_list))
