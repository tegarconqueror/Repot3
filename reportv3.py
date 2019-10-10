#!/usr/bin/python
# coding: utf-8
# copyright: Tegar Moonata

"""
   JANGAN REPORT AKUN YANG GAK BERSALAH
   ANJING, MEMEK, BANGSAT !!
"""

import os,sys,requests,mechanize,cookielib
from bs4 import BeautifulSoup
from http.cookiejar import LWPCookieJar as coki
from getpass import getpass
from time import sleep

reload( sys )
sys.setdefaultencoding( 'utf8' )
br = mechanize.Browser()
cj = cookielib.LWPCookieJar( "cookies.log" )
br.set_cookiejar( cj )
br.set_handle_gzip( True )
br.set_handle_redirect( True )
br.set_handle_referer( True )
br.set_handle_robots( False )
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders=[('User-Agent','Mozilla/5.0 (Linux; Android 8.1.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3384.0 Mobile Safari/537.36')]
URL = "https://mbasic.facebook.com{}"
s = requests.Session()

H = "\033[0;92m"
P = "\033[0;97m"
M = "\033[0;91m"
C = "\033[0;96m"
id = []
asu1 = []
asu2 = []
asu3 = []

def login():
	banner()
	print P+"[#] Login Akun Facebook [#]"
	br.open( "https://mbasic.facebook.com" )
	br._factory.is_html = True
	br.select_form( nr = 0 )
	br.form["email"] = raw_input("[-] username: ")
	br.form["pass"] = getpass("[-] password: ")
	br.submit()
	url = br.geturl()
	if "save-device" in str( url ):
		cj.save()
		autoReport()
	elif "checkpoint" in str( url ):
		exit("[!] akun cekpoint:)*")
	else:
		exit("[!] login gagal cek email / pass")

