from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional


@dataclass
class Transaction:
    timestamp: str
    type: str  # deposit, withdrawal, transfer
    amount: float
    note: str = ""


@dataclass
class Account:
    number: str
    owner: str
    pin: str
    balance: float = 0.0
    transactions: List[Transaction] = field(default_factory=list)

    def deposit(self, amount: float, note: str = "") -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        self.transactions.append(
            Transaction(timestamp=datetime.utcnow().isoformat(), type="deposit", amount=amount, note=note)
        )

    def withdraw(self, amount: float, note: str = "") -> None:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        self.transactions.append(
            Transaction(timestamp=datetime.utcnow().isoformat(), type="withdrawal", amount=amount, note=note)
        )

    def transfer_to(self, other: "Account", amount: float, note: str = "") -> None:
        if other.number == self.number:
            raise ValueError("Cannot transfer to the same account")
        if amount <= 0:
            raise ValueError("Transfer amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        other.balance += amount
        now = datetime.utcnow().isoformat()
        self.transactions.append(Transaction(timestamp=now, type="transfer_out", amount=amount, note=note))
        other.transactions.append(Transaction(timestamp=now, type="transfer_in", amount=amount, note=note))

