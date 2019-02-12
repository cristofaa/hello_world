from tkinter import *
import os,sys,time

ventana=Tk()
ventana.title("ventana para idle")
ventana.geometry("600x500")



#este codigo se va a dividir en dos partes el la vista  y el controlador 
#controlador 

def generar_carpeta_archivo_vista_y_controlador():
  os.system("mkdir nuevo_proyecto;echo #archivo_vista > vista.py;echo #archivo_controlador > controlador.py")







ventana.mainloop()
