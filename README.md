# BotTwitter
Bot Twitter para hacer tweets automaticos

- Instalamos tweepy
$pip install tweepy
sino tenemos instalado "pip" lo hacemos de la siguiente manera: sudo apt-get install python-pip
 
- Creamos una aplicacion
En la siguiente pagina creamos la aplicacion: https://apps.twitter.com/app/new
 
- Obtenemos los tokens:
Consumer Key (API Key)
Consumer Secret (API Secret)
Access Token
Access Token Secret
Los colocamos en el script y listo...!
 
- Ejecutamos nuestro script:
$python tweet.py
 
- Modificamos tweets.py
Aqui colocamos las lineas como queremos que aparezcan de manera automatica
 
- por ultimo lo colocamos como tarea programada:
59 * * * * /ruta de script/python tweet.py
