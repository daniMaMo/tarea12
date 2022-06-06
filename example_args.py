import datetime

def adder(*lists):
    for l in lists:
        print("entrada_inicial:", l[0])

adder([1,2],[2,2,5],[5,8,9])

DATA = [[datetime.datetime(2022, 1, 1, 0, 0), 153357743.0, 6.15], [datetime.datetime(2022, 1, 2, 0, 0), 161880469.0, 6.053], [datetime.datetime(2022, 1, 3, 0, 0), 169773375.0, 6.034], [datetime.datetime(2022, 1, 4, 0, 0), 172208177.0, 6.014], [datetime.datetime(2022, 1, 5, 0, 0), 181196294.0, 5.987]]
DATA_dates = [dates[0] for dates in DATA]
print(DATA_dates)

def retrieve_happiness(*lists):
    for l in lists:
        dates = [date for date in DATA_dates if l[0] < date < l[1]]
        print(dates)

retrieve_happiness([datetime.datetime(2022,1,1), datetime.datetime(2022,1,4)])
print(datetime.datetime(2022,1,1))
print(datetime.datetime(2022,1,4))
print(datetime.datetime(2022,1,1) < datetime.datetime(2022,1,4))
print(DATA[0])

date_object = datetime.datetime.strptime('2021-02-03', "%Y-%m-%d")
print(date_object)
