from tkinter import *
import os,sys,time

ventana=Tk()
ventana.title("ventana para idle")
ventana.geometry("600x500")



#este codigo se va a dividir en dos partes el la vista  y el controlador 
#controlador 

def generar_carpeta_archivo_vista_y_controlador():
  os.system("mkdir nuevo_proyecto;echo #archivo_vista > vista.py;echo #archivo_controlador > controlador.py")
  archivo_vista = open("nuevo_proyecto/vista.py","U")
  archivo_controlador = open("nuevo_proyecto/controlador.py","U")
  archivo_vista.write(" from tkinter import* \nimport time,mathventana = tk(  ventana.title("titulo del archivo ") ventana.geometry("500x600") ")
  
  
  
  
  
  
  
  
  archivo_vista.close()
  archivo_controlador.close()










#vista 
btn_generar_carpertas = Button(text="generar carpetas",command = generar_carpeta_archivo_vista_y_controlador )

ventana.mainloop()
