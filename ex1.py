import pandas as pd
df = pd.read_csv('/content/sample_data/california_housing_train.csv')
mean_house_value = df.loc[(df['population'] >= 0) & (df['population'] <= 500), 'median_house_value'].mean()
print('Средняя стоимость дома, где кол-во людей от 0 до 500: $', round(mean_house_value, 2))
min_population = df['population'].min()
max_households = df.loc[df['population'] == min_population, 'households'].max()
print(f'Максимальное количество households в зоне минимального значения population ({min_population}): {max_households}')