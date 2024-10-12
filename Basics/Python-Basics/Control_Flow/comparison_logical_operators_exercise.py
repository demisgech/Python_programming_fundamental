is_Ethiopian_citizen = False
work_experience = 3
has_bachelor_degree = False

is_eligible_to_hire = (is_Ethiopian_citizen and
                       (work_experience >= 2 or has_bachelor_degree))
print("Is eligible to hire = ", is_eligible_to_hire)

application_refused = not is_eligible_to_hire
print("Application refused = ", application_refused)

has_facebook_account = True
username_matched = False
password_matched = True
authenticate_failed = False
login_successful = ((has_facebook_account
                    and username_matched
                    and password_matched)
                    and (not authenticate_failed))
print("Login successful = ", login_successful)


high_income = 100_000
has_good_credit_score = False
eligible_for_loan = (high_income >= 10_000 and has_good_credit_score)
print("Eligible for loan = ", eligible_for_loan)

refused_for_loan = not eligible_for_loan
print("Refused for loan = ", refused_for_loan)
