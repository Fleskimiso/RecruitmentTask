class User:
    def __init__(self, firstname, telephone_number, email, password, role, created_at, children):
        self.firstname = firstname
        self.telephone_number = telephone_number
        self.email = email
        self.password = password
        self.role = role
        self.created_at = created_at
        self.children = children

    def __repr__(self):
        return f"User({self.firstname}, {self.email}, {self.role})"