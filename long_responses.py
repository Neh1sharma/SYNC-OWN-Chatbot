import random

R_EATING = "I don't like eating anything because I'm a bot obviously!" 


def unknown():
       response = ['could you please re-phrase that?',
                   "...",
                   "sounds about right",
                   "what does that mean?"][random.randrange(4)]
       return response