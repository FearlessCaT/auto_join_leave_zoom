from datetime import datetime
from os import system
import re
import time
import webbrowser
import sys
import pyaudio
import audioop
p = pyaudio.PyAudio()

def date_joinInput():
    date_join = input("input date :")
    if date_join.isnumeric():
        date_join_int = int(date_join)
        if date_join_int <32 and date_join_int >9 :
            return date_join
        elif date_join_int <10 and date_join_int >0:
            date_join_str = "0" + str(date_join)
            return date_join_str
        else:
            print ("date must be between 1-31")
            date_joinInput()
    else:
        print ("date must be between 1-31")
        date_joinInput()
        

def month_joinInput():
    month_join = input("input month :")
    if month_join.isnumeric():
        month_join_int = int(month_join)
        if month_join_int <13 and month_join_int >9 :
            return month_join
        elif month_join_int <10 and month_join_int >0:
            month_join_str = "0" + str(month_join)
            return month_join_str
        else:
            print ("month must be between 1-12")
            month_joinInput()
    else:
        print ("month must be between 1-12")
        month_joinInput()

def year_joinInput():
    year_join = input("input year :")
    if year_join.isnumeric():
        year_join_int = int(year_join)
        if year_join_int <100:
            year_join_int = year_join_int + 2000
            return year_join_int
        elif year_join_int >2500:
            year_join_int = year_join_int - 543
            return year_join_int
        elif year_join_int <2100 and year_join >2000:
            year_join_int = year_join_int
            return year_join_int
        else: 
            print ("invalid year re-enter again")
            year_joinInput()
    else:
        print ("invalid year re-enter again")
        year_joinInput()

def hour_joinInput():
    hour_join = input("hours (skip = 00) :")
    if hour_join == "":
        hour_join = "00"
        return hour_join
    elif hour_join.isnumeric():
        hour_join_int = int(hour_join)
        if hour_join_int <25 and hour_join_int >9:
            return hour_join_int
        elif hour_join_int <10 and hour_join_int >=0:
            hour_join_str = "0" + str(hour_join)
            return hour_join_str
        else:
            print("hours must be between 0-24")
            hour_joinInput()
    else:
        print("hours must be between 1-60")
        hour_joinInput()

def min_joinInput():
    min_join = input("minutes (skip = 00) :")
    if min_join == "":
        min_join = "00"
        return min_join
    elif min_join.isnumeric():
        min_join_int = int(min_join)
        if min_join_int <61 and min_join_int >9:
            return min_join_int
        elif min_join_int <10 and min_join_int >=0:
            min_join_str = "0" + str(min_join)
            return min_join_str
        else:
            print("minute must be between 0-60")
            min_joinInput()
    else:
        print("minute must be between 0-60")
        min_joinInput()

def sec_joinInput():
    sec_join = input("seconds (skip = 00) :")
    if sec_join == "":
        sec_join = "00"
        return sec_join
    elif sec_join.isnumeric():
        sec_join_int = int(sec_join)
        if sec_join_int <61 and sec_join_int >9:
            return sec_join_int
        elif sec_join_int <10 and sec_join_int >=0:
            sec_join_str = "0" + str(sec_join)
            return sec_join_str
        else:
            print("seconds must be between 0-60")
            sec_joinInput()
    else:
        print("seconds must be between 0-60")
        sec_joinInput()

def date_leaveInput():
    date_leave = input("input date :")
    if date_leave.isnumeric():
        date_leave_int = int(date_leave)
        if date_leave_int <32 and date_leave_int >9 :
            return date_leave
        elif date_leave_int <10 and date_leave_int >0:
            date_leave_str = "0" + str(date_leave)
            return date_leave_str
        else:
            print ("date must be between 1-31")
            date_leaveInput()
    else:
        print ("date must be between 1-31")
        date_leaveInput()
        

