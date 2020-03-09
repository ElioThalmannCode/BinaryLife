# BinaryLife Dokumentation

---
##  1. <a name='TableofContent'></a>Table of Content
<!-- vscode-markdown-toc -->
* 1. [Table of Content](#TableofContent)
* 2. [Wie startet man das Game?](#WiestartetmandasGame)
		* 2.1. [Installiere python3](#Installierepython3)
		* 2.2. [Führe das Game aus](#FhredasGameaus)
* 3. [Kurzfassung](#Kurzfassung)
* 4. [Was gibt es für Elemente in diesem Spiel.](#WasgibtesfrElementeindiesemSpiel.)
		* 4.1. [NPC](#NPC)
		* 4.2. [hood](#hood)
		* 4.3. [Familie](#Familie)
		* 4.4. [yourself](#yourself)
* 5. [Namen](#Namen)
* 6. [Exposé](#Expos)
	* 6.1. [Inhalt](#InhaltdesGames)
	* 6.2. [Zielgeräte](#Zielgerte)
	* 6.3. [Positionierung](#Positionierung)
	* 6.4. [Risiken](#Risiken)

<!-- vscode-markdown-toc-config
	numbering=true
	autoSave=true
	/vscode-markdown-toc-config -->
<!-- /vscode-markdown-toc -->

----

##  2. <a name='WiestartetmandasGame'></a>Wie startet man das Game?

####  2.1. <a name='Installierepython3'></a>Installiere python3

##### Linux:
```bash
sudo apt install python3 #ubuntu
sudo dnf install python3 #fedora/debian
git clone https://github.com/ElioThalmannCode/BinaryLife
```
##### Windows:
Tutorial: https://www.howtogeek.com/197947/how-to-install-python-on-windows/
##### MacOS:
```bash
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
brew install python3 
```
####  2.2. <a name='FhredasGameaus'></a>Führe das Game aus
a. Gehe zum Zielordner mit bash oder cmd.
b. führe diesen Befehl aus:
```bash
git clone https://github.com/ElioThalmannCode/BinaryLife
python3 main.py
```

---

##  3. <a name='Kurzfassung'></a>Kurzfassung
Im Grunde wird die Story des Spielers selber geschrieben anhand der Endscheidungen die der Spieler in dem Spiel getroffen hat. Es gibt kein genaues Ziel und auch kein genaues Ende es wird einfach so lange gespielt bis du stirbst oder du aufgibst. Die Story besteht aus zufälligen Ereignissen die auf den Spieler treffen. Das Ziel dieses Spiels ist mit den Ereignissen und Schwierigkeiten des Lebens umzugehen.

---

##  4. <a name='WasgibtesfrElementeindiesemSpiel.'></a>Was gibt es für Elemente in diesem Spiel.

####  4.1. <a name='NPC'></a>NPC
NPC ist Englisch und heisst "Non-player character" was soviel heisst wie "Nicht-Spieler-Charakter" also eine Person der du im Spiel begegnest aber der du keine Befehle geben kannst.

So sieht die ```class``` des NPC aus:
```python
class npc():
    def __init__(self, first_name, last_name, gender, age, contact, love, money, family, alive, looks, iq):
        self.first_name =   first_name
        self.last_name  =   last_name
        self.gender     =   gender
        self.age        =   age
        self.contact    =   contact
        self.love       =   love
        self.money      =   money
        self.family     =   family
        self.alive      =   alive
        self.looks      =   looks
        self.iq         =   iq
```
####  4.2. <a name='hood'></a>hood
Hood ist die englische Abkürzung für Nachbarschaft. Das ist der Ort anderem die Person die du spielst reingeboren wird.
So sieht die hood ```class``` aus:
```python
class hood():
    def __init__(self, save, education):
        self.save   =   save
        self.education  =   education
```
####  4.3. <a name='Familie'></a>Familie
Die Familie ist sehr wichtig in deinem Spielverlauf! Wenn du eine reiche Familie hast sind die Chancen höher das du gute Bildung und ein sicheres Leben erhältst. Es wird die gleiche ```class``` wie bei NPC verwendet.

####  4.4. <a name='yourself'></a>yourself
Yourself ist der Spieler den man gerade am spielen ist. Diese ```class``` bestimmt dein Aussehen, Name, iq usw. Dies ist sehr wichtig im ganzen Spielverlauf.
Die yourself ```class``` sieht so aus:
```python
class yourself_class():
    def __init__(self, first_name, last_name, gender, health, iq, looks, fame, age):
        self.first_name =   first_name
        self.last_name  =   last_name
        self.gender =   gender
        self.health =   health
        self.iq     =   iq
        self.looks  =   looks
        self.fame   =   fame
        self.age    =   age
```
usw.

---

##  5. <a name='Namen'></a>Namen
Es gibt enorm viele Namen in diesem Spiel. Es wird ein zufälliger Name für einen neuen Spieler ausgewählt.

---

##  6. <a name='Expos'></a>Exposé
###  6.1. <a name='InhaltdesGames'></a>Inhalt:
Du spielst ein Spieler der zufällig generiert wird. In diesem Spiel gibt es immer wieder zufällige ereignisse die random passieren. Die ereignisse werden nach Alter angepasst. Das Spiel startet in dem du ein kleines Kind bist. Du kannst in diesen Jahren noch nicht viel entscheiden dies übernehmen nämlich deine Eltern für dich. Sobald du dann aber in die Schule gehst, sobald du etwas älter bist, gibt es schon die ersten kindlichen Ereignisse wie zb. du wirst mal wieder von deinem Lehrer zum nachsitzen verdonnert und bekommst ein Brief heim oder du zerstörst aus Versehen das Fenster deines Nachbaren. Dies ist aber auch der Teil in deinem Leben wo du dich für deinen zukünftigen Beruf qualifizieren musst. Wenn du schlecht in der Schule bist kannst du nicht auf die höheren Schulen gehen wo du dann auch in hohe Einkommensstufen kommst. Da kommen wir auch zum nächsten Teil deines Lebens, dem Leben als junger Erwachsener. Das ist ein sehr wichtiger Abschnitt in deinem Leben. In diesem Teil wirst du in deinen Job einsteigen, einige positive wie auch negative Ereignisse werden dir in Nachtclubs passieren und vieleicht wirst du ein Partner fürs Leben erhalten. Du kannst auch hookups und Onlineverabredungen machen. Der nächste Schritt ist das Erwachsenenleben. Du kannst 
###  6.2. <a name='Zielgerte'></a> Zielgeräte
Dieses Spiel kann auf jedem Gerät gespielt werden solange es Python unterstützt.
###  6.3. <a name='Positionierung'></a>Positionierung
Dieses Spiel ist ein 1/1 Klon zu dem 2018 erschienenen Spiel Bitlife. Es ist ein "Casual Game". Das Spiel ist für jede Altersgruppe fast konzipiert ausser der zu jungen Spieler da es die Option Alkohol oder Drogen zu konsumieren gibt sobald man in ein Nachtclub geht. Bei dem Spiel wird besonders auf das mehrmals durchspielen gesetzt da jeder neuer Spielversuch ein ganz neues Spielerlebnis ist.
###  6.4. <a name='Risiken'></a>Risiken

---