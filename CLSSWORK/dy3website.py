has_account=True
email_verified=False
can_login=has_account and email_verified
email="haleemakuttu@gmail.com"
is_email_valid="@" in email
user_age=17
is_age_valid=user_age >= 18
can_login_final=has_account and email_verified and is_email_valid and is_age_valid
print("can login:",can_login)
print("is the user email valid :",is_email_valid)
print("Is the user age valid:",is_age_valid )
print("at last user can log in or not:",can_login_final)
print("has account is:",has_account is True)