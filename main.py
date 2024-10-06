from flask import Flask,request,jsonify
r=None
j=str
p=request.args
import requests
d=requests.exceptions
x=requests.get
D=Flask(__name__)
def l(F):
 try:
  T=x(f"https://otaku-is-unbreakable-api.vercel.app/proxy/cors?url=https://otaku-is-unbreakable-api.vercel.app/bypass?url={url}")
  T.raise_for_status()
  S=T.json()
  H=S.get('bypassed')
  N=S.get('time_spent')
  if H is r or N is r:
   return{'error':'Due to error -KIER'}
  return{'bypassed':H,'time_spent':N}
 except d.RequestException as e:
  return{'error':j(e)}
@D.route('/bypass',methods=['GET'])
def C():
 F=p.get('url')
 if not F:
  return jsonify({'error':'No URL Provided  -KIER'}),400
 P=l(F)
 if 'error' in P:
  return jsonify({'error':P['error']}),500
 else:
  return jsonify({'success':'true','key':P['bypassed'],'time':P['time_spent']})
if __name__=="__main__":
 D.run(host='0.0.0.0',port=9838)