def otw_report( id ):
	loop=0
	print "\n[*] report profile dengan tuduhan akun palsu\n"
	sleep(1)
	bs1 = BeautifulSoup( s.get(URL.format( "/%s?v=timeline"%( target ))).content, "html.parser" )
	bs2 = BeautifulSoup( s.get(URL.format( bs1.find( "a", string = "Lainnya" ).get( "href" ))).content, "html.parser" )
	bs3 = BeautifulSoup( s.get(URL.format( bs2.find( "a", string = "Cari Dukungan atau Laporkan Profil").get( "href" ))).content, "html.parser" )
	for x in bs3( "form" ):
		asu1.append( x["action"] )
	for x in bs3( "input" ):
		try:
			if "fb_dtsg" in x["name"]:
				asu1.append( x["value"] )
			if "jazoest" in x["name"]:
				asu1.append( x["value"] )
				break
		except:pass
	bs4 = BeautifulSoup( s.post(URL.format( asu1[0] ),data={"fb_dtsg": asu1[1],"jazoest": asu1[2],"tag": "profile_fake_account"}).content, "html.parser" )
	for x in bs4( "form" ):
		asu2.append( x["action"] )
	for x in bs4( "input" ):
		try:
			if "fb_dtsg" in x["name"]:
				asu2.append( x["value"] )
			if "jazoest" in x["name"]:
				asu2.append( x["value"] )
			if "RX_PROFILE_REPORT_CONFIRMATION" in x["value"]:
				asu2.append( x["value"] )
				break
		except:pass
	if "RX_PROFILE_REPORT_CONFIRMATION" in asu2[3]:
		bs5 = BeautifulSoup( s.post(URL.format( asu2[0] ),data={"fb_dtsg": asu2[1],"jazoest": asu2[2],"action_key": asu2[3]}).content, "html.parser" )
		for x in bs5( "form" ):
			asu3.append( x["action"] )
		for x in bs5( "input" ):
			try:
				if "fb_dtsg" in x["name"]:
					asu3.append( x["value"] )
				if "jazoest" in x["name"]:
					asu3.append( x["value"] )
					break
			except:pass
		report = s.post(URL.format( asu3[0] ),data={"fb_dtsg": asu3[1],"jazoest": asu3[2],"checked": "yes","action": "Laporkan"}).text
		if "Dikirimkan ke Facebook untuk Ditinjau" in str( report ):
			print "[success] -> %s%s%s"%( H,bs1.title.text,P )
		else:
			print "[failed] -> %s%s%s"%( M,bs1.title.text,P )
	else:
		print "[failed] -> %s%s%s"%( M,bs1.title.text,P )
	print "\n[*] report status dengan tuduhan ujaran kebencian dll."
	sleep(1)
	for meki in id:
		loop+=1
		print "\n[*] report ke %s "%(loop)
		try:		
			asu4 = []
			bs6 = BeautifulSoup( s.get( meki ).content, "html.parser" )
			for x in bs6( "form" ):
				asu4.append( x["action"] )
			for x in bs6( "input" ):
				try:
					if "fb_dtsg" in x["name"]:
						asu4.append( x["value"] )
					if "jazoest" in x["name"]:
						asu4.append( x["value"] )
						break
				except:pass
			asu5 = []
			bs7 = BeautifulSoup( s.post(URL.format( asu4[0] ),data={"fb_dtsg": asu4[1],"jazoest": asu4[2],"tag": "harassment"}).content, "html.parser" )
			for x in bs7( "form" ):
				asu5.append( x["action"] )
			for x in bs7( "input" ):
				try:
					if "fb_dtsg" in x["name"]:
						asu5.append( x["value"] )
					if "jazoest" in x["name"]:
						asu5.append( x["value"] )
					if "RESOLVE_PROBLEM_REDIRECT" in x["value"] or "FRX_PROFILE_REPORT_CONFIRMATION" in x["value"]:
						asu5.append( x["value"] )
						break
				except:pass
			if "RESOLVE_PROBLEM_REDIRECT" in asu5[3]:
				asu6 = []
				bs8 = BeautifulSoup( s.post(URL.format( asu5[0] ),data={"fb_dtsg": asu5[1],"jazoest": asu5[2],"action_key": asu5[3]}).content, "html.parser" )
				for x in bs8( "form" ):
					asu6.append( x["action"] )
				for x in bs8( "input" ):
					try:
						if "fb_dtsg" in x["name"]:
							asu6.append( x["value"] )
						if "jazoest" in x["name"]:
							asu6.append( x["value"] )
							break
					except:pass
				asu7 = []
				bs9 = BeautifulSoup( s.post(URL.format( asu6[0] ),data={"fb_dtsg": asu6[1],"jazoest": asu6[2],"answer": "offensive"}).content, "html.parser" )
				for x in bs9( "form" ):
					asu7.append( x["action"] )
				for x in bs9( "input" ):
					try:
						if "fb_dtsg" in x["name"]:
							asu7.append( x["value"] )
						if "jazoest" in x["name"]:
							asu7.append( x["value"] )
							break
					except:pass
				if "Apa yang salah dengan foto ini?" in str( bs9 ):
					asu8 = []
					bs10 = BeautifulSoup( s.post(URL.format( asu7[0] ),data={"fb_dtsg": asu7[1],"jazoest": asu7[2],"answer":"other"}).content, "html.parser" )
					for x in bs10( "form" ):
						asu8.append( x["action"] )
					for x in bs10( "input" ):
						try:
							if "fb_dtsg" in x["name"]:
								asu8.append( x["value"] )
							if "jazoest" in x["name"]:
								asu8.append( x["value"] )
								break
						except:pass
					asu9 = []
					bs11 = BeautifulSoup( s.post(URL.format( asu8[0] ),data={"fb_dtsg": asu8[1],"jazoest": asu8[2],"answer":"hate"}).content, "html.parser" )
					for x in bs11( "form" ):
						asu9.append( x["action"] )
					for x in bs11( "input" ):
						try:
							if "fb_dtsg" in x["name"]:
								asu9.append( x["value"] )
							if "jazoest" in x["name"]:
								asu9.append( x["value"] )
								break
						except:pass
					if "Kirimkan ke Facebook untuk Ditinjau" in str( bs11 ):
						reportt = s.post(URL.format( asu9[0] ),data={"fb_dtsg": asu9[1],"jazoest": asu9[2],"action_key": "REPORT_CONTENT"}).text
						if "Dikirimkan ke Facebook untuk Ditinjau" in str( reportt ):
							print "[success] -> %s%s%s"%( H,bs1.title.text,P )
						else:
							print "[failed] -> %s%s%s"%( M,bs1.title.text,P )
					else:
						print "[failed] -> %s%s%s"%( M,bs1.title.text,P )
				elif "Apa yang salah dengan kiriman ini?" in str( bs9 ):
					asu8 = []
					bs10 = BeautifulSoup( s.post(URL.format( asu7[0] ),data={"fb_dtsg": asu7[1],"jazoest": asu7[2],"answer":"hatespeech"}).content, "html.parser" )
					for x in bs10( "form" ):
						asu8.append( x["action"] )
					for x in bs10( "input" ):
						try:
							if "fb_dtsg" in x["name"]:
								asu8.append( x["value"] )
							if "jazoest" in x["name"]:
								asu8.append( x["value"] )
								break
						except:pass
					asu9 = []
					bs11 = BeautifulSoup( s.post(URL.format( asu8[0] ),data={"fb_dtsg": asu8[1],"jazoest": asu8[2],"answer":"individual"}).content, "html.parser" )
					for x in bs11( "form" ):
						asu9.append( x["action"] )
					for x in bs11( "input" ):
						try:
							if "fb_dtsg" in x["name"]:
								asu9.append( x["value"] )
							if "jazoest" in x["name"]:
								asu9.append( x["value"] )
								break
						except:pass
					asu10 = []
					bs12 = BeautifulSoup( s.post(URL.format( asu9[0] ),data={"fb_dtsg": asu9[1],"jazoest": asu9[2],"answer":"harassing_someone_else"}).content, "html.parser" )
					for x in bs12( "form" ):
						asu10.append( x["action"] )
					for x in bs12( "input" ):
						try:
							if "fb_dtsg" in x["name"]:
								asu10.append( x["value"] )
							if "jazoest" in x["name"]:
								asu10.append( x["value"] )
								break
						except:pass
					if "Kirimkan ke Facebook untuk Ditinjau" in str( bs12 ):
						reportt = s.post(URL.format( asu10[0] ),data={"fb_dtsg": asu10[1],"jazoest": asu10[2],"action_key": "REPORT_CONTENT"}).text
						if "Dikirimkan ke Facebook untuk Ditinjau" in str( reportt ):
							print "[success] -> %s%s%s"%( H,bs1.title.text,P )
						else:
							print "[failed] -> %s%s%s"%( M,bs1.title.text,P )
					else:
						print "[failed] -> %s%s%s"%( M,bs1.title.text,P )
				elif "Apa yang salah dengan postingan ini?" in str( bs9 ):
					asu8 = []
					bs10 = BeautifulSoup( s.post(URL.format( asu7[0] ),data={"fb_dtsg": asu7[1],"jazoest": asu7[2],"answer":"againstbelief"}).content, "html.parser" )
					for x in bs10( "form" ):
						asu8.append( x["action"] )
					for x in bs10( "input" ):
						try:
							if "fb_dtsg" in x["name"]:
								asu8.append( x["value"] )
							if "jazoest" in x["name"]:
								asu8.append( x["value"] )
								break
						except:pass
					reportt = s.post(URL.format( asu8[0] ),data={"fb_dtsg": asu8[1],"jazoest": asu8[2],"action_key": "REPORT_CONTENT"}).text
					if "Dikirimkan ke Facebook untuk Ditinjau" in str( reportt ):
						print "[success] -> %s%s%s"%( H,bs1.title.text,P )
					else:
						print "[failed] -> %s%s%s"%( M,bs1.title.text,P )
				else:
					print "[failed] -> %s%s%s"%( M,bs1.title.text,P )
			elif "FRX_PROFILE_REPORT_CONFIRMATION" in asu5[3]:
				asu6 = []
				bs8 = BeautifulSoup( s.post(URL.format( asu5[0] ),data={"fb_dtsg": asu5[1],"jazoest": asu5[2],"action_key": asu5[3]}).content, "html.parser" )
				for x in bs8( "form" ):
					asu6.append( x["action"] )
				for x in bs8( "input" ):
					try:
						if "fb_dtsg" in x["name"]:
							asu6.append( x["value"] )
						if "jazoest" in x["name"]:
							asu6.append( x["value"] )
							break
					except:pass
				reportt = s.post(URL.format( asu6[0] ),data={"fb_dtsg": asu6[1],"jazoest": asu6[2],"checked": "yes","action": "Laporkan"}).text
				if "Dikirimkan ke Facebook untuk Ditinjau" in str( reportt ):
					print "[success] -> %s%s%s"%( H,bs1.title.text,P )
				else:
					print "[failed] -> %s%s%s"%( M,bs1.title.text,P )
			else:
				print "[failed] -> %s%s%s"%( M,bs1.title.text,P )
		except IndexError:
			print "[failed] -> %s%s%s"%( M,bs1.title.text,P )
	os.remove("cookies.log")
	exit("\n[+] done, semoga akun target angus:)*")
					
