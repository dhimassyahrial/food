#!/usr/bin/env python
# -*- coding: utf-8 -*-


import telebot
import time
# import sys
# import re
import os
import logging

# import mysql.connector
# import subprocess
# import requests
import datetime
import traceback


from telebot import types


BOTNAME = "LKPP BOT"
TOKEN_BOT = '1133464808:AAEkCUyYg14u-cUQ_6jZgqcID7_GYyX1b9E' #dhimas_test_bot
# TOKEN_BOT = '2026061059:AAHO1FlpstfPbanEGbF0CwiDF66NXyJXxBY' #protokol bot


bot = telebot.TeleBot(TOKEN_BOT)
groupID = -718209669 #LKPP Dco



# @bot.message_handler(commands=['start'])
# def action_start(message):
# 	user = open('user.txt','r')
# 	user = user.read()
# 	id_message = message.chat.id
# 	if str(id_message) in user:
# 		text = f" Hi Kak *{message.chat.first_name}* Ketik /input untuk memulai"
# 		bot.send_message(message.chat.id,text, parse_mode="Markdown")

# 	else:
# 		text = f" Mohon Maaf , kakak belum terdaftar. Silahkan hubungi 085292551702."
# 		bot.send_message(message.chat.id,text, parse_mode="Markdown")


@bot.message_handler(commands=['cek'])
def action_cek(message):
	print(message)
	text = "Nomer id kamu adalah: "
	text += str(message.from_user.id)
	bot.send_message(message.chat.id,text)


@bot.message_handler(commands=['in'])
def action_in(message):
    user_ceo = open('user-ceo.txt','r')
    user_ceo = user_ceo.read()
    if str(message.from_user.id) in user_ceo:
        text = message.text.split()
        with open('user.txt', 'a') as user:
            user.writelines(f"\n{text[1]}")
            text = f"Berhasil ditambahkan bossku"
            bot.send_message(message.chat.id,text, parse_mode="Markdown")
    else:
        text = f"Maaf kurang tepat boss"
        bot.send_message(message.chat.id,text, parse_mode="Markdown")

@bot.message_handler(commands=['admin'])
def action_in(message):
    user_ceo = open('user-ceo.txt','r')
    user_ceo = user_ceo.read()
    if str(message.from_user.id) in user_ceo:
        text = message.text.split()
        with open('user-ceo.txt', 'a') as user:
            user.writelines(f"\n{text[1]}")
            text = f"Berhasil ditambahkan bossku"
            bot.send_message(message.chat.id,text, parse_mode="Markdown")
    else:
        text = f"Maaf kurang tepat boss"
        bot.send_message(message.chat.id,text, parse_mode="Markdown")

user_dict = {}

class User:
	def __init__(self, name):
		self.name = name
		self.idUser = None
		self.namaUser = None
		self.nohpUser = None
		self.chat_idUser = None
		self.section = None
		self.category = None
		self.activity = None
		self.detailAct = None
		self.siteid = None
		self.sitelokasi = None
		self.pic = None
		self.tanggalmulai = None
		self.pukulmulai = None
		self.tanggalselesai = None
		self.pukulselesai = None
		self.status = None
		self.needsup = None
		self.keterangan = None
		self.longitude = None
		self.latitude = None
		self.userState = 0
		self.current_shown_dates = None
userDef = User(" ")


class Daftar:
    def __init__(self, name):
        self.nama = name
        self.nohp = None
        self.posisi = None
        self.fname = None
        self.chatid = None

daftar_dict = {}

def processPhoto(message):
    # print ('message.photo =', message.photo)
    fileID = message.photo[-1].file_id
    # print ('fileID =', fileID)
    file = bot.get_file(fileID)
    # print ('file.file_path =', file.file_path)
    # bot.send_photo(message.chat.id, fileID)
    bot.send_photo(groupID, fileID)
    fname = message.from_user.first_name
    text = f"Photo from Kak {fname}"
    bot.send_message(groupID, text)
    bot.send_message(message.from_user.id, 'Thankyou Kak', parse_mode="Markdown")

