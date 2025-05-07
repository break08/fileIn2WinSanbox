import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import tempfile
import random
import os
from tkinter import ttk
import json

vgpu_val = "Disable"
network_val = "Default"
audio_val = "Default"
video_val = "Default"
graphics_val = "Default"
readonly_val = "false"
lang_val = "English"

def langcheck_main():
    if lang_val == "English":
        text1.config (text = "Folder's Location")
        text2.config (text = "Status")
        text3.config (text = ".wsb file's name")
        text4.config (text = "Output Location")
        checkbox1.config (text = "Create .wsb file in Temp folder in AppData")
        checkbox2.config (text = "Open in Windows Sanbox when when the creation process is complete")
        checkbox3.config (text = "Random name for Folder")
        button2.config (text = "Direct Folder")
        button3.config (text = "Start")
        button4.config (text = "Direct Output Folder")
        button5.config (text = "Advanced")
        button6.config (text = "Personalize")
        label1.config (text = "Waiting for input ....")
    if lang_val == "Tiếng Việt":
        text1.config (text = "Đường dẫn đến thư mục")
        text2.config (text = "Trạng thái")
        text3.config (text = "Tên file .wsb")
        text4.config (text = "Đường dẫn đến thư mục đầu ra")
        checkbox1.config (text = "Tạo file .wsb trong thư mục Temp trong AppData")
        checkbox2.config (text = "Mở trong Windows Sanbox khi quá trình tạo hoàn tất")
        checkbox3.config (text = "Tên ngẫu nhiên cho thư mục")
        button2.config (text = "Chọn thư mục")
        button3.config (text = "Bắt đầu")
        button4.config (text = "Chọn thư mục đầu ra")
        button5.config (text = "Nâng cao")
        button6.config (text = "Cá nhân hóa")
        label1.config (text = "Đang chờ nhập ....")
    if lang_val == "中国人":
        text1.config (text = "文件夹位置")
        text2.config (text = "状态")
        text3.config (text = ".wsb 文件名")
        text4.config (text = "输出位置")
        checkbox1.config (text = "在 AppData 的 Temp 文件夹中创建 .wsb 文件 ")
        checkbox2.config (text = "创建完成后在 Windows Sanbox 中打开")
        checkbox3.config (text = "文件夹的随机名称")
        button2.config (text = "选择文件夹")
        button3.config (text = "开始")
        button4.config (text = "选择输出文件夹")
        button5.config (text = "高级")
        button6.config (text = "个性化")
        label1.config (text = "等待输入 ....")
