import smtplib
import pandas as pd
import json
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sys
import os
from email.mime.base import MIMEBase
from email import encoders
import mimetypes

CONFIG_FILE = 'config.json'
MAIL_FILE = 'mail.txt'
MAILS_XLSX = 'mails.xlsx'

ATTACHMENT_DIR = 'Anhang'

# Debugging Funktion
def debug(msg):
    print(f"[DEBUG] {msg}")

def load_config():
    debug(f"Lade Konfiguration aus {CONFIG_FILE}")
    with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def load_message():
    debug(f"Lese Nachricht aus {MAIL_FILE}")
    with open(MAIL_FILE, 'r', encoding='utf-8') as f:
        return f.read()

def load_emails():
    debug(f"Lese E-Mail-Adressen aus {MAILS_XLSX}")
    df = pd.read_excel(MAILS_XLSX, engine='openpyxl', header=None)
    emails = df.iloc[:,0].dropna().astype(str).tolist()
    debug(f"Gefundene E-Mail-Adressen: {emails}")
    return emails

def send_mail(smtp_server, smtp_port, smtp_user, smtp_password, from_address, subject, to_addr, message):
    debug(f"Sende E-Mail an {to_addr}")
    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_addr
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain', 'utf-8'))

    # Alle Attachments aus dem Anhang-Ordner anhängen
    if os.path.isdir(ATTACHMENT_DIR):
        for filename in os.listdir(ATTACHMENT_DIR):
            filepath = os.path.join(ATTACHMENT_DIR, filename)
            if os.path.isfile(filepath):
                import unicodedata
                debug(f"Füge Anhang hinzu: {filename}")
                ctype, encoding = mimetypes.guess_type(filepath)
                if ctype is None or encoding is not None:
                    ctype = 'application/octet-stream'
                maintype, subtype = ctype.split('/', 1)
                # ASCII-kompatibler Dateiname: Leerzeichen zu Unterstrich, Umlaute/Sonderzeichen entfernen
                def to_ascii_filename(name):
                    name = name.replace(' ', '_')
                    name = unicodedata.normalize('NFKD', name).encode('ascii', 'ignore').decode('ascii')
                    return name
                safe_filename = to_ascii_filename(filename)
                with open(filepath, 'rb') as f:
                    filedata = f.read()
                    part = MIMEBase(maintype, subtype)
                    part.set_payload(filedata)
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition', f'attachment; filename="{safe_filename}"')
                msg.attach(part)

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_user, smtp_password)
            server.sendmail(from_address, to_addr, msg.as_string())
        debug(f"E-Mail erfolgreich an {to_addr} gesendet.")
    except Exception as e:
        debug(f"Fehler beim Senden an {to_addr}: {e}")

def main():
    config = load_config()
    message = load_message()
    emails = load_emails()
    for email in emails:
        send_mail(
            config['smtp_server'],
            config['smtp_port'],
            config['smtp_user'],
            config['smtp_password'],
            config.get('from_address', config['smtp_user']),
            config['subject'],
            email,
            message
        )

if __name__ == '__main__':
    main()
