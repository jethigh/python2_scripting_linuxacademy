FIRST_NAME = 'John'
LAST_NAME = 'Dawn'
BIRTH_DATE = '01.01.1980'
AGE = '40'

print("My name is " + FIRST_NAME + " " + LAST_NAME + ".")
print("I was born on " + BIRTH_DATE + " and I'm " + AGE + " years old.")

# albo
print("My name is %s %s.\nI was born on %s and I'm %s years old.") % (FIRST_NAME, LAST_NAME, BIRTH_DATE, AGE)

# albo
print("My name is {} {}.\nI was born on {} and I'm {} years old.").format(FIRST_NAME, LAST_NAME, BIRTH_DATE, AGE)