class TestName:
    def speakerName(self, name):
        special = '!' or '#' or '$' or '%' or '&' or "'" or '(' or ')' or '*' or '+' or ',' or '-' or '.' or '/' or ':' or ';' or '<' or '=' or '>' or '?' or '@' or '[' or '\\' or ']' or '^' or '_' or '`' or '{' or '|' or '}' or '~' or ' '
        if name.isalpha() and name[0].isupper() and name[1:].islower() and special not in name:
            return True
        else:
            return False
    
    def inputNotEmpty(self, name):
        if len(name) != 0:
            return True
        else:
            return False