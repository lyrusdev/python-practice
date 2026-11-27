# 01 - Cash Machine

A console ATM written in Python. The user logs in with a PIN and then uses a menu to check the balance, deposit and withdraw money.

> The program interface (menus and messages) is in Spanish.

## Features

- PIN login with a maximum of 3 attempts. After the third failed attempt the program closes without showing the menu.
- Menu with four options: check balance, deposit, withdraw and exit.
- Amount validation: accepts whole numbers and decimals such as `12.5`, and rejects letters, empty input, negative numbers, zero and values like `1.2.3`.
- Withdrawals cannot exceed the available balance.
- Invalid menu options are rejected and the menu is shown again.
- Operation counter shown when the user exits. It counts balance checks and completed deposits and withdrawals. Rejected operations are not counted.

## How to run

```
python cash_machine.py
```

Demo PIN: `1234`. Starting balance: `100.0`.

## Example

```
Ingrese el pin: 1234
Bienvenido/a

Elija una opción: 2
Ingrese el monto a depositar: 50
Su nuevo saldo es 150.0

Elija una opción: 4
¡Gracias por usar Next Level!
Su número total de operaciones es: 1
```

## How it works

The program runs in two steps, one after the other:

1. A `while` loop asks for the PIN until the user logs in or runs out of attempts.
2. A second `while` loop shows the menu, but only if the login succeeded.

## Concepts practiced

- `while` loops with compound conditions (`and`, `not`)
- `if / elif / else`
- `input()` and converting text to `float`
- Validating input with `isdigit()` and `replace()`
- Constants (`PIN`) and boolean flags (`is_logged`)
- Counters and f-strings

## Possible improvements

- Format amounts with two decimals (`:.2f`).
- Add a withdrawal limit per operation.
- Move the amount validation into a function once I learn functions, since it is repeated for deposits and withdrawals.
- Handle invalid input with `try/except` once I learn error handling.

## Notes

The PIN is hardcoded for learning purposes only. Real programs should never store credentials in the source code.