def month_leaveInput():
    month_leave = input("input month :")
    if month_leave.isnumeric():
        month_leave_int = int(month_leave)
        if month_leave_int <13 and month_leave_int >9 :
            return month_leave
        elif month_leave_int <10 and month_leave_int >0:
            month_leave_str = "0" + str(month_leave)
            return month_leave_str
        else:
            print ("month must be between 1-12")
            month_leaveInput()
    else:
        print ("month must be between 1-12")
        month_leaveInput()

def year_leaveInput():
    year_leave = input("input year :")
    if year_leave.isnumeric():
        year_leave_int = int(year_leave)
        if year_leave_int <100:
            year_leave_int = year_leave_int + 2000
            return year_leave_int
        elif year_leave_int >2500:
            year_leave_int = year_leave_int - 543
            return year_leave_int
        elif year_leave_int <2100 and year_leave >2000:
            year_leave_int = year_leave_int
            return year_leave_int
        else: 
            print ("invalid year re-enter again")
            year_leaveInput()
    else:
        print ("invalid year re-enter again")
        year_leaveInput()

def hour_leaveInput():
    hour_leave = input("hours (skip = 00) :")
    if hour_leave == "":
        hour_leave = "00"
        return hour_leave
    elif hour_leave.isnumeric():
        hour_leave_int = int(hour_leave)
        if hour_leave_int <25 and hour_leave_int >9:
            return hour_leave_int
        elif hour_leave_int <10 and hour_leave_int >=0:
            hour_leave_str = "0" + str(hour_leave)
            return hour_leave_str
        else:
            print("hours must be between 0-24")
            hour_leaveInput()
    else:
        print("hours must be between 1-60")
        hour_leaveInput()

def min_leaveInput():
    min_leave = input("minutes (skip = 00) :")
    if min_leave == "":
        min_leave = "00"
        return min_leave
    elif min_leave.isnumeric():
        min_leave_int = int(min_leave)
        if min_leave_int <61 and min_leave_int >9:
            return min_leave_int
        elif min_leave_int <10 and min_leave_int >=0:
            min_leave_str = "0" + str(min_leave)
            return min_leave_str
        else:
            print("minute must be between 0-60")
            min_leaveInput()
    else:
        print("minute must be between 0-60")
        min_leaveInput()

def sec_leaveInput():
    sec_leave = input("seconds (skip = 00) :")
    if sec_leave == "":
        sec_leave = "00"
        return sec_leave
    elif sec_leave.isnumeric():
        sec_leave_int = int(sec_leave)
        if sec_leave_int <61 and sec_leave_int >9:
            return sec_leave_int
        elif sec_leave_int <10 and sec_leave_int >=0:
            sec_leave_str = "0" + str(sec_leave)
            return sec_leave_str
        else:
            print("seconds must be between 0-60")
            sec_leaveInput()
    else:
        print("seconds must be between 0-60")
        sec_leaveInput()

#function confirm
def confirmjoinInput():
    confirm = input ("confirm (Y = yes N = no) :")
    if confirm == "Y" or confirm == "y":
        return
    elif confirm == "N" or confirm == "n":
        join_input()
    else:
        confirmjoinInput()

def confirmleaveInput():
    confirm = input ("confirm (Y = yes N = no) :")
    if confirm == "Y" or confirm == "y":
        return
    elif confirm == "N" or confirm == "n":
        leave_input()
    else:
        confirmleaveInput()

def join_input():
    #input detail
    url = input("paste url here :")
    date_join_fn = str(date_joinInput())
    month_join_fn = str(month_joinInput())    
    year_join_fn = str(year_joinInput())
    hour_join_fn = str(hour_joinInput())
    min_join_fn = str(min_joinInput())
    sec_join_fn = str(sec_joinInput())

    datetime_str_join = date_join_fn + "/" + month_join_fn + "/" + year_join_fn + " " + hour_join_fn + ":" + min_join_fn + ":" + sec_join_fn
    print("going to join" + " " + url + " " + "at" + " " + datetime_str_join)

    confirmjoinInput()

    at_trigger_join = datetime.strptime(datetime_str_join, "%d/%m/%Y %H:%M:%S")
    return at_trigger_join , url

