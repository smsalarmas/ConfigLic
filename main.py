#!/usr/bin/env python
# -*- coding: latin-1 -*-

from PyQt4 import QtGui, QtCore
from QTMainConfig import Ui_WizardConfig
from socket import gethostname

import datetime
from Crypto.Cipher import XOR
from base64 import b64encode, b64decode
import uuid
from ConfigParser import ConfigParser

class MainClass(QtGui.QWizard):
	def __init__(self):
		QtGui.QWizard.__init__(self)
		self.MainWindow = Ui_WizardConfig()
		self.MainWindow.setupUi(self)
		self.setWindowTitle('365Config 1.1')

		self.NombreEquipo = 'mc24.no-ip.net' #str(gethostname())
		self.UsuarioBD = 'sa'
		self.ContrasenaBD = 'jerm'
		
		self.connect(self.MainWindow.Clear, QtCore.SIGNAL("clicked()"), self.BorrarCampos)

		self.connect(self.MainWindow.pushButton_GenerarConfig, QtCore.SIGNAL("clicked()"), self.Generar)

		#self.connect(self.QNuevoMensaje.buttonBox, QtCore.SIGNAL("accepted()"),self.EnviarSMS)


	def BorrarCampos(self):
		self.MainWindow.p1.clear()
		self.MainWindow.p2.clear()
	def Generar(self):
                # aqui va el password
		if 1==1:
			if self.MainWindow.radioButton_Server.isChecked():
				if self.MainWindow.radioButton_Local.isChecked():
					pass
				else:
					self.NombreEquipo = self.MainWindow.lineEdit_DireccionBD.text()
				if self.MainWindow.lineEdit_UsuarioBD.text() != '':
					self.UsuarioBD = self.MainWindow.lineEdit_UsuarioBD.text()
				if self.MainWindow.lineEdit_ClaveBD.text() != '':
					self.ContrasenaBD = self.MainWindow.lineEdit_ClaveBD.text()

				StringBD = 'Driver={SQL Server Native Client 11.0};Server=NOMBREPC;Database=365DB;Uid=USUARIOBD;Pwd=PASSWORDBD'
				StringBD = StringBD.replace('USUARIOBD',str(self.UsuarioBD))
				StringBD = StringBD.replace('PASSWORDBD',str(self.ContrasenaBD))
				StringBD = StringBD.replace('NOMBREPC',str(self.NombreEquipo))
				
				self.LongitudPermitida = self.MainWindow.lineEdit_SMSLongitud.text()
				self.PrefijosPermitidos = self.MainWindow.lineEdit_PrefijosSMS.text()
				self.PrefijosPermitidos = self.LongitudPermitida+','+self.PrefijosPermitidos

				self.PruebaSMS = self.MainWindow.lineEdit_PruebaRSMS.text()
				
				self.DirSMTP = self.MainWindow.lineEdit_DireccionSMTP.text()
				self.PuertoSMTP = self.MainWindow.lineEdit_PuertoSMTP.text()
				self.UsuarioSMTP = self.MainWindow.lineEdit_UsuarioCorreo.text()
				self.ContrasenaSMTP = self.MainWindow.lineEdit_ClaveCorreo.text()

				self.ServerWeb = self.MainWindow.lineEdit_ServerWeb.text()



				ps = b64encode(str(self.MainWindow.p1.text()))
				deco = XOR.new(b64decode(ps))
				StringBD =  b64encode(deco.encrypt(str(StringBD)))
				deco = XOR.new(b64decode(ps))
				lic =  b64encode(deco.encrypt(':'.join(['{:02x}'.format((uuid.getnode() >> i) & 0xff) for i in range(0,8*6,8)][::-1])))
				deco = XOR.new(b64decode(ps))
				cualmodo =  b64encode(deco.encrypt('1'))
				if self.PrefijosPermitidos:
					deco = XOR.new(b64decode(ps))
					numerosvalidos =  b64encode(deco.encrypt(str(self.PrefijosPermitidos)))
				else:
					numerosvalidos = ''
				if self.LongitudPermitida:
					deco = XOR.new(b64decode(ps))
					lennums =  b64encode(deco.encrypt(str(self.LongitudPermitida)))
				else:
					lennums = ''
				if self.PruebaSMS:
					deco = XOR.new(b64decode(ps))
					numpruebarapida =  b64encode(deco.encrypt(str(self.PruebaSMS)))
				else:
					numpruebarapida = ''
				if self.ServerWeb:
					deco = XOR.new(b64decode(ps))
					direccionweb =  b64encode(deco.encrypt(str(self.ServerWeb)))
				else:
					direccionweb = ''
				if self.DirSMTP:
					deco = XOR.new(b64decode(ps))
					dirsmtp =  b64encode(deco.encrypt(str(self.DirSMTP)))
				else:
					dirsmtp = ''
				if self.PuertoSMTP:
					deco = XOR.new(b64decode(ps))
					puertosmtp =  b64encode(deco.encrypt(str(self.PuertoSMTP)))
				else:
					puertosmtp = ''
				if self.UsuarioSMTP:
					deco = XOR.new(b64decode(ps))
					usuariosmtp =  b64encode(deco.encrypt(str(self.UsuarioSMTP)))
				else:
					usuariosmtp = ''
				if self.ContrasenaSMTP:
					deco = XOR.new(b64decode(ps))
					clavesmtp =  b64encode(deco.encrypt(str(self.ContrasenaSMTP)))
				else:
					clavesmtp = ''

				deco = XOR.new(b64decode(ps))
				conexionvalidlic = b64encode(deco.encrypt(str('Driver={SQL Server Native Client 11.0};Server=mc24.no-ip.net;Database=365License;Uid=sa;Pwd=jerm')))

				deco = XOR.new(b64decode(ps))
				fecha = datetime.datetime.now()
				fecha = b64encode(deco.encrypt(str(fecha.year)+','+str(fecha.month)+','+str(fecha.day)+','+str(fecha.hour)+','+str(fecha.minute)+','+str(fecha.second)))

				self.Tipo = '1' #Si es server 1 si es cliente 2
				deco = XOR.new(b64decode(ps))
				tipo = b64encode(deco.encrypt(str(self.Tipo)))
				
				self.CrearArchivo(StringBD,lic,cualmodo,tipo,numerosvalidos,numpruebarapida,direccionweb,dirsmtp,puertosmtp,usuariosmtp,clavesmtp,conexionvalidlic,fecha)

			else:
				if self.MainWindow.radioButton_Local.isChecked():
					pass
				else:
					self.NombreEquipo = self.MainWindow.lineEdit_DireccionBD.text()
				if self.MainWindow.lineEdit_UsuarioBD.text() != '':
					self.UsuarioBD = self.MainWindow.lineEdit_UsuarioBD.text()
				if self.MainWindow.lineEdit_ClaveBD.text() != '':
					self.ContrasenaBD = self.MainWindow.lineEdit_ClaveBD.text()

				StringBD = 'Driver={SQL Server Native Client 11.0};Server=NOMBREPC;Database=365DB;Uid=USUARIOBD;Pwd=PASSWORDBD'
				StringBD = StringBD.replace('USUARIOBD',str(self.UsuarioBD))
				StringBD = StringBD.replace('PASSWORDBD',str(self.ContrasenaBD))
				StringBD = StringBD.replace('NOMBREPC',str(self.NombreEquipo))
				
				self.LongitudPermitida = self.MainWindow.lineEdit_SMSLongitud.text()
				self.PrefijosPermitidos = self.MainWindow.lineEdit_PrefijosSMS.text()
				self.PrefijosPermitidos = self.LongitudPermitida+','+self.PrefijosPermitidos

				self.PruebaSMS = self.MainWindow.lineEdit_PruebaRSMS.text()
				
				self.DirSMTP = self.MainWindow.lineEdit_DireccionSMTP.text()
				self.PuertoSMTP = self.MainWindow.lineEdit_PuertoSMTP.text()
				self.UsuarioSMTP = self.MainWindow.lineEdit_UsuarioCorreo.text()
				self.ContrasenaSMTP = self.MainWindow.lineEdit_ClaveCorreo.text()

				self.ServerWeb = self.MainWindow.lineEdit_ServerWeb.text()



				ps = b64encode(str(self.MainWindow.p1.text()))
				deco = XOR.new(b64decode(ps))
				StringBD =  b64encode(deco.encrypt(str(StringBD)))
				deco = XOR.new(b64decode(ps))
				lic =  b64encode(deco.encrypt(':'.join(['{:02x}'.format((uuid.getnode() >> i) & 0xff) for i in range(0,8*6,8)][::-1])))
				deco = XOR.new(b64decode(ps))
				cualmodo =  b64encode(deco.encrypt('1'))
				if self.PrefijosPermitidos:
					deco = XOR.new(b64decode(ps))
					numerosvalidos =  b64encode(deco.encrypt(str(self.PrefijosPermitidos)))
				else:
					numerosvalidos = ''
				if self.LongitudPermitida:
					deco = XOR.new(b64decode(ps))
					lennums =  b64encode(deco.encrypt(str(self.LongitudPermitida)))
				else:
					lennums = ''
				if self.PruebaSMS:
					deco = XOR.new(b64decode(ps))
					numpruebarapida =  b64encode(deco.encrypt(str(self.PruebaSMS)))
				else:
					numpruebarapida = ''
				if self.ServerWeb:
					deco = XOR.new(b64decode(ps))
					direccionweb =  b64encode(deco.encrypt(str(self.ServerWeb)))
				else:
					direccionweb = ''
				if self.DirSMTP:
					deco = XOR.new(b64decode(ps))
					dirsmtp =  b64encode(deco.encrypt(str(self.DirSMTP)))
				else:
					dirsmtp = ''
				if self.PuertoSMTP:
					deco = XOR.new(b64decode(ps))
					puertosmtp =  b64encode(deco.encrypt(str(self.PuertoSMTP)))
				else:
					puertosmtp = ''
				if self.UsuarioSMTP:
					deco = XOR.new(b64decode(ps))
					usuariosmtp =  b64encode(deco.encrypt(str(self.UsuarioSMTP)))
				else:
					usuariosmtp = ''
				if self.ContrasenaSMTP:
					deco = XOR.new(b64decode(ps))
					clavesmtp =  b64encode(deco.encrypt(str(self.ContrasenaSMTP)))
				else:
					clavesmtp = ''

				deco = XOR.new(b64decode(ps))
				conexionvalidlic = b64encode(deco.encrypt(str('Driver={SQL Server Native Client 11.0};Server=mc24.no-ip.net;Database=365License;Uid=sa;Pwd=jerm')))

				deco = XOR.new(b64decode(ps))
				fecha = datetime.datetime.now()
				fecha = b64encode(deco.encrypt(str(fecha.year)+','+str(fecha.month)+','+str(fecha.day)+','+str(fecha.hour)+','+str(fecha.minute)+','+str(fecha.second)))

				self.Tipo = '2' #Si es server 1 si es cliente 2
				deco = XOR.new(b64decode(ps))
				tipo = b64encode(deco.encrypt(str(self.Tipo)))
				
				self.CrearArchivo(StringBD,lic,cualmodo,tipo,numerosvalidos,numpruebarapida,direccionweb,dirsmtp,puertosmtp,usuariosmtp,clavesmtp,conexionvalidlic,fecha)
		else:
			pass
	def CrearArchivo(self,stringbd,lic,cualmodo,tipo,numerosvalidos,numpruebarapida,direccionweb,dirsmtp,puertosmtp,usuariosmtp,clavesmtp,conexionvalidlic,fecha):
			print 'Creando Archivo'
			cfgfile = open("config.ini",'w')
			Config = ConfigParser()
			Config.add_section('BASE DE DATOS')
			Config.set('BASE DE DATOS','Conexion',stringbd)
			Config.add_section('CUENTA')
			Config.set('CUENTA','Lic',lic)
			Config.set('CUENTA','Modo',cualmodo)
			Config.set('CUENTA','Tipo',tipo)
			Config.add_section('MODEMS')
			Config.set('MODEMS','formatos',numerosvalidos)
			Config.set('MODEMS','nums',numpruebarapida)
			Config.add_section('WEB')
			Config.set('WEB','srv',direccionweb)

			Config.add_section('SMTP')
			Config.set('SMTP','smtp',dirsmtp)
			Config.set('SMTP','port',puertosmtp)
			Config.set('SMTP','login',usuariosmtp)
			Config.set('SMTP','password',clavesmtp)

			Config.add_section('REMOTE')
			Config.set('REMOTE','conexion',conexionvalidlic)
			Config.set('REMOTE','date',fecha)

			Config.write(cfgfile)
			print 'Archivo Creado'
			cfgfile.close()

if __name__ == "__main__":
	import sys
	app = QtGui.QApplication(sys.argv)
	app.setStyle(QtGui.QStyleFactory.create("plastique"))
	window = MainClass()
	window.show()
	app.exec_()

