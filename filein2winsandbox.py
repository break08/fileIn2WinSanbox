import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import tempfile
import random
import os

vgpu = "Disable"

def direct_folder():
    folder = filedialog.askdirectory (title = "Select your folder")
    entry_locate.insert (0, folder)
def random_name():
    name = random.randint (0, 100000000000000000000000000000)
    entry_filename.delete (0, tk.END)
    entry_filename.insert (0, f"{name}.wsb")
    if val_ranname.get () == 0:
        entry_filename.delete (0, tk.END)
def creat_in_temp():
    if val_creatintemp.get () == 1:
        tempfolder = tempfile.gettempdir ()
        entry_ouput.delete (0, tk.END)
        entry_ouput.insert (0, tempfolder)
        entry_ouput.config (state = "disabled")
    else:
        entry_ouput.config (state = "normal")
        entry_ouput.delete (0, tk.END)
def direct_output_folder():
    folder = filedialog.askdirectory (title = "Select your folder")
    entry_ouput.delete (0, tk.END)
    entry_ouput.insert (0, folder)
def vgpu_status():
    if val_vgpu.get () == 1:
        global vgpu
        vgpu = "Enable"
    else:
        vgpu = "Disable"
def creat():
    output_folder = entry_ouput.get()
    filename = entry_filename.get()
    file_locate = entry_locate.get()
    file_locate = file_locate.replace ("/", "\\")
    filepathc = os.path.join(output_folder, filename)
    if not entry_filename.get() == "" and not entry_locate.get() == "" and not entry_ouput.get() == "":
        entry_locate.config (state = "disabled")
        entry_filename.config (state = "disabled")
        entry_ouput.config (state = "disabled")
        label1.config (text = "Creating file...")
        example = f"""
<Configuration>
    <VGpu>{vgpu}</VGpu>
    <MappedFolders>
        <MappedFolder>
            <HostFolder>{file_locate}</HostFolder>
            <ReadOnly>false</ReadOnly>
        </MappedFolder>
    </MappedFolders>
</Configuration>
"""
        with open (filepathc, "w") as f:
            f.write (example)
        if val_openinsandbox.get () == 1:
            os.startfile (filepathc)
        label1.config (text = "File Created Successfully")
        entry_locate.config (state = "normal")
        entry_filename.config (state = "normal")
        entry_ouput.config (state = "normal")
    else:
        messagebox.showerror ("Error", "Please fill all fields")
        label1.config (text = "Error, try again")

                            
main = tk.Tk()
main.geometry ("500x500")
main.title ("fileIn2WinSanbox v2.0")
icon_path = 'icon/icon.ico'
main.iconbitmap(icon_path)

val_ranname = tk.IntVar (main, value = 0)
val_creatintemp = tk.IntVar (main, value = 0)
val_openinsandbox = tk.IntVar (main, value = 0)
val_vgpu = tk.IntVar (main, value = 0)

text1 = tk.Label (main, text = "Folder's Location")
text2 = tk.Label (main, text = "Status")
text3 = tk.Label (main, text = ".wsb file's name")
text4 = tk.Label (main, text = "Output Location")
checkbox1 = tk.Checkbutton (main, text = "Create .wsb file in Temp folder in AppData", variable = val_creatintemp, command = creat_in_temp)
checkbox2 = tk.Checkbutton (main, text = "Open in Windows Sanbox when when the creation process is complete", variable = val_openinsandbox)
checkbox3 = tk.Checkbutton (main, text = "Random name for Folder", variable = val_ranname, command = random_name)
checkbox4 = tk.Checkbutton (main, text = "Turn on GPU ", variable = val_vgpu, command = vgpu_status)
button2 = tk.Button (main, text = "Direct Folder", command = direct_folder)
button3 = tk.Button (main, text="Start", command = creat)
button4 = tk.Button (main, text="Direct Output Folder", command = direct_output_folder)
label1 = tk.Label (main, text = "Waiting for input ....", bg = "white", width = 40, height = 8)
entry_locate = tk.Entry (main)
entry_filename = tk.Entry (main)
entry_ouput = tk.Entry (main)

text1.place (x = 10, y = 10)
text2.place (x = 10, y = 50)
text3.place (x = 10, y = 200)
text4.place (x = 200, y = 10)
checkbox1.place (x = 10, y = 250)
checkbox2.place (x = 10, y = 270)
checkbox3.place (x = 10, y = 290)
checkbox4.place (x = 200, y = 290)
button2.place (x = 10, y = 320)
label1.place (x = 10, y = 70)
entry_locate.place (x = 10, y = 30)
entry_filename.place (x = 10, y = 220)
entry_ouput.place (x = 200, y = 30)
button3.place (x = 10, y = 350)
button4.place (x = 100, y = 350)

main.mainloop()