class EmailNotice:
    def render(self):
        return "Email notice"

class ScreenNotice:
    def render(self):
        return "Screen notice"

def display(notice):
    print(notice.render())

for notice in [EmailNotice(), ScreenNotice()]:
    display(notice)
# No messages are sent; render() only returns a string.
