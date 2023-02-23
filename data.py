from tinydb import TinyDB, Query
from cryptography.fernet import Fernet
import os, shutil, logging

base_dir = os.path.dirname(__file__)

USERDATA_F = os.path.abspath(os.curdir)+'\\data\\userdata.json'
USERKND_F = os.path.abspath(os.curdir)+'\\data\\kdnb.bin'
BOOKLIST_F = os.path.abspath(os.curdir)+'\\data\\booklist.csv'
DKEY_F = os.path.abspath(os.curdir)+'\\data\\mo.key'

USERDATA_F_B = os.path.abspath(os.curdir)+'\\backup\\Backup-userdata.json'
USERKND_F_B = os.path.abspath(os.curdir)+'\\backup\\Backup-kdnb.bin'
BOOKLIST_F_B = os.path.abspath(os.curdir)+'\\backup\\Backup-booklist.csv'
DKEY_F_B = os.path.abspath(os.curdir)+'\\backup\\Backup-mo.key'

class UserData:
    def __init__(self):
        logging.info("[Data]: Initialize Userdata...")
        self.db = TinyDB(os.path.abspath(os.curdir)+'\\data\\userdata.json')
        self.lastKdnNum = 10
        self.userid_to_change = None
        self.load_kndNum()
        # if not self.user_exists("Max Mustermann"):
        #     self.add_test_data()

    def load_kndNum(self) -> int:
        with open(os.path.abspath(os.curdir)+'\\data\\kdnb.bin', 'rb') as f:
            num = int.from_bytes(f.read(), byteorder='big')
            self.lastKdnNum = num
            logging.info("[Data]: Kundennummer geladen!")
            return num

    def save_kdnNum(self):
        with open(os.path.abspath(os.curdir)+'\\data\\kdnb.bin', 'wb') as f:
            f.write((self.lastKdnNum).to_bytes(24, byteorder='big', signed=False))
        logging.info("[Data]: Kundennummer gespeichert!")

    def generate_kdnNum(self) -> int:
        new_kdn = self.load_kndNum()
        new_kdn += 1 
        self.lastKdnNum = new_kdn
        self.save_kdnNum()
        logging.info(f"[Data]: Neue Kundennummer: {new_kdn} generiert!")
        return new_kdn

    def add_test_data(self):
        self.add_user("1", "Max Mustermann", "muster@mustermail.de" , "01519876543", "99668 Musterhausen", "Musterstraße 666", "11.11.2011",[])
        self.add_user("2", "Maxi Mustermann", "musterine@mustermail.de", "01519876544", "99668 Musterhausen", "Musterstraße 666", "6.6.1966",[])

    def add_user(self, kndNum, name, email, phone, city, address, birthday, books) -> bool:
        if not self.user_exists(name):
            self.db.insert({"kndNum": kndNum, "name":name, "mail": email, "phone": phone, "city": city, "address": address, "birthday": birthday, "books": books})
            logging.info(f"[Data]: Neuer Nutzer: {name} [{kndNum}] erstellt!")
            return True
        else:
            logging.warning(f"[Data]: Neuer Nutzer konnte nicht erstellt werden!")
            return False

    def user_exists(self, username: str) -> bool:
        for user in self.db:
            if user['name'] == username:
                logging.info(f"[Data]: User {username} existiert!")
                return True
        logging.warning(f"[Data]: User {username} existiert nicht!")
        return False
    
    def remove_user(self, name):
        user = Query()
        if self.user_exists(name):
            self.db.remove(user.name == name)
            logging.warning(f"[Data]: User: {name} wurde gelöscht!")
        else:
            logging.warning(f"[Data]: User: {name} konnte nicht gelöscht werden!")
            return

    def get_userinfo(self, name) -> dict:
        for user in self.db:
            if user['name'] == name:
                logging.info(f"[Data]: Get Userinformation from: {user['name']}!")
                return user

    def user_add_book(self, kdn, isbn):
        new_list = []
        for user in self.db:
            if user['kndNum'] == kdn:
                if isbn not in user['books']:
                    new_list = user['books']
                    new_list.append(isbn)
                    self.db.update({'books': new_list} ,self.User.kndNum == kdn)
                    print("Buch zu User hinzugefügt")
                    logging.info(f"[Data]: User: {user['name']} hat Buch(ISBN): {isbn} ausgeliehen!")
                    break
                else:
                    logging.info(f"[Data]: User: {user['name']} konnte Buch(ISBN): {isbn} nicht ausleihen!")


    def user_remove_book(self, kdn, isbn):
        old_books = []
        for user in self.db:
            if user['kndNum'] == kdn:
                if isbn in user['books']:
                    old_books = user['books']
                    old_books.remove(isbn)
                    self.db.update({'books': old_books} ,self.User.kndNum == kdn)
                    print("Buch von user entfernt")
                    logging.info(f"[Data]: User: {user['name']} hat Buch(ISBN): {isbn} zurück gebracht!")
                    break
    
    def user_get_books(self, knd) -> list:
        for user in self.db:
            if user['kndNum'] == str(knd):
                logging.info(f"[Data]: Userbooklist für User: {user['name']} abgefragt!")
                return user['books']
    
    def get_user_name(self, knd) -> str:
        for user in self.db:
            if user['kndNum'] == knd:
                logging.info(f"[Data]: Username für Kundennummer: {knd} abgefragt!")
                return user['name']

    def edit_username(self, username: str, newname: str ) -> bool:
        if username == newname:
            print("[x] Username identisch, skipping.")
            logging.warning(f"[Data]: Username: {username} und {newname} identisch skipping!")
            return False
        User = Query()
        if not self.db.search(User.name == username):
            print("[x] User zum bearbeiten nicht gefunden")
            logging.warning(f"[Data]: Username: {username} zum bearbeiten nicht gefunden")
            return False
        else:
            self.db.update({'name': newname}, User.name == username)
            print(f"[!] User: {username} wurde zu {newname} geändert")
            logging.info(f"[Data]: Username: {username} wurde zu {newname} geändert")
            return True
        
    def edit_usermail(self, username: str, newvalue: str) -> bool:
        if not self.user_exists(username):
            print(f"[x] User: {username} nicht gefunden!")
            return False
        User = Query()
        changeuser = self.db.search(User.name == username)
        for i in changeuser:
            oldmail = i['mail']
        
        if oldmail == newvalue:
            print(f"[x] Mailaddresses are the same, skipping!")
            return False
        else:
            self.db.update({'mail': newvalue}, User.name == username)
            print(f"[!] Usermail from {username} changed to {newvalue}")
            return True
 
    def edit_userphone(self, username: str, newvalue: str) -> bool:
        if not self.user_exists(username):
            print(f"[x] User: {username} nicht gefunden!")
            return False
        User =  Query()
        changeuser = self.db.search(User.name == username)
        for i in changeuser:
            oldphone = i['phone']
        
        if oldphone == newvalue:
            print(f"[x] Old-Phone and New Value are the same, skipping!")
            return False
        else:
            self.db.update({'phone': newvalue}, User.name == username)
            print(f"[!] User Phone from {username} changed to {newvalue}")
            return True

    def edit_useraddress(self, username: str, newvalue: str) -> bool:
        if not self.user_exists(username):
            print(f"[x] User: {username} nicht gefunden!")
            return False
        User =  Query()
        changeuser = self.db.search(User.name == username)
        for i in changeuser:
            oldaddress = i['address']
        
        if oldaddress == newvalue:
            print(f"[x] Old-Address and New Value are the same, skipping!")
            return False
        else:
            self.db.update({'address': newvalue}, User.name == username)
            print(f"[!] User Address from {username} changed to {newvalue}")
            return True
    
    def edit_usercity(self, username: str, newvalue: str) -> bool:
        if not self.user_exists(username):
            print(f"[x] User: {username} nicht gefunden!")
            return False
        User =  Query()
        changeuser = self.db.search(User.name == username)
        for i in changeuser:
            oldaddress = i['city']
        
        if oldaddress == newvalue:
            print(f"[x] Old-City and New Value are the same, skipping!")
            return False
        else:
            self.db.update({'city': newvalue}, User.name == username)
            print(f"[!] User City from {username} changed to {newvalue}")
            return True
    
    def edit_userbirthday(self, username: str, newvalue: str) -> bool:
        if not self.user_exists(username):
            print(f"[x] User: {username} nicht gefunden!")
            return False
        User =  Query()
        changeuser = self.db.search(User.name == username)
        for i in changeuser:
            oldaddress = i['birthday']
        
        if oldaddress == newvalue:
            print(f"[x] Old-Birthday and New Value are the same, skipping!")
            return False
        else:
            self.db.update({'birthday': newvalue}, User.name == username)
            print(f"[!] User Birthday from {username} changed to {newvalue}")
            return True
    



