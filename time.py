from time import localtime, strftime, mktime

# czas teraz
start_time = localtime()

# Drukowanie czasu jako stringu
print(strftime("%X",start_time))

# Obliczenie i wydrukowanie delty
raw_input("Press button to stop!")
stop_time = localtime()
delta = mktime(stop_time) - mktime(start_time)
print('Czas od startu do wcisniecia klawisza: {}s').format(delta)
