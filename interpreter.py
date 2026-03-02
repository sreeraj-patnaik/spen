from parser import Assign, Print, HistoryAccess


class Interpreter:

    def __init__(self):
        self.variables = {}

    def run(self, statements):

        for stmt in statements:

            if isinstance(stmt, Assign):

                if stmt.name not in self.variables:
                    self.variables[stmt.name] = []

                self.variables[stmt.name].append(stmt.value)

            elif isinstance(stmt, Print):

                if isinstance(stmt.expr, HistoryAccess):

                    values = self.variables.get(stmt.expr.name, [])

                    print(values[stmt.expr.index])

                else:

                    values = self.variables.get(stmt.expr, [])

                    print(values[-1])