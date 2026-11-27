# python-practice

My personal Python practice repository. Each folder is one exercise or small project I build while learning, so you can follow my progress from the first scripts onward.

I'm learning Python through online courses and with the help of AI tools, which I use as a mentor to get feedback and guidance. I write and test the code myself. The goal is to build a steady habit of writing code, not to publish perfect code, so early exercises are simple on purpose and I improve them as I learn.

**Status:** work in progress, updated as I learn.

## Projects

| # | Project | What it does | Concepts practiced |
|---|---------|--------------|--------------------|
| 01 | [cash-machine](./01-cash-machine) | Console ATM with a PIN, a menu, balance, deposits and withdrawals | `while` loops, `if/elif/else`, `input()`, input validation, constants, boolean flags, counters, f-strings |

More exercises will be added as I learn new topics.

## Repository structure

```
python-practice/
├── README.md
└── 01-cash-machine/
    ├── README.md
    └── cash_machine.py
```

## How to run an exercise

1. Install [Python 3](https://www.python.org/downloads/).
2. Clone the repository:
   ```
   git clone https://github.com/lyrusdev/python-practice.git
   ```
3. Go into an exercise folder and run it. For example:
   ```
   cd python-practice/01-cash-machine
   python cash_machine.py
   ```

## Learning path

- [x] Variables, `input()`, `if/else`
- [x] `while` and `for` loops
- [x] Validating user input without crashing the program
- [ ] Functions
- [ ] Lists, tuples and dictionaries
- [ ] Error handling with `try/except`
- [ ] Working with files
- [ ] Modules and libraries

I'm still exploring which area of Python to focus on (backend, data analysis or automation), so this list will change.

## Conventions

- One folder per exercise, numbered in the order I build them.
- File, folder and variable names in English, using `snake_case` for code.
- Small, frequent commits with a message that says what changed.

## Notes

This repository is for practice. Some code, like the demo PIN in the cash machine, is hardcoded for learning purposes only. Real projects should never store credentials in the source code.

The program interface (menus and messages) is in Spanish.
