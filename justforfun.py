# -----------------------------+------------------------------ #
# --- A simple program to store student details using loop --- #
# -----------------------------+------------------------------ #
# -- importing sys.files for decorations --
import os, time

# simple function to clear_screen
def clearScr(): 
    os.system("cls")

# variables
runPgm = True
dataMenu = True
dataShow = True
dataEntry = True
stdData = ["name", "student_ID", "course"]
dataSave = False
dataAppend = False
saveHandle = False

# ascii arts
drakeBYE = [
"             .   __.-/|     ",
"             \`o_O'         ",
"              =( )=  +-----+",
"                U|   | BYE |",
"      /\  /\   / |   +-----+",
"     ) /^\) ^\/ _)\     |   ",
"     )   /^\/   _) \    |   ",
"     )   _ /  / _)  \___|_  ",
" /\  )/\/ ||  | )_)\___,|)) ",
"<  >      |(,,) )__)    |   ",
" ||      /    \)___))       ",
" | \____(      )___) )____  ",
"  \______(_______;;;)__;;;) "
]

fairy =[
"                       ,_  .--.  ",
"             , ,   _)\/    ;--.  ",
"     . ' .    \_\-'   |  .'    \ ",
"    -= * =-   (.-,   /  /       |",
"     ' .\'    ).  ))/ .'   _/\ / ",
"         \_   \_  /( /     \ /(  ",
"         /_\ .--'   `-.    //  \ ",
"         ||\/        , '._//    |",
"         ||/ /`(_ (_,;`-._/     /",
"         \_.'   )   /`\       .' ",
"              .' .  |  ;.   /`   ",
"             /      |\(  `.(     ",
"            |   |/  | `    `     ",
"            |   |  /             ",
"            |   |.'              ",
"         __/'  /                 ",
"     _ .'  _.-`                  ",
"  _.` `.-;`/                     ",
" /_.-'` / /                      ",
"       | /                       ",
"      ( /                        ",
"     /_/                         ",
]

# Decoration::title
def draw():
    print("# -----------------------------+------------------------------ #") 
    print("# --- A simple program to store student details using loop --- #") 
    print("# -----------------------------+------------------------------ #")

# Decoration::line
def xliner():
    print("# ---------------------------- + ----------------------------- #")

# Decoration::menu
def menu():
    print("1: Show  Student Details")
    print("2: Enter Student Details")
    print("3: Exit")

# Decoration::entry_port
def dEntry():
    print("1: New Entry")
    print("2: Return Back")
    if dataSave: print("3: Save Data")
    if saveHandle: print("4: Overwrite Save Data")
    if dataAppend: print("5: Append Save File")
    xliner()
    print("-: [Use other keys to exit the Program] :-".upper())
    
# Decoration::system_exit
def shutDown():
    for i in drakeBYE:
        print(i)
        time.sleep(.1)
    print("! ---- exiting program ---- ! ".capitalize())
    time.sleep(1.2) # timer before program terminates
    quit() # exit the loop and close the program

# Decoration::LiveData viewer
def dataViewer():
    for eData in stdData:
        print(":: " + eData)

# data for student detail:: user-input handling
def studentDetail():
    print("#: Please Enter Student Name")
    stdData[0] = input(">: ")
    print("#: Please Enter Student Number")
    stdData[1] = input(">: ")
    print("#: Please Enter Student Course")
    stdData[2] = input(">: ")

# save data function
def saveData():
    oFile = open("students.txt", "w")
    for item in stdData:
        oFile.write(item + " ")
    oFile.write("\n") # newline creation
    oFile.close()
    for i in fairy:
        print(i)
        time.sleep(.1)

# append data function
def appenData():
    aFile = open("students.txt", "a")
    for item in stdData:
        aFile.write(item + " ")
    aFile.write("\n") # newline creation
    aFile.close()
    for i in fairy:
        print(i)
        time.sleep(.1)

# show data fn
def showStdData():
    clearScr()
    draw()
    print('')
    xliner()
    print("[-- The Student Data From The Records --]")
    xliner()
    try:
        # read the saved file
        rFile = open("students.txt", 'r')

        # decor for display
        print(" + {:10} {:10} {:10} {:10}".format("StdIndex", "Name", "Number", "Course"))
        i = 1
        # using loop to print data
        for item in rFile:
            student = item.split()
            print(" - {:10} {:10} {:10} {:10}".format(str(i), student[0], student[1], student[2]))
            i += 1
        rFile.close()

        xliner()
        input(">: 'enter' to return...")

    except OSError:
        print("#: Error404:: There's no file named 'students'!")
        input(">: 'Enter' to continue")

# main function :: the looper
while runPgm:
    while dataMenu:
        clearScr() # clearScr fn call
            
        # Cl-interface design
        draw() # fn call
        xliner()# fn call
        menu() # ui-menu
        xliner()# fn call

        # receive user data
        choice = input(">: ")

        # conditional operation
        if choice == "1":
            showStdData()
        elif choice == "2":
            dataMenu = False
            dataEntry = True
        elif choice == "3":
            shutDown()
        
    while dataEntry:
        clearScr()

        # Cl-interface design
        draw() # fn call
        xliner()# fn call
        dEntry() # ui-entry form
        xliner()# fn call
        # 
        print(":: -- Current Student Data -- ::")
        dataViewer()# live data viewer
        xliner()# fn call

        # user entry
        choice = input(">: ")

        if choice == "1":
            print("#: Enter New Student data :: Press 'Y' or 'y' to continue")
            enData = input(">: ")
            if enData == "y":
                studentDetail() # fn call for input handling
                #  once user enters all data show save data function
                if saveHandle == False:
                    dataSave = True
                if saveHandle == True and dataSave == False:
                    dataAppend = True

        elif choice == "2":
            dataEntry = False
            dataMenu = True

        elif choice == "3" and dataSave == True:
            clearScr()
            print("+ -- Saving Data Don't Close the program -- +".upper())
            time.sleep(.7)
            saveData()
            input(">: Press 'Enter' to complete!")
            dataSave = False
            saveHandle = True
        
        elif choice == "4" and saveHandle == True:
            clearScr()
            print("+ -- Overwriting save file -- +".upper())
            time.sleep(.7)
            saveData()
            input(">: Press 'Enter' to complete!")
            dataAppend = False
            
        elif choice == "5" and dataAppend == True:
            clearScr()
            print("+ -- Appending save file -- +".upper())
            time.sleep(.7)
            appenData()
            input(">: Press 'Enter' to complete!")
            dataAppend = False

        elif choice == "" or choice == "y":
            input("#> Error.IO - 'Enter' to continue")
        else:
            shutDown()



