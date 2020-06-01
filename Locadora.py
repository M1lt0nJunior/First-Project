from tkinter import *
import tkinter.messagebox as tkMessageBox

import mysql.connector

db_connection = mysql.connector.connect(host="localhost", user="root", passwd="killer05", database="neo")
cursor = db_connection.cursor()

#este código monta um formulario
# o root abaixo é só uma varivel

#LeftMainFrame é uma variavel para um frame a esquerda ---sempre começar com Left
#os dados entre parentes se referem as propriedades do frame apresentado na tela

form = Tk()
form.title("Locadora de veículos")
form.geometry("1275x750+0+0")
form.configure(bg='green')

#Frames

#------------------------------------------------------------------------Frame principal da esquerda--------------------
LeftMainFrame = Frame(form,width=1000, height=950, bd=3, relief='raise')
LeftMainFrame.pack(side=LEFT)

#------------------------------------------------------------------------Frame principal da direita---------------------
RightMainFrame = Frame(form,width=250,height=850, bd=3, relief='raise')#raise quer dizer que ele é flexivel se aumentar a tela ele aumenta junto
RightMainFrame.pack(side=RIGHT)
#-----------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------Frame de titulo--------------------------------
LeftMainFrame0=Frame(LeftMainFrame,bg='yellow',width=1000,height=100,bd=1,relief='raise')
LeftMainFrame0.pack(side=TOP)
lblTitulo=Label(LeftMainFrame0,font=('arial',52,'bold'),bd=2,text=' Sistema Locadora de Veículos ',bg='lightgray')
lblTitulo.grid(row=0,column=0,sticky=W)
#-----------------------------------------------------------------------------------------------------------------------


#------------------------------------------------------------------------Frames secundarios da esquerda-----------------
InternalMainFrame = Frame(LeftMainFrame,width=1000,height=225,bd=3, relief='raise',bg='white')
InternalMainFrame.pack(side=TOP)
InternalMainFrame2 = Frame(LeftMainFrame,width=1000,height=225,bd=3,relief='raise',bg='moccasin')
InternalMainFrame2.pack(side=TOP)
InternalMainFrame3 = Frame(LeftMainFrame,width=1000,height=225,bd=3,relief='raise',bg='lightskyblue')
InternalMainFrame3.pack(side=TOP)
InternalMainFrame4 = Frame(LeftMainFrame,width=1000,height=225,bd=3,relief='raise')
InternalMainFrame4.pack(side=TOP)
#-----------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------Frames secundários da direita------------------
InternalMainFrameDireita = Frame(RightMainFrame,width=350,height=325,bg='lightskyblue',bd=3,relief='raise')
InternalMainFrameDireita.pack(side=TOP)
InternalMainFrameDireita2 = Frame(RightMainFrame,width=350,height=325,bg='lightskyblue',bd=3)
InternalMainFrameDireita2.pack(side=BOTTOM)
#-----------------------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------Campo do recibo Cx de Texto-------------------

txtRecibo = Text(InternalMainFrameDireita2,height = 10, width = 20, bd=8,bg='lemonchiffon', font=('arial',12,'bold')).grid(row=0, column=0)

#-----------------------------------------------------------------------------------------------------------------------

#botões do ultimo frame
#bg é o back groud do botão
#fg é a cor do texto no botão
#padx é a largura do botao
#width = largura
#height = altura

#------------------------------------------------------------------------Campo dos Botões do Rodapé---------------------

#------------Botão Sair
def iExit():
    form.destroy()
    exit()
#---------------------------------
def Limpar():
    txtCliente.delete(0,END)
    txtNome.delete(0,END)


#---------------------------------



cmdTotal = Button(InternalMainFrame4, text='Total', padx=83, bd=2,fg='yellow', bg='black',
                font=('arial',8,'bold'),width=12,height=3).grid(row=0,column=0)

cmdRecibo =   Button(InternalMainFrame4,text='Recibo',padx= 83, bd=2,fg='yellow', bg='black',
                font=('arial',8,'bold'),width=12,height=3).grid(row=0,column=1)

cmdLimpar =   Button(InternalMainFrame4,text='Limpar',command=Limpar,padx=83,bd=2,fg='yellow',bg='black',
                font=('arial',8,'bold'), width=12,height=3).grid(row=0,column=2)

cmdSair = Button(InternalMainFrame4,text='Sair',command=iExit, padx=83, bd=2,fg='yellow', bg='black',
                font=('arial',8,'bold'),width=12,height=3).grid(row=0,column=3)
#-----------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------Campo do frame Top(primeiro frame)-------------
lblCliente=Label(InternalMainFrame,font=('arial',11,'bold'), text='Cliente   :',bg='white', bd=8, justify='left')
lblCliente.grid(row=1,column=0,sticky=W)

