import quandl
import yfinance as yf
from MenuClass import menu


#Creación del dataframe con quandl
try:
    data_q = quandl.get("WIKI/GOOGL", start_date="2015-01-01", end_date="2018-12-31")
except:
    input("No hay datos quandl")


#Creación del dataframe con yfinance
try:
    data_y = yf.download("GOOGL", "2015-1-1", "2018-12-31")
except:
    input("No hay datos yfinance")



def show_quandl():
    print(data_q)

def show_yfinance():
    print(data_y)




def main():
    funciones =[
        show_quandl,show_yfinance
    ]

    opciones = [
        "Mostrar datos de quandl","Mostrar datos de YFinance"
    ]

    my_menu = menu(funciones,opciones)

    while True:
        function = my_menu.select_menu()
        if function == -1: break
        else: function()
        input("Continue...")
    input("Thanks for using this menu")

if __name__ == "__main__":
    main()