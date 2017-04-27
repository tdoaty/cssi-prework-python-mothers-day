sender = input("Who is this card for?")
receiver = input("Who is this card from?")
holiday = input("What is the holiday?")
def holiday_greeting(sender, receiver, holiday):
    return "Happy " + holiday ", " + receiver + "!  - Sincerely " + sender
