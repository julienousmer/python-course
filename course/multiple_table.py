number = int(input(f"Quelle table souhaitez vous afficher ?\n"))

datas = []
for i in range(1, 11):
    data = i * number
    if (data % 3) == 0:
        data = f"{data}*"
    datas.append(data)

print(datas)
