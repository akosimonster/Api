from flask import Flask ,request ,jsonify #line:1
r =None #line:2
j =str #line:3
p =request .args #line:4
import requests #line:5
d =requests .exceptions #line:6
x =requests .get #line:7
D =Flask (__name__ )#line:8
def l (OOO0O0000O0O0O00O ):#line:9
 try :#line:10
  O0OO0O00OO0O0O0O0 =x (f"https://otaku-is-unbreakable-api.vercel.app/proxy/cors?url=https://otaku-is-unbreakable-api.vercel.app/bypass?url={url}")#line:11
  O0OO0O00OO0O0O0O0 .raise_for_status ()#line:12
  O00OOO0O00OOOOOO0 =O0OO0O00OO0O0O0O0 .json ()#line:13
  O0OOOOOOO0OOOO00O =O00OOO0O00OOOOOO0 .get ('bypassed')#line:14
  OOO0000OOOO0OO0O0 =O00OOO0O00OOOOOO0 .get ('time_spent')#line:15
  if O0OOOOOOO0OOOO00O is r or OOO0000OOOO0OO0O0 is r :#line:16
   return {'error':'Due to error -KIER'}#line:17
  return {'bypassed':O0OOOOOOO0OOOO00O ,'time_spent':OOO0000OOOO0OO0O0 }#line:18
 except d .RequestException as O0OOO0O00OOOOOOOO :#line:19
  return {'error':j (O0OOO0O00OOOOOOOO )}#line:20
@D .route ('/bypass',methods =['GET'])#line:21
def C ():#line:22
 O0OO00O0O0O0OOOO0 =p .get ('url')#line:23
 if not O0OO00O0O0O0OOOO0 :#line:24
  return jsonify ({'error':'No URL Provided  -KIER'}),400 #line:25
 O000O0OO000OO00OO =l (O0OO00O0O0O0OOOO0 )#line:26
 if 'error'in O000O0OO000OO00OO :#line:27
  return jsonify ({'error':O000O0OO000OO00OO ['error']}),500 #line:28
 else :#line:29
  return jsonify ({'success':'true','key':O000O0OO000OO00OO ['bypassed'],'time':O000O0OO000OO00OO ['time_spent']})#line:30
if __name__ =="__main__":#line:31
 D .run (host ='0.0.0.0',port =9838 )#line:32
