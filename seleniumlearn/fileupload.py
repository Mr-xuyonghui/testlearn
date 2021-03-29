import win32con
import win32gui
def upload(filepath,browser_type="chrome"):
    if browser_type == "chrome":
        title = "打开"
    else:
        title = ""
    dialog = win32gui.FindWindow("#32770",title)
    ComboBoxEx32 = win32gui.FindWindowEx(dialog,0,"ComboBoxEx32",None)
    ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, "ComboBox", None)
    #编辑按钮
    edit = win32gui.FindWindowEx(ComboBox,0,'Edit',None)
    #打开按钮
    button = win32gui.FindWindowEx(dialog,0,'Button',"打开(&0)")
    #往编辑中输入文件路径
    win32gui.SendMessage(edit,win32con.WN_SERRECT,None,filepath)
    win32gui.SendMessage(dialog,win32con.WN_COMMAND,1,button)