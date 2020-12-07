# secret-santa

## :christmas_tree: :christmas_tree: :christmas_tree: Ho-Ho-Ho! :christmas_tree: :christmas_tree: :christmas_tree:
My wife and I needed to facilitate a "Secret Santa" group. So, of course I wrote something to automate matching the pairs and notifying each person. Python script using [Twilio](https://www.twilio.com/) to automate the message component. Fun and easy.

### How's it work?
Everyone in the secret santa group is assigned an index in a series. When the program runs, the order is shuffled and everyone is assigned their own position - _n_ - and an elf (the person they're giving a gift to) at the position of _n+1_. Finally, when the end of the list is reached, the person at this position is assigned an elf of the person in the first position. It makes more sense to think of it as a circle instead of a linear series.

### Requirements
* Friends (okay...just people?)
* A Twilio account
* Holiday Spirit :gift:

### Running
You'll need the Python Twilio library installed. Run
```bash
pip install twilio
```
Then, in `config.py`, update your list of secret santas and their phone numbers. Finally, modify the config variables for the Twilio account in `main.py` -- all this information can be found on your Twilio dashboard.
```python
accountSID = 'your_acc_id'
authToken = 'your_auth_token'
twilio_cli = Client(accountSID, authToken)
twilio_number = 'your_twilio_number'
```
Run ```python main.py``` and pretend you're a hard-working, objective, caring person.
