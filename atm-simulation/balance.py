from pathlib import Path
import logging

BALANCE_FILE = Path(__file__).parent / "balance.txt"
logger = logging.getLogger(__name__)


def read_balance():
    try:
        with open(BALANCE_FILE, "r") as file:
            return int(file.read())
    except FileNotFoundError:
        logger.warning("Balance file not found ⛔ Initializing balance to zero")
        return 0
    except ValueError as e:
        logger.error(f"Invalid balance value ,{e}")
        return 0


def write_balance(current_balance):
    try:
        with open(BALANCE_FILE, "w") as file:
            file.write(str(current_balance))
    except FileNotFoundError:
        logger.error("Cannot write balance: file not found")
