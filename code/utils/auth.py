def authenticate(login, password, all_users):
    user = None

    # Find the user based on login (email or telephone)
    for u in all_users:
        if u.email == login or u.telephone_number == login:
            user = u
            break

    if user and user.password == password:
        # Authentication successful, return the role
        return user

    # Authentication failed, return None
    return None