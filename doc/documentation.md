# BinaryLife Dokumentation

---
## Table of Content
<!-- TOC -->

- [BinaryLife Dokumentation](#binarylife-dokumentation)
    - [Table of Content](#table-of-content)
                    - [Elio Thalmann](#elio-thalmann)
    - [1.Wie startet man das Game?](#1wie-startet-man-das-game)
            - [1.1 Installiere python3(Wenn du es noch nicht Besitzt)](#11-installiere-python3wenn-du-es-noch-nicht-besitzt)
                - [Linux:](#linux)
                - [Windows:](#windows)
                - [MacOS:](#macos)
            - [1.2 Führe das Game aus](#12-führe-das-game-aus)
    - [2.Kurzfassung](#2kurzfassung)
    - [3.Was gibt es für Elemente in diesem Spiel.](#3was-gibt-es-für-elemente-in-diesem-spiel)
        - [3.1 NPC](#31-npc)
        - [3.2 hood](#32-hood)
        - [3.3 Familie](#33-familie)
        - [3.4 yourself](#34-yourself)
    - [4. Namen](#4-namen)
    - [5. Exposé](#5-exposé)
        - [5.1 Inhalt:](#51-inhalt)
        - [5.2 Zielgeräte](#52-zielgeräte)
        - [5.3 Positionierung](#53-positionierung)
        - [Risiken](#risiken)

<!-- /TOC -->

## 1.Wie startet man das Game?

#### 1.1 Installiere python3(Wenn du es noch nicht Besitzt)

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
#### 1.2 Führe das Game aus
a. Gehe zum Zielordner mit bash oder cmd.
b. führe diesen Befehl aus:
```bash
git clone https://github.com/ElioThalmannCode/BinaryLife
python3 main.py
```
## 2.Kurzfassung
Im Grunde wird die Story des Spielers selber geschrieben anhand der Endscheidungen die der Spieler in dem Spiel getroffen hat. Es gibt kein genaues Ziel und auch kein genaues Ende es wird einfach so lange gespielt bis du stirbst oder du aufgibst. Die Story besteht aus zufälligen Ereignissen die auf den Spieler treffen. Das Ziel dieses Spiels ist mit den Ereignissen und Schwierigkeiten des Lebens umzugehen.

## 3.Was gibt es für Elemente in diesem Spiel.

#### 3.1 NPC
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
#### 3.2 hood
Hood ist die englische Abkürzung für Nachbarschaft. Das ist der Ort anderem die Person die du spielst reingeboren wird.
So sieht die hood ```class``` aus:
```python
class hood():
    def __init__(self, save, education):
        self.save   =   save
        self.education  =   education
```
### 3.3 Familie
Die Familie ist sehr wichtig in deinem Spielverlauf! Wenn du eine reiche Familie hast sind die Chancen höher das du gute Bildung und ein sicheres Leben erhältst. Es wird die gleiche ```class``` wie bei NPC verwendet.

### 3.4 yourself
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
## 4. Namen
Es gibt enorm viele Namen in diesem Spiel. Es wird ein zufälliger Name für einen neuen Spieler ausgewählt.
## 5. Exposé
### 5.1 Inhalt:
Du spielst ein Spieler der zufällig generiert wird. In diesem Spiel gibt es immer wieder zufällige ereignisse die random passieren. Die ereignisse werden nach Alter angepasst. Das Spiel startet in dem du ein kleines Kind bist. Du kannst in diesen Jahren noch nicht viel entscheiden dies übernehmen nämlich deine Eltern für dich. Sobald du dann aber in die Schule gehst, sobald du etwas älter bist, gibt es schon die ersten kindlichen Ereignisse wie zb. du wirst mal wieder von deinem Lehrer zum nachsitzen verdonnert und bekommst ein Brief heim oder du zerstörst aus Versehen das Fenster deines Nachbaren. Dies ist aber auch der Teil in deinem Leben wo du dich für deinen zukünftigen Beruf qualifizieren musst. Wenn du schlecht in der Schule bist kannst du nicht auf die höheren Schulen gehen wo du dann auch in hohe Einkommensstufen kommst. Da kommen wir auch zum nächsten Teil deines Lebens, dem Leben als junger Erwachsener. Das ist ein sehr wichtiger Abschnitt in deinem Leben. In diesem Teil wirst du in deinen Job einsteigen, einige positive wie auch negative Ereignisse werden dir in Nachtclubs passieren und vieleicht wirst du ein Partner fürs Leben erhalten. Du kannst auch hookups und Onlineverabredungen machen. Der nächste Schritt ist das Erwachsenenleben. Du kannst 
### 5.2 Zielgeräte
Dieses Spiel kann auf jedem Gerät gespielt werden solange es Python unterstützt.
### 5.3 Positionierung
Dieses Spiel ist ein 1/1 Klon zu dem 2018 erschienenen Spiel Bitlife. Es ist ein "Casual Game". Das Spiel ist für jede Altersgruppe fast konzipiert ausser der zu jungen Spieler da es die Option Alkohol oder Drogen zu konsumieren gibt sobald man in ein Nachtclub geht. Bei dem Spiel wird besonders auf das mehrmals durchspielen gesetzt da jeder neuer Spielversuch ein ganz neues Spielerlebnis ist.
### Risiken