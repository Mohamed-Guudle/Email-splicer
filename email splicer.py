email = input("please enter your email: ").strip()
username = email[:email.index('@')]
domain_name = email[email.index('@')+1:]
format_ = (f"your username is '{username}' and your domain is '{domain_name}'")
print(format_)