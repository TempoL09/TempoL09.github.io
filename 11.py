motorcycles = ['honda','yamaha','suzuki','ducati']

too_expensive = motorcycles.pop(3)

print(motorcycles)
print(f"A {too_expensive.title()}is too expensive for me.")


aaa = 2019
bbb = 'audi'
f = f'{aaa} {bbb}'
print(f.upper())


from random import choice
ccc = ['acd','fss','eeee','taaa']
CCC = choice(ccc)
print(CCC)


filename = 'pi_digits.txt'
with open(filename) as f:
    contents = f.read()
print(contents.rstrip())
