import sys

# po wywolaniu sys.exit() nie sa wolane nastepne instrukcje
# tutaj zwracam 1 mimo tego, ze wykonuje sie poprawnie i daloby 0
# wiec echo $? zwroci 1
# w ten sposob mozna przerywac wykonanie z kodem ktory sobie zazyczymy
# moze byc przydatne w automatyzaji ktora decyzje podejmnie w oparciu o 
# zwrocony kod 
print('Start')
sys.exit(1)

print('Tego nie bedzie')