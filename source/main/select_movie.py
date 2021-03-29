import tkinter as tk

def selecting_movie(df):
    mov = []
    movies_titles = df['movie title']
    # Create the root window
    root = tk.Tk()
    root.title("List of Movies")
    root.geometry('500x500')
    scrollbar = tk.Scrollbar(root)
    scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

    # Create a listbox
    listbox = tk.Listbox(root, width=100, height=200, selectmode=tk.SINGLE)
    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)

    # Inserting the listbox items
    for item in movies_titles:
        listbox.insert(tk.END, item)

    # Function for printing the
    # selected listbox value(s)

    def selected_item():
        # Traverse the tuple returned by
        # curselection method and print
        # correspoding value(s) in the listbox

        for i in listbox.curselection():
            mov.append(listbox.get(i))
            root.quit()
            # return listbox.get(i)

    # Create a button widget and
    # map the command parameter to
    # selected_item function
    btn = tk.Button(root, text='Select Movie', command=selected_item)

    # Placing the button and listbox
    btn.pack(side='bottom')
    listbox.pack()
    root.mainloop()
    return mov[0]
