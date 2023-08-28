import random

from rich.console import Console
from rich.table import Table

def result_table(title: str, columns: list[str], rows: list[list[str]]) -> None:
    """ Creates a table to display the results of each scan """
    table = Table(title=title)
    console = Console()

    for column in columns:
        table.add_column(
            column,
            style=random.choice(
                [
                    "blue",
                    "yellow",
                    "green",
                    "red",
                    "cyan",
                    "magenta",
                    "violet"
                ]
            ),
            justify="center"
        )

    # Convert all the data into string because it's possible to encounter a BOOL wich `rich` will raise an error at.
    rows = [[str(i) for i in row] for row in rows]

    for row in rows:
        table.add_row(
            *row
        )

    console.print(table)
