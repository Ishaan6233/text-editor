import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.messagebox import showinfo
from tkinter.simpledialog import askstring


def text_editor():
    def open_file():
        filepath = askopenfilename(
            filetypes=[('Text Files', '*.txt'), ('All Files', '*.*')]
        )

        if not filepath:
            return

        txt_edit.delete(1.0, tk.END)
        with open(filepath, 'r') as input_file:
            text = input_file.read()
            txt_edit.insert(tk.END, text)
        window.title(f'Text Editor - {filepath}')

    def save_file():
        filepath = asksaveasfilename(
            defaultextension='txt',
            filetypes=[('Text Files', '*.txt'), ('All Files', '*.*')],
        )

        if not filepath:
            return

        with open(filepath, 'w') as output_file:
            text = txt_edit.get(1.0, tk.END)
            output_file.write(text)
        window.title(f'Text Editor - {filepath}')

    def cut():
        txt_edit.event_generate("<<Cut>>")

    def copy():
        txt_edit.event_generate("<<Copy>>")

    def paste():
        txt_edit.event_generate("<<Paste>>")

    def undo():
        txt_edit.event_generate("<<Undo>>")

    def redo():
        txt_edit.event_generate("<<Redo>>")

    def find():
        find_string = askstring("Find", "Enter text to find:")
        txt_edit.tag_remove('found', '1.0', tk.END)
        if find_string:
            idx = '1.0'
            while 1:
                idx = txt_edit.search(find_string, idx, nocase=1, stopindex=tk.END)
                if not idx:
                    break
                lastidx = f"{idx}+{len(find_string)}c"
                txt_edit.tag_add('found', idx, lastidx)
                idx = lastidx
            txt_edit.tag_config('found', foreground='red', background='yellow')

    def replace():
        find_string = askstring("Find", "Enter text to find:")
        replace_string = askstring("Replace", "Enter text to replace with:")
        text_content = txt_edit.get('1.0', tk.END)
        new_content = text_content.replace(find_string, replace_string)
        txt_edit.delete('1.0', tk.END)
        txt_edit.insert(tk.END, new_content)

    def word_count():
        text_content = txt_edit.get('1.0', tk.END)
        words = len(text_content.split())
        showinfo("Word Count", f"Words: {words}")

    window = tk.Tk()
    window.title('Text Editor')
    window.rowconfigure(0, minsize=800, weight=1)
    window.columnconfigure(1, minsize=800, weight=1)

    txt_edit = tk.Text(window, undo=True)
    fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
    btn_open = tk.Button(fr_buttons, text='Open', command=open_file)
    btn_save = tk.Button(fr_buttons, text='Save As...', command=save_file)
    btn_cut = tk.Button(fr_buttons, text='Cut', command=cut)
    btn_copy = tk.Button(fr_buttons, text='Copy', command=copy)
    btn_paste = tk.Button(fr_buttons, text='Paste', command=paste)
    btn_undo = tk.Button(fr_buttons, text='Undo', command=undo)
    btn_redo = tk.Button(fr_buttons, text='Redo', command=redo)
    btn_find = tk.Button(fr_buttons, text='Find', command=find)
    btn_replace = tk.Button(fr_buttons, text='Replace', command=replace)
    btn_word_count = tk.Button(fr_buttons, text='Word Count', command=word_count)

    btn_open.grid(row=0, column=0, sticky='ew', padx=5, pady=5)
    btn_save.grid(row=1, column=0, sticky='ew', padx=5, pady=5)
    btn_cut.grid(row=2, column=0, sticky='ew', padx=5, pady=5)
    btn_copy.grid(row=3, column=0, sticky='ew', padx=5, pady=5)
    btn_paste.grid(row=4, column=0, sticky='ew', padx=5, pady=5)
    btn_undo.grid(row=5, column=0, sticky='ew', padx=5, pady=5)
    btn_redo.grid(row=6, column=0, sticky='ew', padx=5, pady=5)
    btn_find.grid(row=7, column=0, sticky='ew', padx=5, pady=5)
    btn_replace.grid(row=8, column=0, sticky='ew', padx=5, pady=5)
    btn_word_count.grid(row=9, column=0, sticky='ew', padx=5, pady=5)

    fr_buttons.grid(row=0, column=0, sticky='ns')
    txt_edit.grid(row=0, column=1, sticky='nsew')

    menu_bar = tk.Menu(window)
    file_menu = tk.Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="Open", command=open_file)
    file_menu.add_command(label="Save As...", command=save_file)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=window.quit)
    menu_bar.add_cascade(label="File", menu=file_menu)

    edit_menu = tk.Menu(menu_bar, tearoff=0)
    edit_menu.add_command(label="Cut", command=cut)
    edit_menu.add_command(label="Copy", command=copy)
    edit_menu.add_command(label="Paste", command=paste)
    edit_menu.add_command(label="Undo", command=undo)
    edit_menu.add_command(label="Redo", command=redo)
    edit_menu.add_separator()
    edit_menu.add_command(label="Find", command=find)
    edit_menu.add_command(label="Replace", command=replace)
    menu_bar.add_cascade(label="Edit", menu=edit_menu)

    tools_menu = tk.Menu(menu_bar, tearoff=0)
    tools_menu.add_command(label="Word Count", command=word_count)
    menu_bar.add_cascade(label="Tools", menu=tools_menu)

    window.config(menu=menu_bar)

    window.mainloop()


if __name__ == '__main__':
    text_editor()
