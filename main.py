# Round a float to the nearest 10th (0.1) in Python

# ✅ round a float to the nearest 10th (0.1)

result_1 = round(4.5678, 1)
print(result_1)  # 👉️ 4.6

result_2 = round(4.1234, 1)
print(result_2)  # 👉️ 4.1

# -------------------------------

# ✅ print a float rounded to the nearest 10th (0.1)

my_float = 4.5678

my_str_1 = f'{my_float:.1f}'
print(my_str_1)  # 👉️ '4.6'

my_str_2 = f'{my_float:.2f}'
print(my_str_2)  # 👉️ '4.57'