def processDoc(message):
    # print ('message.document =', message.document)
    # print(message)
    fileID = message.document.file_id
    # print ('fileID =', fileID)
    file = bot.get_file(fileID)
    # print ('file.file_path =', file.file_path)
    # bot.send_photo(message.chat.id, fileID)
    bot.send_document(groupID, fileID)
    fname = message.from_user.first_name
    text = f"Document from Kak {fname}"
    bot.send_message(groupID, text)
    bot.send_message(message.from_user.id, 'Thankyou Kak', parse_mode="Markdown")


@bot.message_handler(content_types=['photo'])
def photo(message):
    processPhoto(message)

@bot.message_handler(content_types=['document'])
def photo(message):
    processDoc(message)

class CommandHandler:
	def stepSatu(self, message, section):
		fname = message.from_user.first_name
		print(f'{fname} report Satu')
		chat_id = str(message.from_user.id)
		user = User(section)
		user_dict[chat_id] = user
		user.section = section
		text = f"Mengundang Kepala LKPP"
		bot.edit_message_text(chat_id=chat_id, message_id=message.message.message_id, text = text)
		text = f''' Sebelum mengundang Kepala LKPP di acara resmi/acara kenegaraan, pastikan kamu udah bernodin ke BHSIU terkait permohonan sarana prasarana, booking tempat pelaksanaan, jamuan ataupun layanan keprotokolan. Kalau udah dilakukan, Acara dilakukan dimana? '''
		lokasi = ['Kantor LKPP', 'Luar Kantor LKPP']

		if len(lokasi) > 0:
			markup = types.InlineKeyboardMarkup()
			for row in lokasi:
				markup.row(types.InlineKeyboardButton(f"{row}",callback_data=f"LOKASI {row}"))
			bot.send_message(chat_id, text, reply_markup=markup, parse_mode="MARKDOWN")

	def stepSatuKoordinasi(self, message, section):
		fname = message.from_user.first_name
		print(f'{fname} report Koordinasi Tata Upacara')
		chat_id = str(message.from_user.id)
		user = User(section)
		user_dict[chat_id] = user
		user.section = section
		text = f"{section}"
		bot.edit_message_text(chat_id=chat_id, message_id=message.message.message_id, text = text)
		text = f'''Sebelum melaksanakan upacara pembukaan/peresmian/pelantikan dsb, pastikan kamu telah bernodin ke BHSIU terkait permohonan sarana prasarana, booking tempat pelaksanaan, jamuan ataupun layanan keprotokolan. Jika sudah, pilih kategori Upacara berikut:
		'''
		upacara = ['Upacara Pembukaan/Peresmian', 'Upacara Pelantikan']

		if len(upacara) > 0:
			markup = types.InlineKeyboardMarkup()
			for row in upacara:
				markup.row(types.InlineKeyboardButton(f"{row}",callback_data=f"UPACARA {row}"))
			bot.send_message(chat_id, text, reply_markup=markup, parse_mode="MARKDOWN")

	def stepSatuTata(self, message, section):
		fname = message.from_user.first_name
		print(f'{fname} report Koordinasi Tata Penerimaan VIP/VVIP')
		chat_id = str(message.from_user.id)
		user = User(section)
		user_dict[chat_id] = user
		user.section = section
		text = f"{section}"
		bot.edit_message_text(chat_id=chat_id, message_id=message.message.message_id, text = text)
		text = f'''Sebelum melakukan koordinasi terkait tata penghormatan/penerimaan tamu VIP/VVIP, pastikan kamu telah bernodin ke BHSIU terkait permohonan sarana prasarana, booking tempat pelaksanaan, jamuan ataupun layanan keprotokolan. Pilih kategori Tamu berikut:
		'''
		tamu = ['Presiden/Wakil Presiden', 'Menteri/setingkat Menteri', 'Kepala Daerah (Gubernur/WakilGubernur/Bupati/Walikota)', 'Lainnya']

		if len(tamu) > 0:
			markup = types.InlineKeyboardMarkup()
			for row in tamu:
				markup.row(types.InlineKeyboardButton(f"{row}",callback_data=f"TAMU {row}"))
			bot.send_message(chat_id, text, reply_markup=markup, parse_mode="MARKDOWN")

	def stepTamu(self, message, section):
		fname = message.from_user.first_name
		print(f'{fname} report Tamu')
		chat_id = str(message.from_user.id)
		user = User(section)
		user_dict[chat_id] = user
		user.section = section
		text = f"Mengundang {section}"
		bot.edit_message_text(chat_id=chat_id, message_id=message.message.message_id, text = text)
		print(section)
		if section == 'Presiden/Wakil Presiden':
			msg = f"Kalau tamu yang hadir adalah Presiden/Wakil Presiden, silahkan langsung berkoordinasi dengan tim Protokol."
		elif section == 'Menteri/setingkat Menteri':
			msg = f"Kalau tamu yang hadir adalah Menteri/Setingkat Menteri, maka kalian harus mengagendakan pejabat pimpinan tinggi untuk melakukan penyambutan di tempat kedatangan tamu. Jangan lupa siapkan ruang transit VIP."
		elif section == 'Kepala Daerah (Gubernur/WakilGubernur/Bupati/Walikota)':
			msg = f"Kalau tamu yang hadir adalah Kepala Daerah, maka kalian harus mengagendakan pejabat pimpinan tinggi untuk mendampingi Kepala LKPP atau menerima tamu tadi"
		elif section == 'Lainnya':
			msg = f"Kalau tamu yang hadir selain kategori tersebut, segera koordinasikan dengan Unit Organinasi kamu ya."
		bot.send_message(chat_id, msg, parse_mode="Markdown")
		self.closing(message,'close')


	def stepSatuSatu(self, message, section):
		fname = message.from_user.first_name
		print(f'{fname} report Satu')
		chat_id = str(message.from_user.id)
		user = User(section)
		user_dict[chat_id] = user
		user.section = section
		text = f"Kunjungan Tamu Penting"
		bot.edit_message_text(chat_id=chat_id, message_id=message.message.message_id, text = text)




	def stepTiga(self, message, section):
		fname = message.from_user.first_name
		print(f'{fname} report Tiga')
		chat_id = str(message.from_user.id)
		user = User(section)
		user_dict[chat_id] = user
		user.section = section
		text = f"Acaranya di {section}"
		bot.edit_message_text(chat_id=chat_id, message_id=message.message.message_id, text = text)
		print(section)
		if section == 'Kantor LKPP':
			msg = f"Sob, kamu udah mempersiapkan ruangan dan sarana prasarana pada kegiatan di kantor? Next, kamu bisa bikin rundown/naskah MC kegiatan sesuai pedoman kita. Pedomannya bisa kamu lihat pada infografis di link yang tertera. Tim kamu juga bisa bikin bahan paparan atau pointer untuk Kepala LKPP dengan menggunakan format yang sudah kami sediakan pada link : *bit.ly/TemplatePaparanKepalaLKPP* 😊"
			bot.send_message(chat_id, msg, parse_mode="Markdown")
			# msg2 = f"Kirimin undangan sama rundown nya disini ya"
			# bot.send_message(chat_id, msg2, parse_mode="Markdown")
		elif section == 'Luar Kantor LKPP':
			msg = f'''Sob, kamu udah mempersiapkan lokasi kegiatan di luar kantor? Next, kamu bisa bikin rundown/naskah MC kegiatan. Pedomannya bisa kamu lihat pada infografis di bawah. Tim kamu juga bisa bikin bahan paparan atau pointer untuk Kepala LKPP dengan menggunakan format yang sudah kami sediakan pada link : *bit.ly/TemplatePaparanKepalaLKPP* \nKamu harus berkoordinasi secara langsung dengan tim Protokol dan juga Sekretaris Pimpinan. Informasikan lokasi pelaksanaan dan juga waktu pelaksanaan dengan detail. Jangan lupa, koordinasikan persiapan undangan dan  juga akomodasi selama kegiatan dilaksanakan. Semangat! 😊'''
			bot.send_message(chat_id, msg, parse_mode="Markdown")
		self.closing(message,'close')
		

	def stepUpacara(self, message, section):
		fname = message.from_user.first_name
		print(f'{fname} report Tiga')
		chat_id = str(message.from_user.id)
		user = User(section)
		user_dict[chat_id] = user
		user.section = section
		text = f"{section}"
		bot.edit_message_text(chat_id=chat_id, message_id=message.message.message_id, text = text)
		print(section)
		if section == 'Upacara Pembukaan/Peresmian':
			msg = f"Sebelum menyelenggarakan upacara pembukaan/peresmian/dsb, silakan susun rundown/naskah MC menggunakan pedoman di bawah ini. Ada beberapa simbolis pada upacara pembukaan kegiatan/peresmian, seperti memukul gong, menekan sirine, mengetuk palu, memotong pita dan lain lain. Silakan pilih yang paling sesuai dengan acaramu. Selain itu, tentukan tamu undangan yang akan hadir, informasikan secara update apabila ada perubahan jadwal maupun tamu VIP yang akan hadir kepada tim Protokol yaa.. Semangat! 😊"
			bot.send_message(chat_id, msg, parse_mode="Markdown")
			# msg2 = f"Kirimin undangan sama rundown nya disini ya"
			# bot.send_message(chat_id, msg2, parse_mode="Markdown")
		elif section == 'Upacara Pelantikan':
			msg = f'''Sebelum menyelenggarakan upacara pelantikan, pastikan kamu telah mempersiapkan beberapa dokumen pelantikan seperti : naskah sumpah jabatan, naskah pelantikan, dokumen pakta integritas, dokumen berita acara dan juga ballpoint untuk penandatanganan. Silakan berkoordinasi lebih lanjut kepada tim Protokol terkait layout tempat upacara pelantikan agar sesuai dengan peraturan perundang undangan. 😊'''
			bot.send_message(chat_id, msg, parse_mode="Markdown")
		self.closing(message,'close')
		

	def closing(self, message, section):
		fname = message.from_user.first_name
		print(f'{fname} report Satu')
		chat_id = str(message.from_user.id)
		user = User(section)
		user_dict[chat_id] = user
		user.section = section
		pilihan = ['Kembali ke Menu Utama', 'Selesai']
		text = "Silahkan tentukan pilihan kamu Sob"
		if len(pilihan) > 0:
			markup = types.InlineKeyboardMarkup()
			for row in pilihan:
				markup.row(types.InlineKeyboardButton(f"{row}",callback_data=f"CLOSING {row}"))
			bot.send_message(chat_id, text, reply_markup=markup, parse_mode="MARKDOWN")
		

	def initial(self, message, section):
		fname = message.from_user.first_name
		print(f'{fname} closing')
		chat_id = str(message.from_user.id)
		self.clearData(chat_id)
		user = User(section)
		user_dict[chat_id] = user
		user.section = section
		text = "😊"
		bot.edit_message_text(chat_id=chat_id, message_id=message.message.message_id, text = text)
		if True:
			print(f'{fname} INPUT')
			text = f''' Hi kak *{fname}* Sobat Kredibel, pesan ini dijawab oleh Bot Protokol. Ada yang bisa kami bantu?  Kamu bisa memilih:
			- Mengundang *Kepala LKPP* di acara resmi/acara kenegaraan
			- Koordinasi terkait *Tata Upacara*
			- Koordinasi terkait *Tata Penghormatan/Penerimaan Tamu VIP/VVIP*'''
			# bot.send_message(message.chat.id, text, parse_mode="Markdown")
			result = ['Mengundang Kepala LKPP', 'Koordinasi Tata Upacara', 'Tata Penghormatan/Penerimaan Tamu']
			markup = types.InlineKeyboardMarkup()
			for row in result:
				print(row)
				markup.row(types.InlineKeyboardButton(f"{row}",callback_data=f"SEC {row}" ))
			bot.send_message(message.from_user.id, text, reply_markup=markup, parse_mode="MARKDOWN")
		else :
			text = f"Mohon Maaf , kakak belum terdaftar, Silahkan hubungi 085292551702"
			bot.send_message(message.from_user.id,text, parse_mode="Markdown")
		

	def thanks(self, message, section):
		fname = message.from_user.first_name
		print(f'{fname} report thanks')
		chat_id = str(message.from_user.id)
		user = User(section)
		user_dict[chat_id] = user
		user.section = section
		text = 'Makasih ya udah mau ngobrol sama Protokol Bot. Semoga acaramu sukses, Sob. Semangat!!'
		bot.edit_message_text(chat_id=chat_id, message_id=message.message.message_id, text = text)
		text = "😊"
		bot.send_message(chat_id, text, parse_mode="MARKDOWN")
		self.clearData(chat_id)

	def clearData(self, chat_id):
		user = user_dict[chat_id]
		user.idUser = None
		user.namaUser = None
		user.nohpUser = None
		user.chat_idUser = None
		user.section = None
		user.category = None
		user.activity = None
		user.detailAct = None
		user.siteid = None
		user.sitelokasi = None
		user.pic = None
		user.tanggalmulai = None
		user.tanggalselesai = None
		user.status = None
		user.needsup = None
		user.keterangan = None
		user.userState = 0
		user.current_shown_dates = None

