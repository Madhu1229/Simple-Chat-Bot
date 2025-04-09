import random

R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_DRINKING = "I don't like drinking anything because I'm a bot obviously!"
R_SICK = "I'm sorry to hear that you're not feeling well. It's important to prioritize your health and get the rest you need to recover. Make sure to stay hydrated, get plenty of rest, and consider seeking medical attention if necessary. If there's anything I can do to help or if you need someone to talk to, I'm here for you. Take care, and I hope you feel better soon!"

def unknown():
    response = ['Could you please re-pharse that?',
                "...",
                "Sounds about right",
                "what does that mean?"][random.randrange(4)]
    return response





