import re

TOKEN_SPEC = [
    ('NUMBER', r'\d+'),
    ('PRINT', r'print'),
    ('IDENT', r'[a-zA-Z_][a-zA-Z0-9_]*'),
    ('EQUAL', r'='),
    ('AT', r'@'),
    ('LPAREN', r'\('),
    ('RPAREN', r'\)'),
    ('NEWLINE', r'\n'),
    ('SKIP', r'[ \t]+')
]

token_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in TOKEN_SPEC)

def tokenize(code):
    tokens = []
    for match in re.finditer(token_regex, code):
        kind = match.lastgroup
        value = match.group()
        if kind == 'NUMBER':
            value = int(value)
        if kind != 'SKIP':
            tokens.append((kind, value))
    return tokens