cmdHandler = CommandHandler()


@bot.message_handler(commands=['help'])
def action_help(message):
    cmdHandler.userlog(message,'help')
    bot.send_message(message.chat.id, "❇️ /start - untuk memulai\n\n"
                                      "🔰 /input - input komplain\n\n"
                                      )

@bot.message_handler(commands=['input', 'start'])
def handle_start(message):
	# user = open('user.txt','r')
	# user = user.read()
	fname = message.from_user.first_name
	if message.chat.type == "private":
		# if str(message.from_user.id) in user:
		if True:
			print(f'{fname} INPUT')
			text = f''' Hi kak *{fname}* Sobat Kredibel, pesan ini dijawab oleh Bot Protokol. Ada yang bisa kami bantu?  Kamu bisa memilih:
			- Mengundang *Kepala LKPP* di acara resmi/acara kenegaraan
			- Koordinasi terkait *Tata Upacara*
			- Koordinasi terkait *Tata Penghormatan/Penerimaan Tamu VIP/VVIP*'''
			# bot.send_message(message.chat.id, text, parse_mode="Markdown")

			result = ['Mengundang Kepala LKPP', 'Koordinasi Tata Upacara', 'Tata Penghormatan/Penerimaan Tamu']
			markup = types.InlineKeyboardMarkup()
			for row in result:
				print(row)
				markup.row(types.InlineKeyboardButton(f"{row}",callback_data=f"SEC {row}" ))
			bot.send_message(message.chat.id, text, reply_markup=markup, parse_mode="MARKDOWN")
		else :
			text = f"Mohon Maaf , kakak belum terdaftar, Silahkan hubungi 085292551702"
			bot.send_message(message.chat.id,text, parse_mode="Markdown")
	else:
		text = f"Mohon Maaf , hanya bisa di akses melalui private chat"
		bot.send_message(message.chat.id,text, parse_mode="Markdown")