txtCliente = Entry(InternalMainFrame,font=('arial',10,'bold'), bd=1, width=31, justify='left')
txtCliente.grid(row=1,column=1)


lblAlias=Label(InternalMainFrame,font=('arial',10,'bold'),text='Apelido :              ',bg='white', bd=8,justify='left')
lblAlias.grid(row=1,column=2,sticky=W)

txtDiasAlg = Entry(InternalMainFrame,font=('arial',10,'bold'), bd=1,width=31,justify='left')
txtDiasAlg.grid(row=1,column=3)

lblNome =Label(InternalMainFrame,font=('arial',11,'bold'),text='Nome:                  ',bg='white',bd=8,justify='left')
lblNome.grid(row=1,column=4,sticky=W)

txtNome = Entry(InternalMainFrame,font=('arial',10,'bold'),bd=1,width=31,justify='left')
txtNome.grid(row=1,column=5)

lblSnome=Label(InternalMainFrame, font=('arial',11,'bold'),text='S-Nome :',bg='white',bd=8,justify='left')
lblSnome.grid(row=2,column=0,sticky=W)
# sticky serve para tirar a margem

txtSnome=Entry(InternalMainFrame,font=('arial',10,'bold'),bd=1,width=31, justify='left')
txtSnome.grid(row=2,column=1,sticky=W)

lblEnd=Label(InternalMainFrame,font=('arial',11,'bold'),text = 'Endereço :',bg='white',bd=8,justify='left')
lblEnd.grid(row=2,column=2,sticky=W)

txtEnd=Entry(InternalMainFrame,font=('arial',10,'bold'),bd=1,width=31,justify='left')
txtEnd.grid(row=2,column=3)

lblArea=Label(InternalMainFrame,font=('arial',11,'bold'),text='Area :',bg='white',bd=8,justify='left')
lblArea.grid(row=2,column=4,sticky=W)

txtArea=Entry(InternalMainFrame,font=('arial',10,'bold'),bd=1,width=31,justify= 'left')
txtArea.grid(row=2,column=5)
#------------------------------------------------------------------------------------------------conjunto 2 top---------
lblCep=Label(InternalMainFrame, font=('arial',11,'bold'),text='Cod Postal :',bg='white',bd=8,justify='left')
lblCep.grid(row=3,column=0,sticky=W)
# sticky serve para tirar a margem

txtCep=Entry(InternalMainFrame,font=('arial',10,'bold'),bd=1,width=31, justify='left')
txtCep.grid(row=3,column=1,sticky=W)

lblCnh=Label(InternalMainFrame,font=('arial',11,'bold'),text = 'N-CNH :',bg='white',bd=8,justify='left')
lblCnh.grid(row=3,column=2,sticky=W)

txtCnh=Entry(InternalMainFrame,font=('arial',10,'bold'),bd=1,width=31,justify='left')
txtCnh.grid(row=3,column=3)

lblData=Label(InternalMainFrame,font=('arial',11,'bold'),text='Data :',bg='white',bd=8,justify='left')
lblData.grid(row=3,column=4,sticky=W)

txtData=Entry(InternalMainFrame,font=('arial',10,'bold'),bd=1,width=31,justify= 'left')
txtData.grid(row=3,column=5)
#------------------------------------------------------------------------------------------------conjunto 3 top---------
lblLocal=Label(InternalMainFrame,font=('arial',11,'bold'),text = 'Local :',bg='white',bd=8,justify='left')
lblLocal.grid(row=4,column=0,sticky=W)

txtLocal=Entry(InternalMainFrame,font=('arial',10,'bold'),bd=1,width=31,justify='left')
txtLocal.grid(row=4,column=1)

lblNdocCarro=Label(InternalMainFrame,font=('arial',11,'bold'),text='N-Doc-Carro :',bg='white',bd=8,justify='left')
lblNdocCarro.grid(row=4,column=2,sticky=W)

txtNdocCarro=Entry(InternalMainFrame,font=('arial',10,'bold'),bd=1,width=31,justify= 'left')
txtNdocCarro.grid(row=4,column=3)

lblTotalDias=Label(InternalMainFrame,font=('arial',11,'bold'),text='Total Dias :',bg='white',bd=8,justify='left')
lblTotalDias.grid(row=4,column=4,sticky=W)

txtTotalDias=Entry(InternalMainFrame,font=('arial',10,'bold'),bd=1,width=31,justify= 'left')
txtTotalDias.grid(row=4,column=5)

#-----------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------Campo do frame do meio(segundo frame)----------
lblTipoMotor=Label(InternalMainFrame2,font=('arial',11,'bold'), text='Tipo Motor :', bg='moccasin',bd=8, justify='left')
lblTipoMotor.grid(row=1,column=0,sticky=W)

