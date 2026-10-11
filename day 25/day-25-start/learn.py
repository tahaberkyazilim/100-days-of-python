import pandas

mini = pandas.DataFrame({"name": ["Aang", "Zuko", "Toph"], "color": ["Gray", None, "Gray"]})
print(mini["color"] == "Gray")
print(mini["color"].isna())