@bot.message_handler(func=lambda message:True)
def handle_message(message):
	text = message.text.split()
	chat_id = message.chat.id
	print(text[0])
	fname = message.from_user.first_name
	if message.chat.type == "private":
		# if str(message.from_user.id) in user:
		if True:
			print(f'{fname} INPUT')
			text = f''' Hi kak *{fname}* Sobat Kredibel, pesan ini dijawab oleh Bot Protokol. Ada yang bisa kami bantu?  Kamu bisa memilih:
			- Mengundang *Kepala LKPP* di acara resmi/acara kenegaraan
			- Koordinasi terkait *Tata Upacara*
			- Koordinasi terkait *Tata Penghormatan/Penerimaan Tamu VIP/VVIP*'''
			# bot.send_message(message.chat.id, text, parse_mode="Markdown")

			result = ['Mengundang Kepala LKPP', 'Koordinasi Tata Upacara', 'Tata Penghormatan/Penerimaan Tamu']
			markup = types.InlineKeyboardMarkup()
			for row in result:
				print(row)
				markup.row(types.InlineKeyboardButton(f"{row}",callback_data=f"SEC {row}" ))
			bot.send_message(message.chat.id, text, reply_markup=markup, parse_mode="MARKDOWN")
		else :
			text = f"Mohon Maaf , kakak belum terdaftar, Silahkan hubungi 085292551702"
			bot.send_message(message.chat.id,text, parse_mode="Markdown")
	else:
		text = f"Mohon Maaf , hanya bisa di akses melalui private chat"
		bot.send_message(message.chat.id,text, parse_mode="Markdown")


