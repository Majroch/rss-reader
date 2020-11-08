### MENU CLASS ###
import getch, os

class MenuRenderer:
    KEY_UP = 'A'
    KEY_DOWN = 'B'
    KEY_RIGHT = 'C'
    KEY_LEFT = 'D'

    KEY_ESCAPE = 'escape'
    KEY_Q = "q"
    KEY_ENTER = '\n'

    def __init__(self, title, menuEntries:list=[]):
        if len(menuEntries) <= 0:
            raise(Exception("You need to provide some menu entries!"))

        self.menuEntries = menuEntries
        self.title = title
        self.selected = 0

    def render(self):
        os.system("clear")
        print("#" * 10, end=" ")
        print(self.title, end=" ")
        print("#" * 10)

        for index in range(0, len(self.menuEntries)):
            if self.selected == index:
                print(self.menuEntries[index], "<<<")
            else:
                print(self.menuEntries[index])

    def getInput(self):
        movement = getch.getch()
        if movement == '\x1b':
            movement = getch.getch()
            if movement == '[':
                return getch.getch()
            else:
                return self.KEY_ESCAPE
        else:
            return movement

    def logic(self):
        if self.selected < 0:
            self.selected = len(self.menuEntries)-1
        elif self.selected > len(self.menuEntries)-1:
            self.selected = 0
            
    def run(self):
        while True:
            self.render()
            movement = self.getInput()
            if movement == self.KEY_UP:
                self.selected -= 1
            elif movement == self.KEY_DOWN:
                self.selected += 1
            elif movement == self.KEY_ESCAPE or movement == self.KEY_Q:
                exit()
            elif movement == self.KEY_ENTER:
                return self.selected
            
            self.logic()
