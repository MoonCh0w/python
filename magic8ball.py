import random

answers_array = ["No.", "Go fuck yourself.", "Yes.", "Maybe.", "Not sure.", "Fuck off.", "Try again later.", "I don't know.", "What do you think?", "You're retarded."]
questions_array = ["What is it?", "What do you want?", "Go ahead, ask your question.", "Yes daddy?"]

que = random.choice(questions_array)
ans = random.choice(answers_array)
inp = input(("%s: ") % (que))

if len(inp) >= 1:
    print(ans)
else:
    print("Type something you fucking retard. (Try again)")
