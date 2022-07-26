import tkinter
import tkinter.filedialog
import pygame.mixer as pymix

from tkinter import ANCHOR, END

# ウィンドウの作成
root = tkinter.Tk()
root.title('音楽アプリ')
root.iconbitmap('Tkinter/音楽アプリ/Music_29918.ico')
root.geometry('550x450')
root.resizable(0, 0)

# フォントの定義
basic_font = ('Times New Roman', 12)
list_font = ('Times New Roman', 15)

# 関数の定義
def add_item():
    file_type = [('MP3', '*.mp3'), ('WAV', '*.wav')]
    file_name = tkinter.filedialog.askopenfilename(filetypes=file_type, initialdir='./Dropbox')
    my_list_box.insert(END, file_name)

def remove_item():
    my_list_box.delete(ANCHOR) # 選択したものを削除するためには引数にANCHOR

def clear_list():
    my_list_box.delete(0, END)

def play():
    global music_player
    # 再生中の音楽を停止する
    pymix.quit()

    # 再生するファイルのパスを取得
    n = my_list_box.curselection() # リストボックスが何番目を選択しているかを取得
    sound_file = my_list_box.get(n) # n番目の要素を取得
    
    # 音楽を再生
    pymix.init()
    sounds = pymix.Sound(sound_file)
    music_player = sounds.play()
    music_player.set_volume(0.1) # 0.01刻みで0.00〜1.00まで選択可能

def stop():
    pymix.pause()

def restart():
    pymix.unpause()

def adjust_volume(volume):
    music_player.set_volume(float(volume))

# フレームの作成
input_frame = tkinter.Frame(root)
output_frame = tkinter.Frame(root)
button_frame = tkinter.Frame(root)
vol_frame = tkinter.Frame(root)

input_frame.pack()
output_frame.pack()
button_frame.pack()
vol_frame.pack()

# ファイルに関するボタンを作成
list_add_button = tkinter.Button(input_frame, text='追加', borderwidth=2, font=basic_font, command=add_item)
list_remove_button = tkinter.Button(input_frame, text='選択削除', borderwidth=2, font=basic_font, command=remove_item)
list_clear_button = tkinter.Button(input_frame, text='一括削除', borderwidth=2, font=basic_font, command=clear_list)

list_add_button.grid(row=0, column=0, padx=2, pady=5, ipadx=5)
list_remove_button.grid(row=0, column=1, padx=2, pady=5, ipadx=5)
list_clear_button.grid(row=0, column=2, padx=2, pady=5, ipadx=5)

# スクロールバーの追加
y_scrollbar = tkinter.Scrollbar(output_frame)
x_scrollbar = tkinter.Scrollbar(output_frame, orient='horizontal')


# 音楽リストの作成
my_list_box = tkinter.Listbox(output_frame, width=45, height=15, yscrollcommand=y_scrollbar.set,
                            xscrollcommand=x_scrollbar.set, borderwidth=4, font=list_font)
my_list_box.grid(row=0, column=0)

y_scrollbar.config(command=my_list_box.yview)
y_scrollbar.grid(row=0, column=1, sticky='ns')

x_scrollbar.config(command=my_list_box.xview)
x_scrollbar.grid(row=1, column=0, sticky='we')


# 音楽再生に関するボランの作成
play_button = tkinter.Button(button_frame, text='再生', borderwidth=2, font=basic_font, command=play)
stop_button = tkinter.Button(button_frame, text='一時停止', borderwidth=2, font=basic_font, command=stop)
restart_button = tkinter.Button(button_frame, text='再開', borderwidth=2, font=basic_font, command=restart)

play_button.grid(row=0, column=0, padx=4, pady=5, ipadx=5)
stop_button.grid(row=0, column=1, padx=4, pady=5, ipadx=5)
restart_button.grid(row=0, column=2, padx=4, pady=5, ipadx=5)

# 音量バーの作成
vol_label = tkinter.Label(vol_frame, text='音量', font=basic_font)
# lambdaしなくても関数に引数を渡してくれるスケールバーなら
vol_scale = tkinter.Scale(vol_frame, orient='horizontal', length=300, from_=0.0, to=1.0, resolution=0.01, showvalue=0, command=adjust_volume)
vol_scale.set(0.1)

vol_label.grid(row=0, column=0, padx=2, pady=15)
vol_scale.grid(row=0, column=1, padx=2, pady=15)

# ループ処理
root.mainloop()