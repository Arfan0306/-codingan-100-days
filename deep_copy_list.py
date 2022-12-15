data_0 =[1,2]
data_1 =[3,4]

data_2D = [data_0,data_1]
data_2D_copy = data_2D.copy()

print(f"data = {data_2D}")
print(f"data copy = {data_2D_copy}")

# mengambil data dari data nested list
data = data_2D[1][0]
print(f"data = {data}")

data_2D[1][0] = 5
print(f"data = {data_2D}")

# deepcopy

from copy import deepcopy

data_2D = [data_0,data_1,10]
data_2D_deepcopy = deepcopy(data_2D)

data_2D[1][0] = 30
print(f"data = {data_2D}")
print(f"data copy = {data_2D_copy}")
print(f"data deep = {data_2D_deepcopy}")