def leave_input():
    type_l = input("set auto leave meeting \n [1] basic : will leave at given time \n\n [2] advance : will leave after the given time and no audio detect for 100 seconds \n\n Choice:")
    if type_l == "1" or type == "[1]":
        print ("will leave at given time")
        date_leave_fn = str(date_leaveInput())
        month_leave_fn = str(month_leaveInput())    
        year_leave_fn = str(year_leaveInput())
        hour_leave_fn = str(hour_leaveInput())
        min_leave_fn = str(min_leaveInput())
        sec_leave_fn = str(sec_leaveInput())
        datetime_str_leave = date_leave_fn + "/" + month_leave_fn + "/" + year_leave_fn + " " + hour_leave_fn + ":" + min_leave_fn + ":" + sec_leave_fn
        print("going to leave" + " " + "at" + " " + datetime_str_leave)
        confirmleaveInput()
        at_trigger_leave = datetime.strptime(datetime_str_leave, "%d/%m/%Y %H:%M:%S")
        return at_trigger_leave , "1"

    elif type_l == "2" or type_l == "[2]":
        print("will leave after the given time and no audio detect for 100 seconds (please play via aux jack)")
        date_leave_fn = str(date_leaveInput())
        month_leave_fn = str(month_leaveInput())    
        year_leave_fn = str(year_leaveInput())
        hour_leave_fn = str(hour_leaveInput())
        min_leave_fn = str(min_leaveInput())
        sec_leave_fn = str(sec_leaveInput())
        datetime_str_leave = date_leave_fn + "/" + month_leave_fn + "/" + year_leave_fn + " " + hour_leave_fn + ":" + min_leave_fn + ":" + sec_leave_fn
        print("going to search for sound" + " " + "at" + " " + datetime_str_leave)
        confirmleaveInput()
        at_trigger_leave = datetime.strptime(datetime_str_leave, "%d/%m/%Y %H:%M:%S")
        for i in range(p.get_device_count()):
            dev = p.get_device_info_by_index(i)
            print(dev.get('name'))
            loop = 0
            if dev.get('name') == "Stereo Mix (Realtek(R) Audio)":
                index_stereo_mix = i
                break
            elif loop >7:
                print("stereo mix is not found please enable stereo mix in volume mixer in control panel")
                leave_input()
            else:
                loop = loop + 1
        return at_trigger_leave , "2" , index_stereo_mix
    else:
        leave_input()

def sound_detect(index_stereo_mix):
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    RATE = 44100
    silent_threshold = 4
    timeleave = 100
    device = index_stereo_mix
    stream = p.open(format=FORMAT, channels = p.get_device_info_by_index(device).get('maxInputChannels') , rate=RATE, input = True ,  frames_per_buffer=CHUNK , input_device_index = device)
    while True:
        data=stream.read(CHUNK)
        threshold = audioop.max(data , 2)
        if  threshold > silent_threshold :
            print("device is still found sound")
            timeleave = 100
        else :
            print("Sound not found countdown" + " " + str(timeleave))
            print ("don't close this program it will autoexit after target time")  
            time.sleep(1)
            timeleave = timeleave - 1
            if timeleave == 0:
                system('taskkill /F /FI "WINDOWTITLE eq Zoom*" ')
                p.terminate()
                return

print("made by FearlessCaT")
joinInput = join_input()
leaveInput = leave_input()
at_trigger_join = joinInput[0]
url = joinInput[1]
at_trigger_leave = leaveInput[0]
typeLeave = leaveInput[1]
index_stereo_mix = leaveInput[2]
datenow = datetime.now()
duration_join = at_trigger_join - datenow
duration_sec_join = duration_join.total_seconds()
duration_leave = at_trigger_leave - at_trigger_join
duration_sec_leave = duration_leave.total_seconds()
print(duration_join,duration_leave)
time.sleep(duration_sec_join)
webbrowser.open(url)
time.sleep(duration_sec_leave)
if typeLeave == 1:
    system('taskkill /F /FI "WINDOWTITLE eq Zoom*" ')
    sys.exit()
else:
    sound_detect(index_stereo_mix)
sys.exit()