from tinydb import TinyDB, Query
from cryptography.fernet import Fernet
import os, shutil

base_dir = os.path.dirname(__file__)
USERDATA_F = os.path.abspath(os.curdir)+'\\data\\userdata.json'
USERKND_F = os.path.abspath(os.curdir)+'\\data\\kdnb.bin'
BOOKLIST_F = os.path.abspath(os.curdir)+'\\data\\booklist.csv'
USERDATA_F_B = os.path.abspath(os.curdir)+'\\backup\\Backup-userdata.json'
USERKND_F_B = os.path.abspath(os.curdir)+'\\backup\\Backup-kdnb.bin'
BOOKLIST_F_B = os.path.abspath(os.curdir)+'\\backup\\Backup-booklist.csv'
DKEY_F = os.path.abspath(os.curdir)+'\\data\\mo.key'
DKEY_F_B = os.path.abspath(os.curdir)+'\\backup\\Backup-mo.key'
class UserData:
    def __init__(self):
        self.db = TinyDB(os.path.abspath(os.curdir)+'\\data\\userdata.json')
        self.User = Query()
        self.lastKdnNum = 10
        self.load_kndNum()
        if not self.user_exists("Max Mustermann"):
            self.add_test_data()

    def load_kndNum(self) -> int:
        with open(os.path.abspath(os.curdir)+'\\data\\kdnb.bin', 'rb') as f:
            num = int.from_bytes(f.read(), byteorder='big')
            self.lastKdnNum = num
            return num

    def save_kdnNum(self):
        with open(os.path.abspath(os.curdir)+'\\data\\kdnb.bin', 'wb') as f:
            f.write((self.lastKdnNum).to_bytes(24, byteorder='big', signed=False))

    def generate_kdnNum(self) -> int:
        new_kdn = self.load_kndNum()
        new_kdn += 1 
        self.lastKdnNum = new_kdn
        self.save_kdnNum()
        return new_kdn

    def add_test_data(self):
        self.add_user("1", "Max Mustermann", "muster@mustermail.de" , "01519876543", "Musterhausen", "Musterstraße 666", "11.11.2011",[])
        self.add_user("2", "Maxi Mustermann", "musterine@mustermail.de", "01519876544", "Musterhausen", "Musterstraße 666", "6.6.1966",[])

    def add_user(self, kndNum, name, email, phone, city, address, birthday, books) -> bool:
        if not self.user_exists(name):
            self.db.insert({"kndNum": kndNum, "name":name, "mail": email, "phone": phone, "city": city, "address": address, "birthday": birthday, "books": books})
            return True
        else:
            return False

    def user_exists(self, username: str) -> bool:
        for user in self.db:
            if user['name'] == username:
                return True
        return False
    
    def remove_user(self, name):
        user = Query()
        if self.user_exists(name):
            self.db.remove(user.name == name)
            #print("User " + name + " gelöscht!")
        else:
            return

    def get_userinfo(self, name) -> dict:
        for user in self.db:
            if user['name'] == name:
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
                    break

    def user_remove_book(self, kdn, isbn):
        old_books = []
        for user in self.db:
            if user['kndNum'] == kdn:
                if isbn in user['books']:
                    old_books = user['books']
                    old_books.remove(isbn)
                    self.db.update({'books': old_books} ,self.User.kndNum == kdn)
                    print("Buch von user entfernt")
                    break
    
    def user_get_books(self, knd) -> list:
        for user in self.db:
            if user['kndNum'] == knd:
                return user['books']
    
    def get_user_name(self, knd) -> str:
        for user in self.db:
            if user['kndNum'] == knd:
                return user['name']

def backup_data():
    remove_backup_data()
    if os.path.exists(USERDATA_F):
        shutil.copy2(USERDATA_F, USERDATA_F_B)
    if os.path.exists(USERKND_F):
        shutil.copy2(USERKND_F, USERKND_F_B)
        # shutil.copy2(DKEY_F, DKEY_F_B)

def get_backup_data():
    remove_data()
    if os.path.exists(USERDATA_F_B) and os.path.exists(USERKND_F_B):
        shutil.copy2(USERDATA_F_B, USERDATA_F)
        shutil.copy2(USERKND_F_B, USERKND_F)
        # shutil.copy2(DKEY_F_B, DKEY_F)
        print("Data: Userdata wiederhergestellt!")


def remove_backup_data():
    if os.path.exists(USERDATA_F_B):
        os.remove(USERDATA_F_B)
        print("Data: Backup Userdata gelöscht!")
    if os.path.exists(USERKND_F_B):
        os.remove(USERKND_F_B)
        # os.remove(DKEY_F_B)
        print("Data: Backup KND gelöscht!")


def remove_data():
    if os.path.exists(USERDATA_F):
        os.remove(USERDATA_F)
        print("Data: User-DB gelöscht!")
    if os.path.exists(USERKND_F):
        os.remove(USERKND_F)
        print("Data: KND-DB gelöscht!")
        # os.remove(DKEY_F)


  

def create_base_files():
    if os.path.exists(USERDATA_F) or os.path.exists(USERKND_F):
        print("Data: Zuerst User-DB UND KND-DB löschen!")
        return False

    if not os.path.exists(USERDATA_F):
        print("Data: Erstelle neue User-DB...")
        with open(USERDATA_F, 'w') as f:
            f.write("")
        print("Data: Neue User-DB erstellt!")
    
    if not os.path.exists(USERKND_F):
        print("Data: Erstelle neue Bücher-DB...")
        with open(USERKND_F, 'wb') as f:
            f.write((10).to_bytes(24, byteorder='big', signed=False))
        print("Data: Neue KND-DB erstellt")
    return True