txtTipoMotor = Entry(InternalMainFrame2,font=('arial',10,'bold'), bd=1, width=31, justify='left')
txtTipoMotor.grid(row=1,column=1)


lblEstilo=Label(InternalMainFrame2,font=('arial',11,'bold'),text='Estilo :             ',bg='moccasin', bd=8,justify='left')
lblEstilo.grid(row=1,column=2,sticky=W)

txtEstilo = Entry(InternalMainFrame2,font=('arial',10,'bold'), bd=1,width=31,justify='left')
txtEstilo.grid(row=1,column=3)

lblCarroAno =Label(InternalMainFrame2,font=('arial',11,'bold'),text='Carro-Ano :        ',bg='moccasin',bd=8,justify='left')
lblCarroAno.grid(row=1,column=4,sticky=W)

txtCarroAno = Entry(InternalMainFrame2,font=('arial',10,'bold'),bd=1,width=31,justify='left')
txtCarroAno.grid(row=1,column=5)

lblClasseCarro=Label(InternalMainFrame2,font=('arial',11,'bold'),text='Classe-Carro :',bg='moccasin',bd=8,justify='left')
lblClasseCarro.grid(row=2,column=0,sticky=W)

txtClasseCarro=Entry(InternalMainFrame2,font=('arial',10,'bold'),bd=1,width=31,justify= 'left')
txtClasseCarro.grid(row=2,column=1)


lblDescCarro=Label(InternalMainFrame2, font=('arial',11,'bold'),text='Desc-Carro :',bg='moccasin',bd=8,justify='left')
lblDescCarro.grid(row=2,column=2,sticky=W)
# sticky serve para tirar a margem

txtDescCarro=Entry(InternalMainFrame2,font=('arial',10,'bold'),bd=1,width=31, justify='left')
txtDescCarro.grid(row=2,column=3,sticky=W)


lblKmAnterior=Label(InternalMainFrame2,font=('arial',11,'bold'),text = 'Km-Anterior :',bg='moccasin',bd=8,justify='left')
lblKmAnterior.grid(row=2,column=4,sticky=W)

txtKmAnterior=Entry(InternalMainFrame2,font=('arial',10,'bold'),bd=1,width=31,justify='left')
txtKmAnterior.grid(row=2,column=5)

lblKmEntrega=Label(InternalMainFrame2,font=('arial',11,'bold'),text='Km-Entrega :',bg='moccasin',bd=8,justify='left')
lblKmEntrega.grid(row=3,column=0,sticky=W)

txtKmEntrega=Entry(InternalMainFrame2,font=('arial',10,'bold'),bd=1,width=31,justify= 'left')
txtKmEntrega.grid(row=3,column=1)
#------------------------------------------------------------------------------------------------conjunto 2-------------
lblFabCarro=Label(InternalMainFrame2, font=('arial',11,'bold'),text='Fab-Carro :',bg='moccasin',bd=8,justify='left')
lblFabCarro.grid(row=3,column=2,sticky=W)
# sticky serve para tirar a margem

txtFabCarro=Entry(InternalMainFrame2,font=('arial',10,'bold'),bd=1,width=31, justify='left')
txtFabCarro.grid(row=3,column=3,sticky=W)

lblModelo=Label(InternalMainFrame2,font=('arial',11,'bold'),text = 'Modelo :',bg='moccasin',bd=8,justify='left')
lblModelo.grid(row=3,column=4,sticky=W)

txtModelo=Entry(InternalMainFrame2,font=('arial',10,'bold'),bd=1,width=31,justify='left')
txtModelo.grid(row=3,column=5)

lblFabMotor=Label(InternalMainFrame2,font=('arial',11,'bold'),text='Fab-Motor :',bg='moccasin',bd=8,justify='left')
lblFabMotor.grid(row=4,column=0,sticky=W)

txtFabMotor=Entry(InternalMainFrame2,font=('arial',10,'bold'),bd=1,width=31,justify= 'left')
txtFabMotor.grid(row=4,column=1)
#------------------------------------------------------------------------------------------------conjunto 3-------------
lblCorCarro=Label(InternalMainFrame2,font=('arial',11,'bold'),text = 'Cor-Carro :',bg='moccasin',bd=8,justify='left')
lblCorCarro.grid(row=4,column=2,sticky=W)

txtCorCarro=Entry(InternalMainFrame2,font=('arial',10,'bold'),bd=1,width=31,justify='left')
txtCorCarro.grid(row=4,column=3)

lblSeguroCarro=Label(InternalMainFrame2,font=('arial',11,'bold'),text='Seguro-Carro :',bg='moccasin',bd=8,justify='left')
lblSeguroCarro.grid(row=4,column=4,sticky=W)