def direct_folder():
    folder = filedialog.askdirectory (title = "Select your folder")
    entry_locate.delete (0, tk.END)
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
def advanced():
    adv = tk.Tk()
    adv.geometry ("500x500")
    adv.title ("Advanced")

    def langcheck_advanced():
        if lang_val == "English":
            text1a.config (text = "VGPU")
            text2a.config (text = "Network")
            text3a.config (text = "Audio")
            text4a.config (text = "Video")
            text5a.config (text = "Graphics")
            text6a.config (text = "Read Only")
            save.config (text = "Save")
        if lang_val == "Tiếng Việt":
            text1a.config (text = "VGPU")
            text2a.config (text = "Mạng")
            text3a.config (text = "Âm thanh")
            text4a.config (text = "Video")
            text5a.config (text = "Đồ họa")
            text6a.config (text = "Chỉ đọc")
            save.config (text = "Lưu")
        if lang_val == "中国人":
            text1a.config (text = "VGPU")
            text2a.config (text = "网络")
            text3a.config (text = "音频")
            text4a.config (text = "视频")
            text5a.config (text = "图形")
            text6a.config (text = "只读")
            save.config (text = "保存")

    text1a = tk.Label (adv, text = "VGPU")
    text1a.place (x = 5, y = 10)

    vgpu = ttk.Combobox (adv, values = ["Enable", "Disable"])
    vgpu.place (x = 80, y = 10)

    network = ttk.Combobox (adv, values = ["Default", "Disable"])
    network.place (x = 80, y = 50)

    text2a = tk.Label (adv, text = "Network")
    text2a.place (x = 5, y = 50)

    text3a = tk.Label (adv, text = "Audio")
    text3a.place (x = 5, y = 90)

    audio = ttk.Combobox (adv, values = ["Default", "Disable"])
    audio.place (x = 80, y = 90)

    text4a = tk.Label (adv, text = "Video")
    text4a.place (x = 5, y = 130)

    video = ttk.Combobox (adv, values = ["Default", "Disable"])
    video.place (x = 80, y = 130)

    text5a = tk.Label (adv, text = "Graphics")
    text5a.place (x = 5, y = 170)

    graphics = ttk.Combobox (adv, values = ["Default", "Disable"])
    graphics.place (x = 80, y = 170)

    readonly = ttk.Combobox (adv, values = ["true", "false"])
    readonly.place (x = 80, y = 210)

    text6a = tk.Label (adv, text = "Read Only")
    text6a.place (x = 5, y = 210)

    with open ("user-change.json", "r") as f:
        data = json.load (f)
    
    global vgpu_val, network_val, audio_val, video_val, graphics_val, readonly_val

    if data["vgpu"] == "0":
        vgpu_val = "Disable"
        vgpu.set ("Disable")
    else:
        vgpu_val = "Enable"
        vgpu.set ("Enable")

    if data["network"] == "0":
        network_val = "Disable"
        network.set ("Disable")
    else:
        network_val = "Default"
        network.set ("Default")
    
    if data["audio"] == "0":
        audio_val = "Disable"
        audio.set ("Disable")
    else:
        audio_val = "Default"
        audio.set ("Default")
    
    if data["video"] == "0":
        video_val = "Disable"
        video.set ("Disable")
    else:
        video_val = "Default"
        video.set ("Default")
    
    if data["graphicsgpu"] == "0":
        graphics_val = "Disable"
        graphics.set ("Disable")
    else:
        graphics_val = "Default"
        graphics.set ("Default")

    if data["readonly"] == "0":
        readonly_val = "false"
        readonly.set ("false")
    else:
        readonly_val = "true"
        readonly.set ("true")

    def changes():
        #check
        global vgpu_val, network_val, audio_val, video_val, graphics_val, readonly_val
        if vgpu.get () == "Enable":
            vgpu_val = "Enable"
            data["vgpu"] = "1"
        else:
            vgpu_val = "Disable"
            data["vgpu"] = "0"
        
        if network.get () == "Default":
            network_val = "Default"
            data["network"] = "1"
        else:
            network_val = "Disable"
            data["network"] = "0"
        
        if audio.get () == "Default":
            audio_val = "Default"
            data["audio"] = "1"
        else:
            audio_val = "Disable"
            data["audio"] = "0"
        
        if video.get () == "Default":
            video_val = "Default"
            data["video"] = "1"
        else:
            video_val = "Disable"
            data["video"] = "0"

        if graphics.get () == "Default":
            graphics_val = "Default"
            data["graphicsgpu"] = "1"
        else:
            graphics_val = "Disable"
            data["graphicsgpu"] = "0"
        
        if readonly.get () == "true":
            readonly_val = "true"
            data["readonly"] = "1"
        else:
            readonly_val = "false"
            data["readonly"] = "0"
        
        #write
        with open ("user-change.json", "w") as f:
            json.dump (data, f, indent = 4)
    
    save = tk.Button (adv, text = "Save", command = changes)
    save.place (x = 250, y = 10)

    langcheck_advanced()    
        
    vgpu.set (vgpu_val)

    adv.mainloop()
def personalize():
    setting = tk.Tk()
    setting.title ("Personalize")
    setting.geometry ("500x500")
    def langcheck_personalize():
        if lang_val == "English":
            note1.config (text = "Language")
            save.config (text = "Save")
        if lang_val == "Tiếng Việt":
            note1.config (text = "Ngôn ngữ")
            save.config (text = "Lưu")
        if lang_val == "中国人":
            note1.config (text = "语言")
            save.config (text = "保存")
    note1 = tk.Label (setting, text = "Language")
    note1.place (x = 10, y = 10)
    lang = ttk.Combobox (setting, values = ["English", "Tiếng Việt", "中国人"])
    lang.place (x = 80, y = 10)
    with open ("user-change.json", "r") as f:
        data = json.load (f)
    global lang_val
    if data["language"] == "english":
        lang_val = "English"
        lang.set ("English")
    elif data["language"] == "vietnamese":
        lang_val = "Tiếng Việt"
        lang.set ("Tiếng Việt")
    elif data["language"] == "chinese":
        lang_val = "中国人"
        lang.set ("中国人")
    def save_set ():
        global lang_val
        with open ("user-change.json", "w") as f:
            if lang.get () == "English":
                lang_val = "English"
                data["language"] = "english"
            elif lang.get () == "Tiếng Việt":
                lang_val = "Tiếng Việt"
                data["language"] = "vietnamese"
            elif lang.get () == "中国人":
                lang_val = "中国人"
                data["language"] = "chinese"
            json.dump (data, f, indent = 4)
        langcheck_main()
        langcheck_personalize()
    save = tk.Button (setting, text = "Save", command = save_set)
    save.place (x = 250, y = 10)
    langcheck_personalize()
    setting.mainloop()
