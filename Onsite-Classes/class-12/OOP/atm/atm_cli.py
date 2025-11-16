from __future__ import annotations
from getpass import getpass, GetPassWarning
import warnings
from typing import Optional

from .bank import Bank


def prompt_amount(prompt: str) -> float:
    while True:
        raw = input(prompt).strip()
        try:
            value = float(raw)
            if value <= 0:
                print("Amount must be positive.")
                continue
            return value
        except ValueError:
            print("Enter a valid number.")


def run_cli() -> None:
    bank = Bank()
    print("Welcome to the Python ATM")
    while True:
        print("\nMain Menu:")
        print("1) Login")
        print("2) Create Account")
        print("3) Exit")
        choice = input("> ").strip()
        if choice == "1":
            _login_flow(bank)
        elif choice == "2":
            _create_account_flow(bank)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


def _create_account_flow(bank: Bank) -> None:
    print("\n-- Create Account --")
    number = input("Choose account number: ").strip()
    owner = input("Your name: ").strip()
    pin = prompt_pin("Choose 4-digit PIN: ", confirm=True)
    if not number or not owner or not pin:
        print("All fields are required.")
        return
    try:
        initial = 0.0
        raw = input("Initial deposit (optional, default 0): ").strip()
        if raw:
            initial = float(raw)
        bank.create_account(number, owner, pin, initial)
        print("Account created successfully!")
    except ValueError as e:
        print(f"Error: {e}")


def _login_flow(bank: Bank) -> None:
    print("\n-- Login --")
    number = input("Account number: ").strip()
    pin = prompt_pin("PIN: ")
    try:
        account = bank.authenticate(number, pin)
    except ValueError as e:
        print(f"Error: {e}")
        return
    print(f"\nWelcome, {account.owner}!")
    while True:
        print("\nAccount Menu:")
        print("1) Balance")
        print("2) Deposit")
        print("3) Withdraw")
        print("4) Transfer")
        print("5) Mini Statement")
        print("6) Logout")
        choice = input("> ").strip()
        if choice == "1":
            print(f"Balance: {account.balance:.2f}")
        elif choice == "2":
            amount = prompt_amount("Amount to deposit: ")
            try:
                bank.deposit(account.number, amount)
                print("Deposit successful.")
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == "3":
            amount = prompt_amount("Amount to withdraw: ")
            try:
                bank.withdraw(account.number, amount)
                print("Withdrawal successful.")
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == "4":
            target = input("Transfer to account number: ").strip()
            amount = prompt_amount("Amount to transfer: ")
            try:
                bank.transfer(account.number, target, amount)
                print("Transfer successful.")
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == "5":
            print("\n-- Mini Statement (last 10) --")
            for t in account.transactions[-10:]:
                print(f"{t.timestamp} | {t.type:<13} | {t.amount:>10.2f} | {t.note}")
        elif choice == "6":
            print("Logged out.")
            break
        else:
            print("Invalid choice.")


def prompt_pin(prompt: str, confirm: bool = False) -> str:
    while True:
        pin = _safe_getpass(prompt)
        if not pin:
            print("PIN is required.")
            continue
        if not (pin.isdigit() and len(pin) == 4):
            print("PIN must be exactly 4 digits.")
            continue
        if confirm:
            pin2 = _safe_getpass("Confirm PIN: ")
            if pin != pin2:
                print("PINs do not match. Try again.")
                continue
        return pin


def _safe_getpass(prompt: str) -> str:
    try:
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            value = getpass(prompt)
            for warn in w:
                if issubclass(warn.category, GetPassWarning):
                    print("(Note: PIN input may be visible on this terminal.)")
                    break
            return (value or "").strip()
    except Exception:
        # Fallback to visible input if getpass fails in this environment
        return input(prompt).strip()
