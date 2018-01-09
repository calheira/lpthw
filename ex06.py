# inicializa variavel com valor numerico
types_of_people = 10
# inicializa variavel com string formatada
x = f"There are {types_of_people} types of people."
# inicializa variavel com string
binary = "binary"
do_not = "don't"
# inicializa variavel com string formatada 
y = f"Those who know {binary} and those who {do_not}."
# imprime variaveis
print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")
# inicializa variavel com valor booleano
hilarious = False
# inicializa variavel com string e espaco para formatacao
joke_evaluation = "Isn't that joke so funny?!{}"
# imprime variavel usando propriedade format
print(joke_evaluation.format(hilarious))
# inicializa variaveis com strings
w = "This is the left side of..."
e = "a string with a right side."
# concatena strings e imprime o resultado
print(w + e)