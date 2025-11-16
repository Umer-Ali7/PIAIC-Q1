# Python ATM (CLI) using OOP

A simple, local CLI ATM application implemented with Python and OOP. Data is persisted to a JSON file in `data/bank.json`.

## Features

- Create account with PIN and optional initial deposit
- Login and view balance
- Deposit, withdraw, and transfer funds
- Mini statement (last 10 transactions)
- JSON storage with simple structure

## Project Structure

- `main.py` — entry point that runs the CLI
- `atm/models.py` — `Account` and `Transaction` data models
- `atm/storage.py` — `JSONStorage` for reading/writing data
- `atm/bank.py` — `Bank` domain logic and validations
- `atm/atm_cli.py` — Command-line interface flows
- `data/bank.json` — Data file created on first save

## Run

```bash
python main.py
```

On Windows PowerShell:

```powershell
python .\main.py
```

## Notes

- This is single-user, local storage; no concurrency handling.
- PINs are stored as plain text in JSON for simplicity (do not use in production).
- All amounts are treated as floats; minor rounding differences may occur.

