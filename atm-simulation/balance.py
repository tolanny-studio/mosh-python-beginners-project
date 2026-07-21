from pathlib import Path
import logging

"""
Read and write the ATM account balance from persistent storage.
"""

BALANCE_FILE = Path(__file__).parent / "balance.txt"
logger = logging.getLogger(__name__)


def read_balance() -> int:
    try:
        return int(BALANCE_FILE.read_text())
    except FileNotFoundError:
        logger.warning("Balance file not found ⛔ Initializing balance to zero")
        BALANCE_FILE.write_text("0")
        return 0
    except ValueError as e:
        logger.error("Invalid balance value: %s", e)
        return 0


def write_balance(current_balance) -> None:
    try:
        BALANCE_FILE.write_text(str(current_balance))
    except FileNotFoundError:
        logger.error("Cannot write balance: file not found")
