import os

class menu:
    
    def createMenu():

        choice = int(input('''
[1] - Add a match
[2] - Season review
[3] - Data export
[4] - About
[5] - Exit
>'''))
        return choice
    

    def showInfo(version, full):
        if full == False:
            print(f'''
 oooooooo8 oooo                                            o888o  o888o
888         888ooooo    ooooooo  oooo  o  oooo  ooooooo  o888oo o888oo 
 888oooooo  888   888 888     888 888 888 888 888     888 888    888   
        888 888   888 888     888  888888888  888     888 888    888   
o88oooo888 o888o o888o  88ooo88     88   88     88ooo88  o888o  o888o  

v{version} - meeko 2026
              ''')
        else:
            print(f'''
 oooooooo8 oooo                                            o888o  o888o
888         888ooooo    ooooooo  oooo  o  oooo  ooooooo  o888oo o888oo 
 888oooooo  888   888 888     888 888 888 888 888     888 888    888   
        888 888   888 888     888  888888888  888     888 888    888   
o88oooo888 o888o o888o  88ooo88     88   88     88ooo88  o888o  o888o  

v{version} - meeko 2026
A simple basketball statistics tracker, written to be easy to use and to be informational.
https://github.com/worthyworm/showoff
              ''')
        
    def clearScreen():
        os.system('cls' if os.name == 'nt' else 'clear')