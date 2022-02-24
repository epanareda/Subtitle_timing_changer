# Define the function to operate between times with the subtitle format.
def time_operation(time1, time2, add_or_sub):
    '''This function allows to add or substract between 2 set times. The time1 is the inital time of the subtitle file,
    and the time2 is the time to add or substract from the original one. If the operation is a sum, the variable add_or_sub
    must be "add", otherwise, must be "sub".'''
    # Define the variable where put the new time.
    new_time = []

    # Get the hours, minutes and seconds for each time.
    elements = ["hours", "minutes", "seconds"]
    dic1, dic2 = dict(), dict()
    for e,t1,t2 in zip(elements, time1.split(":"), time2.split(":")):
        dic1[e] = t1
        dic2[e] = t2

    # Operate between times
    if(add_or_sub == "add"):
        rest = 0
        for e in elements[::-1]: # The elements order is inverted so seconda must be evaluated first.
            # The first condition deals with the secons-miliseconds separation be a ",".
            if(e=="seconds"):
                sec1, m_sec1 = dic1[e].split(",")
                sec2, m_sec2 = dic2[e].split(",")
                m_sec = int(m_sec1) + int(m_sec2)
                if(m_sec >=1000):
                    m_sec -= 1000
                    rest = 1
                else:
                    rest = 0

                if(len(str(m_sec)) == 1):
                    m_sec = "{}00".format(m_sec)
                elif(len(str(m_sec)) == 2):
                    m_sec = "{}0".format(m_sec)
                else:
                    m_sec = str(m_sec)

                sec = int(sec1) + int(sec2) + rest
                if(sec >=60):
                    sec -= 60
                    rest = 1
                else:
                    rest = 0

                if(len(str(sec)) == 1):
                    sec = "0{}".format(sec)
                else:
                    sec = str(sec)

                new_time.append("{},{}".format(sec, m_sec))
            # The second condition works with the minutes and hours.
            else:
                num = int(dic1[e]) + int(dic2[e]) + rest
                if(num>=60):
                    num -= 60
                    rest = 1
                else:
                    rest = 0

                if(len(str(num)) == 1):
                    num = "0{}".format(num)
                else:
                    num = str(num)

                new_time.append(num)
    elif(add_or_sub == "sub"):
        rest = 0
        for e in elements[::-1]: # The elements order is inverted so seconda must be evaluated first.
            # The first condition deals with the secons-miliseconds separation be a ",".
            if(e=="seconds"):
                sec1, m_sec1 = dic1[e].split(",")
                sec2, m_sec2 = dic2[e].split(",")
                m_sec = int(m_sec1) - int(m_sec2)
                if(m_sec < 0):
                    m_sec = m_sec+1000
                    rest = -1
                else:
                    rest = 0

                if(len(str(m_sec)) == 1):
                    m_sec = "{}00".format(m_sec)
                elif(len(str(m_sec)) == 2):
                    m_sec = "{}0".format(m_sec)
                else:
                    m_sec = str(m_sec)

                sec = int(sec1) - int(sec2) + rest
                if(sec < 0):
                    sec = sec+60
                    rest = -1
                else:
                    rest = 0

                if(len(str(sec)) == 1):
                    sec = "0{}".format(sec)
                else:
                    sec = str(sec)

                new_time.append("{},{}".format(sec, m_sec))
            # The second condition works with the minutes and hours.
            else:
                num = int(dic1[e]) - int(dic2[e]) + rest
                if(num < 0):
                    num = num+60
                    rest = -1
                else:
                    rest = 0

                if(len(str(num)) == 1):
                    num = "0{}".format(num)
                else:
                    num = str(num)

                new_time.append(num)

    return ":".join(new_time[::-1]) # Invert the order agains so the hours are the first ones to write.


# Define the new variable where to save the new subtitles.
new_sub = ""

# Get each line of the originals "srt" file and the ones with time, changes them as indicated.
with open("subs.srt") as file: #¡¡¡¡¡¡¡¡¡¡¡¡IMPORTANT HERE PUT THE NAME OF THE FILE, OR CHANGE THE FILE'S NAME!!!!!!!!!!!
    time_to_change = "00:00:00,500" #¡¡¡¡¡¡¡¡¡¡¡¡IMPORTANT HERE PUT THE SPECIFY THE TIME ("hours:minutes:seconds", seconds with 3 decimals, even if it's al 000) TO ADD OR SUBSTRACT!!!!!!!!!!!
    add_or_sub = "sub" #¡¡¡¡¡¡¡¡¡¡¡¡IMPORTANT HERE PUT THE INDICATE IF THE TIME IS FOR ADD ("add") OR SUBSTRACT ("sub")!!!!!!!!!!!

    for l in file:
        if("-->" in l):
            s_time = l.split(" ")
            for i in range(3):
                if(i!=1):
                    s_time[i] = time_operation(s_time[i], time_to_change, add_or_sub)
            s_time = " ".join(s_time)
            #print(s_time)
            new_sub += s_time + "\n"
        else:
            new_sub += l

# Create a new "srt" file with the result.
with open("new_sub.srt", "w") as file:
    file.write(new_sub)
