class Email():
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_send = False

    def send(self):
        self.is_send = True

    def get_info(self):
        return f'{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_send}'


emails = []
line = input()
while line != "Stop":
    email = line.split(" ")
    from_person = email[0]
    to_person = email[1]
    message = email[2]
    current_email = Email(from_person, to_person, message)
    emails.append(current_email)

    line = input()

send_emails = list(map(int, input().split(", ")))

for index in send_emails:
    emails[index].send()

for email in emails:
    print(email.get_info())
