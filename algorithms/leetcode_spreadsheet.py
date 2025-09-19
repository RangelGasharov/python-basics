class Spreadsheet:

    def __init__(self, rows: int):
        self.cells_map = {}

    def set_cell(self, cell: str, value: int) -> None:
        self.cells_map[cell] = value

    def reset_cell(self, cell: str) -> None:
        self.cells_map.pop(cell, None)

    def get_value(self, formula: str) -> int:
        expr = formula.lstrip("=")
        left, _, right = expr.partition("+")

        def resolve(token: str) -> int:
            if token.isdigit():
                return int(token)
            return self.cells_map.get(token, 0)

        return resolve(left) + resolve(right)


spreadsheet = Spreadsheet(3)
spreadsheet.set_cell("A2", 10)
print(spreadsheet.get_value("=142222222+729"))
print(spreadsheet.get_value("=A2+7"))
print(spreadsheet.get_value("=A1+A2"))
