def is_palindromo(palavra):
    return palavra == palavra[::-1]


print(is_palindromo("ama"))
print(is_palindromo("teste"))
print(is_palindromo("bob"))