def backup_data():
    remove_backup_data()
    if os.path.exists(USERDATA_F):
        shutil.copy2(USERDATA_F, USERDATA_F_B)
    if os.path.exists(USERKND_F):
        shutil.copy2(USERKND_F, USERKND_F_B)
    logging.info("[Data]: Backup erstellt")
 
def get_backup_data():
    remove_data()
    if os.path.exists(USERDATA_F_B) and os.path.exists(USERKND_F_B):
        shutil.copy2(USERDATA_F_B, USERDATA_F)
        shutil.copy2(USERKND_F_B, USERKND_F)
        # shutil.copy2(DKEY_F_B, DKEY_F)
        print("Data: Userdata wiederhergestellt!")
        logging.info("[Data]: Userdata wiederhergestellt!")

def remove_backup_data():
    if os.path.exists(USERDATA_F_B):
        os.remove(USERDATA_F_B)
        print("Data: Backup Userdata gelöscht!")
        logging.info("[Data]: Backup Userdata gelöscht!")
    if os.path.exists(USERKND_F_B):
        os.remove(USERKND_F_B)
        # os.remove(DKEY_F_B)
        logging.info("[Data]: Backup KND gelöscht!")
        print("Data: Backup KND gelöscht!")

def remove_data():
    if os.path.exists(USERDATA_F):
        os.remove(USERDATA_F)
        print("Data: User-DB gelöscht!")
        logging.info("[Data]: User-DB gelöscht!")
    if os.path.exists(USERKND_F):
        os.remove(USERKND_F)
        print("Data: KND-DB gelöscht!")
        logging.info("[Data]: KND-DB gelöscht!")

def create_base_files():
    if os.path.exists(USERDATA_F) or os.path.exists(USERKND_F):
        logging.warning("[Data]: Zuerst User-DB UND KND-DB löschen!")
        return False

    if not os.path.exists(USERDATA_F):
        logging.info("[Data]: Erstelle neue User-DB...")
        with open(USERDATA_F, 'w') as f:
            f.write("")
        logging.info("[Data]: Neue User-DB erstellt!")
    
    if not os.path.exists(USERKND_F):
        logging.info("[Data]: Erstelle neue Bücher-DB...")
        with open(USERKND_F, 'wb') as f:
            f.write((10).to_bytes(24, byteorder='big', signed=False))
        logging.info("[Data]: Neue KND-DB erstellt")
    return True

def backupdata_exists() -> bool:
    if os.path.exists(USERDATA_F_B):
        return True
    return False
