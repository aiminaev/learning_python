stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}

stats_values = list(stats.values())
stats_keys = list(stats.keys())
max_value = max(stats_values)
max_value_index = stats_values.index(max_value)
print(stats_keys[max_value_index])