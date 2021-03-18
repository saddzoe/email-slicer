# email-slicer
# This is a code for an email slicer where it slices the email into two parts; it separates the username from the domain name of an username

email = input("Enter Your Email Address Here: ").strip()
username = email[:email.index("@")]
domain_name = email[email.index("@") + 1:]
outcome_ = (f"Your username is '{username}' and your domain is '{domain_name}'")

print(outcome_)
