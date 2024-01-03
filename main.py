aux = number = int(input('Entre com um número inteiro: '))
rev = 0

while number != 0:
    last_digit = number % 10
    number //= 10
    rev = rev * 10 + last_digit

if rev == aux:
    print(f'{aux} é um palíndromo.')
else:
    print(f'{aux} não é um palíndromo.')
