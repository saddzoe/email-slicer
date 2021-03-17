# email-slicer
# This is a code for an email slicer where it slice it into two parts

email = input("Enter Your Email Address Here: ").strip()
username = email[:email.index("@")]
domain_name = email[email.index("@") + 1 :]
outcome_ = (f"Your username is '{username}' and your domain is '{domain_name}'")

print(outcome_)
