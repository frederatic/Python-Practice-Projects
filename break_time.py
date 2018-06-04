
# Everyone needs a break once in a while

import time
import webbrowser

breaks = 5  # how many breaks you want
break_count = 0
print("Break at"+time.ctime()) # keeps track of breaks
while break_count < breaks:
    time.sleep(3600)  # time in seconds between breaks
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")   # links that gets opened to remind you of break
    break_count += 1