is_logged_in=True
is_subscribed=False
user_credit=100
max_credit=200
min_credit=50
credits_valid=(user_credit >= min_credit and user_credit <= max_credit) and user_credit != min_credit
bonus_eligible= is_subscribed or not (user_credit <= min_credit)
user_credit += 50
user_credit -= 20
user_credit *= 2
user_credit %= 150

