class Assign:
    def __init__(self, name, value):
        self.name = name
        self.value = value


class Print:
    def __init__(self, expr):
        self.expr = expr


class HistoryAccess:
    def __init__(self, name, index):
        self.name = name
        self.index = index



def parse(tokens):
    statements = []
    i = 0

    while i < len(tokens):

        token = tokens[i]

        # Assignment: x = 5
        if token[0] == "IDENT" and tokens[i+1][0] == "EQUAL":

            name = token[1]
            value = tokens[i+2][1]

            statements.append(Assign(name, value))

            i += 3


        # Print statement
        elif token[0] == "PRINT":

            name = tokens[i+2][1]

            # check history access
            if tokens[i+3][0] == "AT":

                index = tokens[i+4][1]
                expr = HistoryAccess(name, index)

                i += 6

            else:

                expr = name
                i += 4

            statements.append(Print(expr))

        else:
            i += 1

    return statements