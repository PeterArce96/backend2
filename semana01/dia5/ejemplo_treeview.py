from tkinter import *
from tkinter import ttk

app = Tk()
app.geometry('800x250')

tree = ttk.Treeview(app)
tree['columns'] = ('Nombre', 'Email', 'Celular')

tree.column('#0')
# que se oculte la columna del ID
# tree.column('#0', width=0,stretch=NO)
tree.column('Nombre')
tree.column('Email')
tree.column('Celular')

tree.heading('#0',text='id')
tree.heading('Nombre',text='Nombre')
tree.heading('Email',text='Email')
tree.heading('Celular',text='Celular')

tree.grid(row=0,column=0)

# insertar datos
tree.insert('',END,'1',values=('peter arce', 'parce@gmail.com','999999999'), text='01')

app.mainloop()