txtSeguroCarro=Entry(InternalMainFrame2,font=('arial',10,'bold'),bd=1,width=31,justify= 'left')
txtSeguroCarro.grid(row=4,column=5)

#-----------------------------------------------------------------------------------------------------------------------


#------------------------------------------------------------------------Campo do frame do Rodapé-----------------------
lblClienteID=Label(InternalMainFrame3,font=('arial',11,'bold'), text='Cliente ID :            ',bg='lightskyblue', bd=2, justify='left')
lblClienteID.grid(row=1,column=0,sticky=W)

txtClienteID = Entry(InternalMainFrame3,font=('arial',10,'bold'), bd=2, width=31, justify='left')
txtClienteID.grid(row=1,column=1)


lblDiasAlg=Label(InternalMainFrame3,font=('arial',11,'bold'),text='Dias locados :',bg='lightskyblue', bd=2,justify='left')
lblDiasAlg.grid(row=1,column=2,sticky=W)

txtDiasAlg = Entry(InternalMainFrame3,font=('arial',10,'bold'), bd=2,width=31,justify='left')
txtDiasAlg.grid(row=1,column=3)

lblDesc =Label(InternalMainFrame3,font=('arial',11,'bold'),text='Desconto :           ',bg='lightskyblue',bd=2,justify='left')
lblDesc.grid(row=1,column=4,sticky=W)

txtDesc = Entry(InternalMainFrame3,font=('arial',10,'bold'),bd=2,width=31,justify='left')
txtDesc.grid(row=1,column=5)

lblDiasTotal=Label(InternalMainFrame3, font=('arial',11,'bold'),text='Total de dias :',bg='lightskyblue',bd=2,justify='left')
lblDiasTotal.grid(row=2,column=0,sticky=W)
# sticky serve para tirar a margem

txtDiasTotal=Entry(InternalMainFrame3,font=('arial',10,'bold'),bd=2,width=31, justify='left')
txtDiasTotal.grid(row=2,column=1,sticky=W)

lblIdFatura=Label(InternalMainFrame3,font=('arial',11,'bold'),text = 'Fatura ID :',bg='lightskyblue',bd=2,justify='left')
lblIdFatura.grid(row=2,column=2,sticky=W)

txtIdFatura=Entry(InternalMainFrame3,font=('arial',10,'bold'),text='(   )____-____',bd=2,width=31,justify='left')
txtIdFatura.grid(row=2,column=3)

lblTotal=Label(InternalMainFrame3,font=('arial',11,'bold'),text='Total :',bg='lightskyblue',bd=2,justify='left')
lblTotal.grid(row=2,column=4,sticky=W)

txtTotal=Entry(InternalMainFrame3,font=('arial',10,'bold'),bd=2,width=31,justify= 'left')
txtTotal.grid(row=2,column=5)

#-----------------------------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------Campos do frame da direita TOP--------------------
style=Checkbutton(InternalMainFrameDireita,text='Estilo \t\t\t',onvalue=1,offvalue=0,bg='lightskyblue',font=('arial',14,'bold')).grid(row=0,sticky=W)
style=Checkbutton(InternalMainFrameDireita,text='Classe ID \t\t',onvalue=1,offvalue=0,bg='lightskyblue',font=('arial',15,'bold')).grid(row=1,sticky=W)
style=Checkbutton(InternalMainFrameDireita,text='Fatura ID \t\t',onvalue=1,offvalue=0,bg='lightskyblue',font=('arial',14,'bold')).grid(row=2,sticky=W)
style=Checkbutton(InternalMainFrameDireita,text='Diária \t\t\t',onvalue=1,offvalue=0,bg='lightskyblue',font=('arial',15,'bold')).grid(row=3,sticky=W)
style=Checkbutton(InternalMainFrameDireita, text='Automático \t\t',onvalue=1,offvalue=0,bg='lightskyblue',font=('arial',15,'bold')).grid(row=4,sticky=W)
style=Checkbutton(InternalMainFrameDireita,text='Ar Condicionado \t\t',onvalue=1,offvalue=0,bg='lightskyblue',font=('arial',14,'bold')).grid(row=5,sticky=W)
style=Checkbutton(InternalMainFrameDireita,text='Seguro Incluso \t\t',onvalue=1,offvalue=0,bg='lightskyblue',font=('arial',15,'bold')).grid(row=6,sticky=W)
style=Checkbutton(InternalMainFrameDireita,text='Detalhe Cliente \t\t',onvalue=1,offvalue=0,bg='lightskyblue',font=('arial',14,'bold')).grid(row=8,sticky=W)



#------campos de dados

def Limpar(): e.delete(txtIdFatura)

#-------------------------------




form.mainloop()
