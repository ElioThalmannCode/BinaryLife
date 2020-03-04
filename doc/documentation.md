# BinaryLife Dokumentation
#### The Game about Live

---
###### Elio Thalmann
## 1.Wie führt man das Game aus?


#### 1.1 Installiere python3(Wenn du es noch nicht Besitzt)

##### Linux:
```bash
sudo apt install python3 #ubuntu
sudo dnf install python3 #fedora/debian
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
python3 main.py
```
## 2.Was ist die Story von diesem Spiel?
Im Grunde wird die Story des Spielers selber geschrieben anhand der Endscheidungen die der Spieler in dem Spiel getroffen hat. Es gibt kein genaues Ziel und auch kein genaues Ende es wird einfach so lange gespielt bis du stirbst oder du aufgibst.

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
Hood ist die englische Abkürzung für Nachbarschaft. Das ist der Ort andem die Person die du spielst reingeboren wird.
So sieht die hood ```class``` aus:
```python
class hood():
    def __init__(self, save, education):
        self.save   =   save
        self.education  =   education
```
### 3.3 Familie
Die Familie ist sehr wichtig in deinem Spielverlauf! Wenn du eine reiche Familie hast sind die Chancen höher das du gute Bildung und ein sicheres Leben erhälst. Es wird die gleiche ```class``` wie bei NPC verwendet.

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