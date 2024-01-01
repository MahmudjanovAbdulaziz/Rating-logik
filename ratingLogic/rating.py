rating = [4, 5, 3, 2, 3, 2, 2, 3, 2, 2, 2, 1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]

rating_counts = {}

for rating_value in rating:
    if rating_value in rating_counts:
        rating_counts[rating_value] += 1
    else:
        rating_counts[rating_value] = 1

for key, value in rating_counts.items():
    print(f'Количество {key}-звезд: {value}')

print('Среднее значение рейтинга равняется ', round (sum(rating) / len(rating), 2))