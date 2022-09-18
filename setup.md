```bash
sudo apt update && sudo apt install apache2 supervisor -y
```

> /etc/supervisor/conf.d/smart_home.conf
```conf
[program:smart_home]
directory=/home/pi/Desktop/py_smart_home       
command=/home/pi/Desktop/py_smart_home/venv/bin/gunicorn -w 9 app:app --timeout 18000
user=pi
autostart=true
autorestart=true
stopasgroup=true
killasgroup=true
stderr_logfile=/var/log/smart_home/app.err.log
stdout_logfile=/var/log/smart_home/app.out.log
```
> /etc/apache2/sites-enabled/000-default.conf
```conf
<VirtualHost *:80>
	ProxyPreserveHost On
	ProxyPass / http://127.0.0.1:8000/
	ProxyPassReverse / http://127.0.0.1:8000/
</VirtualHost>
```

> Append /etc/apache2/apache2.conf
```conf
LoadModule proxy_module modules/mod_proxy.so
LoadModule proxy_http_module modules/mod_proxy_http.so
```

```bash
sudo a2enmod proxy
sudo a2enmod proxy_http
sudo a2enmod proxy_balancer
sudo a2enmod lbmethod_byrequests
sudo systemctl restart apache2
```

# pass with sudo su
> /etc/nginx/conf.d/smart_home.conf
server {
	listen 80;

	server_name _;
	location /static {
		alias /home/api/sap_api/main_pack/static;
	}
	location / {
		proxy_pass http://localhost:8000;
		include /etc/nginx/proxy_params;
		proxy_redirect off;
	}
}

defaultyny udalit etmeli
rm /etc/nginx/sites-enabled/default

commands must do
////
supervisorctl start all
supervisorctl reload
systemctl restart nginx
////

command for server
curl --header "Content-Type: application/json" --request POST --data '{"command":"test_local","action":"1"}' http://192.168.1.88:5000/esp/JsonToArg/
