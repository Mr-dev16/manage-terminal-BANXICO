from res_processing import *
import requests


print("#"*201)
print("#"*90, 'BANCO OF THE MEXICO', "#"*90)
print("#"*201)
print("\n")


# first input, date initial and date end
print("config date of data, example: yyyy-mm-dd\n")
initial_date = input("initial date: ")
end_date = input("end date: ")
print('\n')

# second input, set token of the user
print("set token of the user\n")
token = input("token: ")
print('\n')


def res_data():
    req_percent = requests.get(
        f"https://www.banxico.org.mx/SieAPIRest/service/v1/series/SF43718,SF606553/datos/{initial_date}/{end_date}?token={token}&incremento=PorcAnual")
    req_money = requests.get(
        f"https://www.banxico.org.mx/SieAPIRest/service/v1/series/SF43718,SF606553/datos/{initial_date}/{end_date}?token={token}")
    req_percentJSON = req_percent.json()
    req_moneyJSON = req_money.json()
    print('                percent  money\n')
    print(
        f'mode data:     {mode_data(req_percentJSON)}   {mode_data(req_moneyJSON)}\n')
    print(writer_data(req_moneyJSON))


res_data()
