x = int(input("Digite um número: "))
print(f"A tabuada de {x} é")
print(F"{x} x 1 = {x*1}")
print(F"{x} x 2 = {x*2}")
print(F"{x} x 3 = {x*3}")
print(F"{x} x 4 = {x*4}")
print(F"{x} x 5 = {x*5}")
print(F"{x} x 6 = {x*6}")
print(F"{x} x 7 = {x*7}")
print(F"{x} x 8 = {x*8}")
print(F"{x} x 9 = {x*9}")
print(F"{x} x 10 = {x*10}")
print("="*10)
n=1
while n <= 10:
    print(f"{x}x{n} =",x*n)
    n = n+1
