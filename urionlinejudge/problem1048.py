Salary = float(input())

if Salary <= 400.00:
    increement = (Salary * 15)/100
    NewSalary = Salary + increement
    print(f'Novo salario: {NewSalary:.2f}')
    print(f'Reajuste ganho: {increement:.2f}')
    print(f'Em percentual: 15 %')
elif Salary >= 400.01 and Salary <= 800.00:
    increement = (Salary * 12)/100
    NewSalary = Salary + increement
    print(f'Novo salario: {NewSalary:.2f}')
    print(f'Reajuste ganho: {increement:.2f}')
    print(f'Em percentual: 12 %')
elif Salary >= 800.01 and Salary <= 1200.00:
    increement = (Salary * 10)/100
    NewSalary = Salary + increement
    print(f'Novo salario: {NewSalary:.2f}')
    print(f'Reajuste ganho: {increement:.2f}')
    print(f'Em percentual: 10 %')
elif Salary >= 1200.01 and Salary <= 2000.00:
    increement = (Salary * 7)/100
    NewSalary = Salary + increement
    print(f'Novo salario: {NewSalary:.2f}')
    print(f'Reajuste ganho: {increement:.2f}')
    print(f'Em percentual: 7 %')
elif Salary >= 2000.01:
    increement = (Salary * 4)/100
    NewSalary = Salary + increement
    print(f'Novo salario: {NewSalary:.2f}')
    print(f'Reajuste ganho: {increement:.2f}')
    print(f'Em percentual: 4 %')