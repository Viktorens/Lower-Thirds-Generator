def speakerName(name):
    # x = Special Characters
    special = '!' or '#' or '$' or '%' or '&' or "'" or '(' or ')' or '*' or '+' or ',' or '-' or '.' or '/' or ':' or ';' or '<' or '=' or '>' or '?' or '@' or '[' or '\\' or ']' or '^' or '_' or '`' or '{' or '|' or '}' or '~' or ' '
    # Test
    if name.isalpha() and name[0].isupper() and name[1:].islower() and special not in name:
        return True
    else:
        return False
    