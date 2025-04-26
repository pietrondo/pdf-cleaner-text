# PDF Cleaner Text

Applicazione Python per pulire testo da file PDF tramite interfaccia web.

## Requisiti
- Python 3.8+
- Librerie: Flask, PyPDF2

## Note sull'uso di PyPDF2
- La libreria PyPDF2 non supporta la modifica diretta del testo nelle pagine PDF
- Il testo viene estratto e filtrato, ma le modifiche non vengono riapplicate al PDF originale
- Il PDF risultante conterrà le pagine originali senza alterazioni

## Installazione
```bash
pip install -r requirements.txt
```

## Configurazione
1. Creare file `.env` con eventuali variabili d'ambiente
2. Modificare `config.py` per impostazioni personalizzate

## Utilizzo
1. Avviare l'applicazione: `python app.py`
2. Accedere all'interfaccia web su `http://localhost:5000`
3. Caricare PDF e specificare testo da rimuovere
4. Scaricare PDF pulito

## Deployment CloudPanel

### Prerequisiti
- Server Linux con CloudPanel installato
- Python 3.8+ installato
- uWSGI e Nginx configurati

### Configurazione uWSGI
1. Creare file di configurazione `pdf-cleaner-text.uwsgi.ini`:
```ini
[uwsgi]
plugins = python3
master = true
protocol = uwsgi
socket = 127.0.0.1:8090
wsgi-file = /home/site-user/htdocs/pdf-cleaner-text/app.py

buffer-size = 8192
reload-on-rss = 250
workers = 4
enable-threads = true
close-on-exec = true
umask = 0022
uid = site-user
gid = site-user
ignore-sigpipe = true
ignore-write-errors = true
disable-write-exception = true
```

### Configurazione Nginx
Modificare il file di configurazione Nginx per includere:
```nginx
location / {
    include uwsgi_params;
    uwsgi_read_timeout 3600;
    uwsgi_pass 127.0.0.1:8090;
}
```

### Avvio applicazione
```bash
systemctl restart uwsgi
systemctl restart nginx
```