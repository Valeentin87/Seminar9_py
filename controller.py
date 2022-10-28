import modul
import view

def klick_menu(number):
    if number == 1:
        return modul.lenght()
    elif number == 2:
        return modul.ellips()
    else:
        return view.data_print('Спасибо за работу с редактором!!!')