def creat():
    output_folder = entry_ouput.get()
    if not entry_filename.get()[-4:] == ".wsb":
        entry_filename.insert (tk.END, ".wsb")
    filename = entry_filename.get()
    file_locate = entry_locate.get()
    file_locate = file_locate.replace ("/", "\\")
    filepathc = os.path.join(output_folder, filename)
    if not entry_filename.get() == "" and not entry_locate.get() == "" and not entry_ouput.get() == "":
        entry_locate.config (state = "disabled")
        entry_filename.config (state = "disabled")
        entry_ouput.config (state = "disabled")
        if lang_val == "English":
            label1.config (text = "Creating file...")
        elif lang_val == "Tiếng Việt":
            label1.config (text = "Đang tạo file...")
        elif lang_val == "中国人":
            label1.config (text = "正在创建文件...")
        example = f"""
<Configuration>
    <VGpu>{vgpu_val}</VGpu>
    <MappedFolders>
        <MappedFolder>
            <HostFolder>{file_locate}</HostFolder>
            <ReadOnly>{readonly_val}</ReadOnly>
        </MappedFolder>
    </MappedFolders>
    <ReadOnly>{readonly_val}</ReadOnly>
    <Networking>{network_val}</Networking>
    <AudioInput>{audio_val}</AudioInput>
    <VideoInput>{video_val}</VideoInput>
    <GraphicsGPU>{graphics_val}</GraphicsGPU>
</Configuration>
"""
        with open (filepathc, "w") as f:
            f.write (example)
        if val_openinsandbox.get () == 1:
            os.startfile (filepathc)
        if lang_val == "English":
            label1.config (text = "File Created Successfully")
        elif lang_val == "Tiếng Việt":
            label1.config (text = "Tạo file thành công")
        entry_locate.config (state = "normal")
        entry_filename.config (state = "normal")
        entry_ouput.config (state = "normal")
        file_content.delete (1.0, tk.END)
        file_content.insert(tk.END, example)
    else:
        messagebox.showerror ("Error", "Please fill all fields")
        label1.config (text = "Error, try again")
with open ("user-change.json", "r") as f:
    data = json.load (f)
main = tk.Tk()
main.geometry ("660x800")
main.title ("fileIn2WinSanbox v3.0 beta")
icon_path = 'icon/icon.ico'
main.iconbitmap(icon_path)

val_ranname = tk.IntVar (main, value = 0)
val_creatintemp = tk.IntVar (main, value = 0)
val_openinsandbox = tk.IntVar (main, value = 0)

#main
text1 = tk.Label (main, text = "Folder's Location")
text2 = tk.Label (main, text = "Status")
text3 = tk.Label (main, text = ".wsb file's name")
text4 = tk.Label (main, text = "Output Location")
checkbox1 = tk.Checkbutton (main, text = "Create .wsb file in Temp folder in AppData", variable = val_creatintemp, command = creat_in_temp)
checkbox2 = tk.Checkbutton (main, text = "Open in Windows Sanbox when when the creation process is complete", variable = val_openinsandbox)
checkbox3 = tk.Checkbutton (main, text = "Random name for Folder", variable = val_ranname, command = random_name)
button2 = tk.Button (main, text = "Direct Folder", command = direct_folder)
button3 = tk.Button (main, text="Start", command = creat)
button4 = tk.Button (main, text="Direct Output Folder", command = direct_output_folder)
button5 = tk.Button (main, text="Advanced", command = advanced)
button6 = tk.Button (main, text="Personalize", command = personalize)
label1 = tk.Label (main, text = "Waiting for input ....", bg = "white", width = 40, height = 8)
entry_locate = tk.Entry (main)
entry_filename = tk.Entry (main)
entry_ouput = tk.Entry (main)
file_content = tk.Text (main, wrap = "char", width = 80, height = 20)
sbar1 = tk.Scrollbar (main, orient = "vertical", command = file_content.yview)
sbar2 = tk.Scrollbar (main, orient = "horizontal", command = file_content.xview)
file_content.config (yscrollcommand = sbar1.set, xscrollcommand = sbar2.set)

#pack
text1.place (x = 10, y = 10)
text2.place (x = 10, y = 50)
text3.place (x = 10, y = 200)
text4.place (x = 200, y = 10)
checkbox1.place (x = 10, y = 250)
checkbox2.place (x = 10, y = 270)
checkbox3.place (x = 10, y = 290)
button2.place (x = 10, y = 320)
label1.place (x = 10, y = 70)
entry_locate.place (x = 10, y = 30)
entry_filename.place (x = 10, y = 220)
entry_ouput.place (x = 200, y = 30)
file_content.place (x = 10, y = 400)
button3.place (x = 10, y = 350)
button4.place (x = 100, y = 350)
button5.place (x = 200, y = 290)
button6.place (x = 100, y = 320)

#language
if data["language"] == "english":
    lang_val = "English"
elif data["language"] == "vietnamese":
    lang_val = "Tiếng Việt"
elif data["language"] == "chinese":
    lang_val = "中国人"
langcheck_main()

main.mainloop()