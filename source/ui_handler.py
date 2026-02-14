import os

class menu:
    
    def createMenu():

        choice = int(input('''
[1] - Add a match
[2] - View your matches
[3] - Statistics review
[4] - Data export
[5] - Manage coach mode
[6] - About
[7] - Exit
>'''))
        return choice
    

    def showInfo(version, full):
        if full == False:
            print(f'''
███████╗██╗  ██╗ ██████╗ ██╗    ██╗ ██████╗ ███████╗███████╗
██╔════╝██║  ██║██╔═══██╗██║    ██║██╔═══██╗██╔════╝██╔════╝
███████╗███████║██║   ██║██║ █╗ ██║██║   ██║█████╗  █████╗  
╚════██║██╔══██║██║   ██║██║███╗██║██║   ██║██╔══╝  ██╔══╝  
███████║██║  ██║╚██████╔╝╚███╔███╔╝╚██████╔╝██║     ██║     
╚══════╝╚═╝  ╚═╝ ╚═════╝  ╚══╝╚══╝  ╚═════╝ ╚═╝     ╚═╝     

v{version} - meeko 2026
              ''')
        else:
            print(f'''
███████╗██╗  ██╗ ██████╗ ██╗    ██╗ ██████╗ ███████╗███████╗
██╔════╝██║  ██║██╔═══██╗██║    ██║██╔═══██╗██╔════╝██╔════╝
███████╗███████║██║   ██║██║ █╗ ██║██║   ██║█████╗  █████╗  
╚════██║██╔══██║██║   ██║██║███╗██║██║   ██║██╔══╝  ██╔══╝  
███████║██║  ██║╚██████╔╝╚███╔███╔╝╚██████╔╝██║     ██║     
╚══════╝╚═╝  ╚═╝ ╚═════╝  ╚══╝╚══╝  ╚═════╝ ╚═╝     ╚═╝      

v{version} - meeko 2026
A simple basketball statistics tracker, written to be easy to use and to be informational.
https://github.com/worthyworm/showoff
              ''')
        
    def clearScreen():
        os.system('cls' if os.name == 'nt' else 'clear')