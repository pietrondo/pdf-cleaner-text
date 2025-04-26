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
Seguire la guida ufficiale: https://www.cloudpanel.io/docs/v2/python/deployment/uwsgi/