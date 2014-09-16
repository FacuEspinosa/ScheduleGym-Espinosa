#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtCore, QtGui, Qt
from PyQt4.uic import *

class Myform(QtGui.QMainWindow):
    def __init__(self, parent=None):
        locale=unicode(QtCore.QLocale.system().name())
        QtGui.QWidget.__init__(self, parent)
        self.ui=loadUi("proyecto.ui",self)
        self.filename="alumnos.txt"

    def Seleccionar(self):
        f = self.getFile()
        alumnoCargado=self.ui.cbxalumnos.currentText()
        for line in f:
            datos = line.split(",")
            if datos[0]==alumnoCargado:
                self.ui.listalumnos.setText(datos[0])
                self.ui.listalumnos.setText(datos[1])
                self.ui.listalumnos.setText(datos[2])
                self.ui.listalumnos.setText(datos[3])
                self.ui.listalumnos.setTetx(datos[4])
                self.ui.lblResultados.setText("alumno Cargado")

    def buscar(self):
        f = self.getFile()
        alumnoCargado=self.ui.cbxalumnos.currentText()

    def Registrar(self):
        nombre = self.ui.txtnombre.text()
        dni = self.ui.txtdni.text()
        telefono = self.ui.txttel.text()
        clase = self.ui.cbxclases.currentText()
        cuotaA = self.ui.txtcuota.text()
        value="Nombre:"+nombre+", Dni:"+dni+", Telefono:"+telefono+", Clase:"+clase+",Cuota:"+cuota+"\n"
        f = open(self.filename, "a")
        f.write(value)
        f.close()
        self.ui.txtnombre.setText("")
        self.ui.txtdni.setText("")
        self.ui.txttel.setText("")
        self.ui.txtcuota.setText("")       
        self.ui.lblAviso.setText("Alumno Registrado Correctamente")

    def limpiar(self):
        self.ui.listalumnos.clear()

    def Guardar(self):
        clase = self.ui.txtclase.text()
        hinicio = self.ui.txthinicio.text()
        hfin = self.ui.txthfin.text()
        value=clase+","+hinicio+","+hfin+"\n"
        f = open(self.filename, "a")
        f.write(value)
        f.close()
        self.ui.txtclase.setText("")
        self.ui.txthinicio.setText("")
        self.ui.txthfin.setText("")
        self.ui.lblRTA.setText("Clase Guardada Correctamente")
        self.ui.cbxclases.addItem(self.ui.txtclase.text())
        self.ui.cbxclases2.addItem(self.ui.txtclase.text())

    def buscar2(self):
        f = self.getFile()
        claseCargada=self.ui.cbxclases2.currentText()

    def mostrarClases(self):
        f = self.getFile()
        claseCargada=self.ui.cbxclases2.currentText()
        for line in f:
            datos = line.split(",")
            if datos[0]==claseCargada:
                self.ui.listclase.addItem(datos[0])
                self.ui.listclase.addItem(datos[1])
                self.ui.listclase.addItem(datos[2])
                self.ui.lblRTA.setText("Clase Cargada")

    def limpiar2(self):
        self.ui.listclase.clear()

    def guardarProfesores(self):
        nombrep = self.ui.txtprofesor.text()
        dnip = self.ui.txtdnip.text()
        clasep = self.ui.cbxclases3.currentText()
        pago = self.ui.txtpago.text()
        value="Nombre"+nombrep+", Dni:"+dnip+", Clase:"+clasep+", Pago:"+pago+"\n"
        f = open(self.filename, "a")
        f.write(value)
        f.close()
        self.ui.txtprofesor.setText("")
        self.ui.txtdnip.setText("")
        self.ui.txtpago.setText("")
        self.ui.lblinfo.setText("El Profesor a sido registrado")

    def buscar3(self):
        f = self.getFile()
        profesorCargado=self.ui.cbxprofesores.currentText()

    def Mostrar(self):
        f = self.getFile()
        profesorCargado=self.ui.cbxprofesores.currentText()
        for line in f:
            datos = line.split(",")
            if datos[3]==profesorCargado:
                self.ui.listprofesores.setText(datos[0])
                self.ui.listprofesores.setText(datos[1])
                self.ui.listprofesores.setText(datos[2])
                self.ui.listprofesores.setText(datos[3])
                self.ui.lblinfo.setText("Profesor Cargado")

    def limpiar3(self):
        self.ui.listprofesores.clear()

    def getFile(self):
        try:
            f=open(self.filename, "r")
        except:
            f=open(self.filename, "w")
        return f

if __name__=="__main__":
    app=QtGui.QApplication(sys.argv)
    myapp = Myform()
    myapp.show()
    sys.exit(app.exec_())
