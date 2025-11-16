from __future__ import annotations
import json
from pathlib import Path
from typing import Dict

from .models import Account, Transaction


class JSONStorage:
    def __init__(self, path: str | Path = "data/bank.json") -> None:
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def load(self) -> Dict[str, Account]:
        if not self.path.exists():
            return {}
        data = json.loads(self.path.read_text(encoding="utf-8"))
        accounts: Dict[str, Account] = {}
        for acc_no, acc_data in data.get("accounts", {}).items():
            account = Account(
                number=acc_data["number"],
                owner=acc_data["owner"],
                pin=acc_data["pin"],
                balance=float(acc_data.get("balance", 0.0)),
                transactions=[
                    Transaction(
                        timestamp=t["timestamp"], type=t["type"], amount=float(t["amount"]), note=t.get("note", "")
                    )
                    for t in acc_data.get("transactions", [])
                ],
            )
            accounts[acc_no] = account
        return accounts

    def save(self, accounts: Dict[str, Account]) -> None:
        payload = {
            "accounts": {
                acc_no: {
                    "number": acc.number,
                    "owner": acc.owner,
                    "pin": acc.pin,
                    "balance": acc.balance,
                    "transactions": [
                        {"timestamp": t.timestamp, "type": t.type, "amount": t.amount, "note": t.note}
                        for t in acc.transactions
                    ],
                }
                for acc_no, acc in accounts.items()
            }
        }
        self.path.write_text(json.dumps(payload, indent=2), encoding="utf-8")

