import sys
import time
import random


class MagicBall():


    answers = [
               'It is certain' ,'It is decidedly so'  'Without a doubt' 
                'Yes definitely', 'You may rely on it', 
                'As I see it, yes' ,'Most likely', 'Outlook good' , 
                'Yes', 'Signs point to yes','Don\'t count on it',
                'My reply is no','My sources say no',
                'Outlook not so good','Very doubtful'
              ]

    def __init__(self): 
        pass

    def ask_question(self):
        print('Ask me a question.')
        input('>')
        print("Thinking...")
        #Delaying
        time.sleep(2)
        print(random.choice(self.answers))
        self.replay()


    def replay(self):
        reply = 'yes' 
        play_attempts =  0
        while reply != "no":
            print("Would you like to ask another question? [yes or no]")
            reply = str(input(">")).lower()
            if reply == "yes":
                self.ask_question()
            elif reply == "no":
                print("It was nice playing!!GOODBYE")
                sys.exit(0)
            else:
                print("I apologies, I did not catch that. Please repeat. \n")
                play_attempts += 1

    def replay_inputs(self):
        reply = str(input(">")).lower()
        print("input text '{}' has been detected.".format(reply))
        return reply



if __name__ == '__main__':
    mgb = MagicBall()
    mgb.ask_question()