from flask import Flask, render_template, request, send_file
import fitz  # PyMuPDF
import io
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Ottieni file PDF e testo da rimuovere
        pdf_file = request.files['pdf']
        text_to_remove = request.form['text_to_remove']
        
        # Apri il PDF con PyMuPDF
        doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
        
        # Processa ogni pagina
        for page in doc:
            # Trova tutte le occorrenze del testo da rimuovere
            text_instances = page.search_for(text_to_remove)
            
            # Rimuovi ogni occorrenza
            for inst in text_instances:
                page.add_redact_annot(inst)
            
            # Applica le modifiche
            page.apply_redactions()
        
        # Salva il PDF pulito
        output = io.BytesIO()
        doc.save(output)
        output.seek(0)
        doc.close()
        
        return send_file(
            output,
            mimetype='application/pdf',
            as_attachment=True,
            download_name='cleaned.pdf'
        )
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)