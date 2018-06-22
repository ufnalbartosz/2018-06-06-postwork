'''
Poniżej znajduje się implementacja CLI (command line interface) do modułu
turtle, czyli Pythonowego odpowiednika LOGO. Wykorzystano tutaj wzorzec Template
Method (metoda szablonowa).

W pierwszym, obowiązkowym zadaniu, należy dodać wsparcie dla makr, tak aby można
było nagrać ciąg komend, a następnie odtworzyć ten sam ciąg przy pomocy
komendy "playback". W tym celu, należy dodać następujące komendy:

- record -- rozpoczyna nagrywanie makra
- stop -- kończy nagrywanie makra
- playback -- wykonuje makro, tzn. wszystkie komendy po komendzie "record", aż
  do komendy "stop".

Podpowiedź: Użyj wzorca Command (polecenie).

W drugim, nieobowiązkowym zadaniu, zastanów się, jak można zastosować wzorzec
Composite (kompozyt) do tych makr i spróbuj zastosować go.

Rozwiązania wysyłamy tak samo, jak prework, tylko że w jednym Pull Requeście.
'''

import cmd, sys
import turtle
from functools import wraps

class TurtleShell(cmd.Cmd):
    intro = 'Welcome to the turtle shell.   Type help or ? to list commands.\n'
    prompt = '(turtle) '

    def recordable(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            self = args[0]
            if self.recording_on:
                self.recorded_commands.append([f, args, kwargs])

            f(*args, **kwargs)
        return wrapper

    def __init__(self):
        super().__init__()
        self.recorded_commands = list()
        self.recording_on = False

    def do_record(self, arg):
        self.recording_on = True

    def do_stop(self, arg):
        self.recording_on = False

    def do_playback(self, arg):
        for method, args, kwargs in self.recorded_commands:
            method(*args, **kwargs)

    # ----- basic turtle commands -----
    @recordable
    def do_forward(self, arg):
        'Move the turtle forward by the specified distance:  FORWARD 10'
        turtle.forward(int(arg))

    @recordable
    def do_right(self, arg):
        'Turn turtle right by given number of degrees:  RIGHT 20'
        turtle.right(int(arg))

    @recordable
    def do_left(self, arg):
        'Turn turtle left by given number of degrees:  LEFT 90'
        turtle.left(int(arg))

    @recordable
    def do_home(self, arg):
        'Return turtle to the home position:  HOME'
        turtle.home()

    @recordable
    def do_circle(self, arg):
        'Draw circle with given radius an options extent and steps:  CIRCLE 50'
        turtle.circle(int(arg))

    @recordable
    def do_position(self, arg):
        'Print the current turtle position:  POSITION'
        print('Current position is %d %d\n' % turtle.position())

    @recordable
    def do_heading(self, arg):
        'Print the current turtle heading in degrees:  HEADING'
        print('Current heading is %d\n' % (turtle.heading(),))

    @recordable
    def do_reset(self, arg):
        'Clear the screen and return turtle to center:  RESET'
        turtle.reset()

    def do_bye(self, arg):
        'Close the turtle window, and exit:  BYE'
        print('Thank you for using Turtle')
        turtle.bye()
        return True

if __name__ == '__main__':
     TurtleShell().cmdloop()
