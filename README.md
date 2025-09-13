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
3. Passe die Datei `config.json` mit deinen SMTP-Daten und dem gewünschten Betreff an.
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
