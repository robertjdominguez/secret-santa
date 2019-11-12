import random
from config import *
from twilio.rest import Client


# Twilio congif
accountSID = 'your_acc_id'
authToken = 'your_auth_token'
twilio_cli = Client(accountSID, authToken)
twilio_number = 'your_twilio_number'


def send_msg(cell_number, msg):
    twilio_cli.api.account.messages.create(
        to=cell_number,
        from_=twilio_number,
        body=msg)


def secret_santa(the_list):
    # Shuffle the list
    random.shuffle(the_list)
    # Assign the gift to the person one index higher with counter starting at beginning of list
    i = 0
    for x in the_list:
        santa = x[0]
        i += 1
        if i < len(the_list):
            elf = the_list[i][0]
            message = f"Hi, {santa}!\n\nFor secret santa this year, you are giving a gift to {elf}.\n\nThis message was generated automatically and can't be replied to.\n\nMerry Christmas! \U0001F384"
            santas_workshop = x[1]
            send_msg(santas_workshop, message)
        else:
            santa = the_list[-1][0]
            elf = the_list[0][0]
            message = f"Hi, {santa}!\n\nFor secret santa this year, you are giving a gift to {elf}.\n\nThis message was generated automatically and can't be replied to.\n\nMerry Christmas! \U0001F384"
            santas_workshop = the_list[-1][1]
            send_msg(santas_workshop, message)


def main():
    secret_santa(the_elves)


main()
