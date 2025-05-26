def print_table(headers, rows):
    """
    Print a formatted table using headers and rows.

    Args:
        headers (List[str]): Column headers
        rows (List[List[str]]): List of row entries (each row is a list)
    """
    if not rows:
        print("[INFO] No data to display.")
        return

    columns = list(zip(*([headers] + rows)))
    col_widths = [max(len(str(cell)) for cell in col) for col in columns]

    def format_row(row):
        return "| " + " | ".join(f"{str(cell):<{w}}" for cell, w in zip(row, col_widths)) + " |"

    def build_line():
        return "+-" + "-+-".join("-" * w for w in col_widths) + "-+"

    border = build_line()
    print(border)
    print(format_row(headers))
    print(border)
    for row in rows:
        print(format_row(row))
    print(border)