@bot.callback_query_handler(func=lambda call: True)
def handle_button(call):
	text = call.data
	#print (text)

	menu = text.split()
	print(menu)

	if menu[0] == "SEC":
		# print(f"{call},{menu[1]} {menu[2]} {menu[3]}")
		if menu[1]=='Mengundang':
			cmdHandler.stepSatu(call, menu[1] + " " + menu[2] + " " + menu[3])
		elif menu[1]=='Kunjungan':
			cmdHandler.stepSatuSatu(call, menu[1] + " " + menu[2] + " " + menu[3])
		elif menu[1]=='Koordinasi':
			cmdHandler.stepSatuKoordinasi(call, menu[1] + " " + menu[2] + " " + menu[3])
		elif menu[1]=='Tata':
			cmdHandler.stepSatuTata(call, menu[1] + " " + menu[2] + " " + menu[3])
	elif menu[0] == "PEJABAT":
		if len(menu) == 4:
			cmdHandler.stepDua(call, menu[1] + " " + menu[2] + " " + menu[3])
		elif len(menu) == 2:
			cmdHandler.stepDua(call, menu[1])
	elif menu[0] == "LOKASI":
		if len(menu) == 3:
			cmdHandler.stepTiga(call, menu[1] + " " + menu[2] )
		elif len(menu) == 4:
			cmdHandler.stepTiga(call, menu[1] + " " + menu[2] + " " + menu[3])
	elif menu[0] == "UPACARA":
		if len(menu) == 3:
			cmdHandler.stepUpacara(call, menu[1] + " " + menu[2] )
		elif len(menu) == 4:
			cmdHandler.stepUpacara(call, menu[1] + " " + menu[2] + " " + menu[3])
	elif menu[0] == "TAMU":
		if len(menu) == 3:
			cmdHandler.stepTamu(call, menu[1] + " " + menu[2] )
		elif len(menu) == 4:
			cmdHandler.stepTamu(call, menu[1] + " " + menu[2] + " " + menu[3])
		elif len(menu) == 2:
			cmdHandler.stepTamu(call, menu[1])
	elif menu[0] == "CLOSING":
		if menu[1] == "Kembali":
			cmdHandler.initial(call, menu[1] + " " + menu[2] )
		elif menu[1] == "Selesai":
			cmdHandler.thanks(call, menu[1])








print('bot start running')

def main_loop():
    bot.polling(True)
    while True:
        time.sleep(1)

if __name__ == '__main__':
    try:
        main_loop()
    except Exception as err:
        logging.error(err)
        print ('Internet Error')
