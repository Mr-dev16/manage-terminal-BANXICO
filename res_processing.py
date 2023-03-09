from statistics import mode


def mode_data(data):
    data_dict = data
    idSeries = data_dict['bmx']['series']
    dates = idSeries[0]
    numbers = dates.get('datos')
    numbers_percent = []
    for date in range(0, len(numbers)):
        dict_data = numbers[date]
        numbers_percent.append(dict_data['dato'])
        return mode(numbers_percent)


def writer_data(dato):
    data_dict = dato
    idSeries = data_dict['bmx']['series']
    dates = idSeries[0]
    numbers = dates.get('datos')
    numbers_list = []
    for date in range(0, len(numbers)):
        numbers_list.append(numbers[date])
        if len(numbers_list) == len(numbers):
            txt = open("data.txt", 'a')
            txt.write(f"{numbers_list}")
            txt.close()
            return "view data in document"
