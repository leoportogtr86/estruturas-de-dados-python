def soma_elementos(arr):
    soma = 0
    for i in arr:
        soma += i

    return soma


def soma_array(arr):
    return sum(arr)


print(soma_elementos([10, 20, 30]))
print(soma_array([10, 20, 30]))
