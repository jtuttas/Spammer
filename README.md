# Spammer Python Anwendung

Dieses Tool versendet eine Nachricht an alle E-Mail-Adressen, die in der Datei `mails.xlsx` stehen. Die Nachricht wird aus der Datei `mail.txt` geladen. Die Zugangsdaten für den Mailserver sowie der Betreff werden in der Datei `config.json` gespeichert.

## Voraussetzungen
- Python 3.x
- Siehe `requirements.txt` für benötigte Bibliotheken

## Installation
1. Klone das Repository oder kopiere die Dateien in ein Verzeichnis.
2. Installiere die Abhängigkeiten:
   ```
   pip install -r requirements.txt
   ```
3. Passe die Datei `config.json` mit deinen SMTP-Daten, dem gewünschten Betreff **und optional einer Absenderadresse (`from_address`)** an.


```json
{
  "smtp_server": "dein.smtp.server",
  "smtp_port": 587,
  "smtp_user": "dein_benutzername",
  "smtp_password": "dein_passwort",
  "subject": "Dein Betreff hier",
  "from_address": "deine_absenderadresse@example.com"
}
```

4. Trage die Empfängeradressen in die Datei `mails.xlsx` ein (eine Spalte mit E-Mail-Adressen, z.B. Spalte A, ohne Überschrift).
5. Schreibe die zu versendende Nachricht in die Datei `mail.txt`.

## Ausführung
Starte das Skript mit:
```
python send_mails.py
```

Während des Versands werden Debugging-Meldungen auf der Konsole ausgegeben.

## Hinweise
- Die Anwendung nutzt TLS (Port 587) für den Mailversand.
- Die Zugangsdaten werden im Klartext in `config.json` gespeichert. Achte auf die Sicherheit dieser Datei.
- In der `config.json` kann das Feld `from_address` gesetzt werden, um eine beliebige Absenderadresse zu verwenden. Ist dieses Feld nicht gesetzt, wird standardmäßig `smtp_user` als Absender genutzt.
