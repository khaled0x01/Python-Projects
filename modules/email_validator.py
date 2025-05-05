def verify_email(email):
    # Prompt the user to enter their email and ensure it's valid
    #  example@domain.com
    if '@' in email and '.' in email:
        username, domain = email.split('@')
        if username and domain:
            if '.' in domain:  # Check if domain has a . before splitting
                x, y = domain.split('.')
                if x and y:
                    return 1
        return 0
    return 0