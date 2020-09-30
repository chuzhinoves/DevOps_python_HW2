#list realise
seasons = ["winter"]*2 + ["spring"]*3 + ["summer"] * 3 + ["authm"] * 3 + ["winter"]
input_month = int(input("Enter month: "))
if  input_month < 1:
    raise ValueError("месяц должен начинаться с 1")
elif input_month > 12:
    raise ValueError("месяц должен быть не больше 12")
else:
    print(seasons[input_month - 1])

#dict realise
seasons = ["winter"]*2 + ["spring"]*3 + ["summer"] * 3 + ["authm"] * 3 + ["winter"]
dict_season = {
    i:season
    for i, season in enumerate(seasons)
}
input_month = int(input("Enter month: "))
if  input_month < 1:
    raise ValueError("месяц должен начинаться с 1")
elif input_month > 12:
    raise ValueError("месяц должен быть не больше 12")
else:
    print(dict_season[input_month - 1])
