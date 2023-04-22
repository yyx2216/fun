from tkinter import *
import os,sys,json
add = os.path.abspath('..')
dirs = os.listdir(f'{add}/file')
with open (f'{add}/cfg.json','r') as cfg:
        cfg_log = json.load(cfg)
        exit_key = cfg_log['exit_keyboard']
        sound = cfg_log['sound:0~100']
        sound_of = cfg_log['sound:on/off']
        doing = cfg_log['do:yes/no']
        win_of = cfg_log['win:yes/no']   
        boot_start = cfg_log['Boot_start:yes/no']              
sound_list = {0: -65.25, 1: -56.99, 2: -51.67, 3: -47.74, 4: -44.62, 5: -42.03, 6: -39.82, 7: -37.89, 8: -36.17, 9: -34.63, 10: -33.24,
        11: -31.96, 12: -30.78, 13: -29.68, 14: -28.66, 15: -27.7, 16: -26.8, 17: -25.95, 18: -25.15, 19: -24.38, 20: -23.65,
        21: -22.96, 22: -22.3, 23: -21.66, 24: -21.05, 25: -20.46, 26: -19.9, 27: -19.35, 28: -18.82, 29: -18.32, 30: -17.82,
        31: -17.35, 32: -16.88, 33: -16.44, 34: -16.0, 35: -15.58, 36: -15.16, 37: -14.76, 38: -14.37, 39: -13.99, 40: -13.62,
        41: -13.26, 42: -12.9, 43: -12.56, 44: -12.22, 45: -11.89, 46: -11.56, 47: -11.24, 48: -10.93, 49: -10.63, 50: -10.33,
        51: -10.04, 52: -9.75, 53: -9.47, 54: -9.19, 55: -8.92, 56: -8.65, 57: -8.39, 58: -8.13, 59: -7.88, 60: -7.63,
        61: -7.38, 62: -7.14, 63: -6.9, 64: -6.67, 65: -6.44, 66: -6.21, 67: -5.99, 68: -5.76, 69: -5.55, 70: -5.33,
        71: -5.12, 72: -4.91, 73: -4.71, 74: -4.5, 75: -4.3, 76: -4.11, 77: -3.91, 78: -3.72, 79: -3.53, 80: -3.34,
        81: -3.15, 82: -2.97, 83: -2.79, 84: -2.61, 85: -2.43, 86: -2.26, 87: -2.09, 88: -1.91, 89: -1.75, 90: -1.58,
        91: -1.41, 92: -1.25, 93: -1.09, 94: -0.93, 95: -0.77, 96: -0.61, 97: -0.46, 98: -0.3, 99: -0.15, 100: 0.0}
sound = sound_list[sound]
win = Tk()
win.resizable(False, False)
screenw = win.winfo_screenwidth()
screenh = win.winfo_screenheight()
win.geometry("%dx%d+%d+%d" % (200, 150, (screenw - 200) / 2, (screenh - 150) / 2))
def do():
    def Q(event):
        sys.exit()
    for file in dirs:
        os.startfile(f'{add}\\file\\{file}')
    if win_of == "yes":
        win2 = Tk()
        win2.geometry("%dx%d+%d+%d" % (screenw*1.2, screenh*1.2, (screenw - screenw*1.2) / 2, (screenh - screenh*1.2) / 2))
        win2.resizable(False, False)
        win2.attributes('-alpha', 0.01)
        win2.attributes("-topmost", 1)
        win2.overrideredirect(True) 
        win2.bind(f'<{exit_key}>', Q)
        win2.mainloop()
    if sound_of == 'on':
        from ctypes import cast, POINTER
        from comtypes import CLSCTX_ALL
        from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        volume.SetMasterVolumeLevel(sound, None)
if doing == 'yes':
    do()
button = Button(win,text='点我',font=('微软雅黑',40),command=do,bg='green').pack()
win.mainloop()





