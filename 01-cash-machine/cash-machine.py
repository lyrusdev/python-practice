
# Console ATM: asks for a PIN (3 attempts), then shows a menu
# to check balance, deposit and withdraw money.
balance = 1000.0
WITHDRAWAL_LIMIT = 200.0
operations_count = 0
option = "0"

PIN = "1234"
attempts_left = 3
is_logged = False

# Step 1: ask for the PIN (maximum 3 attempts)
while not is_logged and attempts_left > 0: 
    user_input = input("Ingrese el pin: ")

    if user_input == PIN:
        print("Bienvenido/a")
        is_logged = True
    else:
        attempts_left -= 1

        if attempts_left == 0:
            print("No tiene más intentos, cerrando el sistema...")
        else:
            print(f"Pin incorrecto, le quedan {attempts_left} intentos")

# Step 2: show the menu only if the login succeeded
while is_logged and option != "4":
    print('''
          ¡Bienvenido/a al cajero Next Level!
          Las opciones son:
          1. Consultar saldo
          2. Depositar
          3. Retirar
          4. Salir
          ''')
    option = input("Elija una opción: ")
    
    if option == "1":
        print(f"Su saldo actual es {balance:.2f}")
        operations_count += 1
    elif option == "2":
        deposit = input("Ingrese el monto a depositar: ")
        
        # Remove one dot so decimals like "12.5" pass isdigit(),
        # while letters, negatives and "1.2.3" still fail
        if deposit.replace(".", "", 1).isdigit():
            deposit = float(deposit)
            
            if deposit <= 0:
                print("Monto inválido")
            else:    
                balance += deposit
                print(f"Su nuevo saldo es {balance:.2f}")
                operations_count += 1
        else:
            print("Ingreso no válido")
    elif option == "3":
        withdraw = input("Ingrese el monto a retirar: ")
        
        # Same validation as the deposit above
        if withdraw.replace(".", "", 1).isdigit():
            withdraw = float(withdraw)

            if withdraw <= 0:
                print("Monto inválido")
            elif withdraw > balance:
                print("Saldo insuficiente, revise su saldo")
            elif withdraw > WITHDRAWAL_LIMIT:
                print(f"Monto superior al límite de ${WITHDRAWAL_LIMIT}")
            else:
                balance -= withdraw
                print(f"Su saldo restante es {balance:.2f}")
                operations_count += 1    
        else:
            print("Ingreso no válido")
    elif option == "4":
        print("¡Gracias por usar Next Level!")
        print(f"Su número total de operaciones es: {operations_count}")
    else:
        print("Opción inválida, intente de nuevo")