def post_id( link ):
	bs1 = BeautifulSoup( s.get( link ).content, "html.parser")
	if "Cari Dukungan atau Laporkan Postingan" in str( bs1 ):
		for x in bs1.find_all( "a", string = "Cari Dukungan atau Laporkan Postingan" ):
			id.append( URL.format( x.get( "href" )))
			print "\r[*] mengambil id post %s  "%( len( id )),
			sys.stdout.flush()
			if limit == len( id ):
				otw_report( id )
	if "Lihat Berita Lain" in str( bs1 ):
		post_id( URL.format( bs1.find( "a", string = "Lihat Berita Lain" ).get( "href" )))
	otw_report( id )
		
def autoReport():
	global limit,target
	os.system("clear")
	s.cookies = coki( "cookies.log" )
	s.cookies.load()
	bs1 = BeautifulSoup( s.get(URL.format( "/language.php" )).content, "html.parser" )
	s.get(URL.format( bs1.find( "a", string = "Bahasa Indonesia" ).get( "href" )))
	banner()
	target = raw_input("[*] ID target: ")
	if target.lower() in ["dulahz","100005584243934"]:
		exit("[!] jgn report akun gue bngstss")
	bs2 = BeautifulSoup( s.get(URL.format( "/%s?v=timeline"%( target ))).content, "html.parser" )
	if not "Lainnya" in str( bs2 ):
		exit("[!] profile tidak ditemukan")
	print "[*] nama target %s%s%s "%( H,bs2.title.text,P )
	limit = int(raw_input("[?] jumlah post yang akan direport: "))
	if limit in [""]:
		exit("[!] goblokk")
	post_id(URL.format( "/%s?v=timeline"%( target )))
	
def cek_cookies():
	try:
		s.cookies = coki( "cookies.log" )
		s.cookies.load()
	except IOError:
		login()
	aa = s.get(URL.format( "/me" )).text
	if "mbasic_logout_button" in str( aa ):
		autoReport()
	else:login()
	
def banner():
	print """%s

☆ ════════ •⊰❂⊱• ════════ ☆
☑ Author: Moonza x Voldemort.
☑ Wa: 0895618031306.
☑ Email: moonata404@yahoo.com.
☑ GitHub: https://github.com/tegar001.
☆ ════════ •⊰❂⊱• ════════ ☆
%s #%s ©2019
%s #%s ☾ Voldemort ☽ %s
"""%( C,H,M,H,M,P )

try:
	cek_cookies()
except Exception as R:
	print "\n[!] Error %s"%( R )