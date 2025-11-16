from __future__ import annotations
from typing import Dict, Optional

from .models import Account
from .storage import JSONStorage


class Bank:
    def __init__(self, storage: Optional[JSONStorage] = None) -> None:
        self.storage = storage or JSONStorage()
        self.accounts: Dict[str, Account] = self.storage.load()

    def create_account(self, number: str, owner: str, pin: str, initial_deposit: float = 0.0) -> Account:
        if number in self.accounts:
            raise ValueError("Account number already exists")
        if initial_deposit < 0:
            raise ValueError("Initial deposit cannot be negative")
        acc = Account(number=number, owner=owner, pin=pin, balance=0.0)
        if initial_deposit:
            acc.deposit(initial_deposit, note="Initial deposit")
        self.accounts[number] = acc
        self.storage.save(self.accounts)
        return acc

    def authenticate(self, number: str, pin: str) -> Account:
        acc = self.accounts.get(number)
        if not acc or acc.pin != pin:
            raise ValueError("Invalid account number or PIN")
        return acc

    def get_account(self, number: str) -> Optional[Account]:
        return self.accounts.get(number)

    def deposit(self, number: str, amount: float) -> float:
        acc = self._require(number)
        acc.deposit(amount)
        self.storage.save(self.accounts)
        return acc.balance

    def withdraw(self, number: str, amount: float) -> float:
        acc = self._require(number)
        acc.withdraw(amount)
        self.storage.save(self.accounts)
        return acc.balance

    def transfer(self, src_number: str, dst_number: str, amount: float) -> None:
        src = self._require(src_number)
        dst = self._require(dst_number)
        src.transfer_to(dst, amount)
        self.storage.save(self.accounts)

    def _require(self, number: str) -> Account:
        acc = self.accounts.get(number)
        if not acc:
            raise ValueError("Account not found")
        return acc

