import pyautogui as py


heights = py.prompt("Enter the heights of the students: " ,title="Students Heights").split(" ")

totalHeight = 0
totalstudents = 0
for i in heights:
    totalHeight+=int(i)
    totalstudents+=1

average = round((totalHeight / totalstudents))
x = py.confirm(f"The average height of the class is {average}." , title="Thanks for using RTechs.")


