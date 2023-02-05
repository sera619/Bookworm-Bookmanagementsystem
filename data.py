from tinydb import TinyDB, Query
from cryptography.fernet import Fernet
import os, shutil

base_dir = os.path.dirname(__file__)


class UserData:
    def __init__(self):
        self.db = TinyDB(os.path.abspath(os.curdir)+'\\data\\userdata.json')
        self.User = Query()
        if not self.user_exists("Max Mustermann"):
            self.add_test_data()
        self.lastKdnNum = 0
        self.load_kndNum()

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
        self.add_user("1", "Max Mustermann", "muster@mustermail.de", "01519876543", "Musterhausen", "Musterstraße 666", "11.11.2011",[])
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
                  
    #Encryption
    def generate_key(self):
        key = Fernet.generate_key()
        with open(os.path.abspath(os.curdir)+'\\data\\mo.key', 'wb') as k:
            k.write(key)
    
    def load_key(self):
        key = None
        with open(os.path.abspath(os.curdir)+'\\data\\mo.key', 'rb') as k:
            key = k.read()
        return key

    def encrypt_file(self):
        path = os.path.abspath(os.curdir)+'\\data\\booklist.csv'
        crypt_path = os.path.abspath(os.curdir)+'\\data\\cbooklist-byte.csv'
        k = Fernet(self.load_key())
        with open(path, 'rb') as org_file:
            original = org_file.read()
        encrypt = k.encrypt(original)
        print(encrypt)
        with open(crypt_path, 'wb') as crypt_file:
            crypt_file.write(encrypt)
    
    def decrypt_file(self):
        path = os.path.abspath(os.curdir)+'\\data\\booklist.csv'
        crypt_path = os.path.abspath(os.curdir)+'\\data\\cbooklist-byte.csv'
        k = Fernet(self.load_key())

        with open(crypt_path, 'rb') as crypt_file:
            encrypt = crypt_file.read()
        
        original = k.decrypt(encrypt)
        print(original)

        with open(path, 'wb') as org_file:
            org_file.write(original)

    def backup_data(self):
        userdat = os.path.abspath(os.curdir)+'\\data\\userdata.json'
        userkey = os.path.abspath(os.curdir)+'\\data\\mo.key'
        userknd = os.path.abspath(os.curdir)+'\\data\\kdn.txt'
        shutil.copy2(userdat, os.path.abspath(os.curdir)+'\\backup\\Backup-userdata.json')
        shutil.copy2(userkey, os.path.abspath(os.curdir)+'\\backup\\backup-mo.key')
        shutil.copy2(userknd, os.path.abspath(os.curdir)+'\\backup\\backup-kdn.txt')
        print("Backup von Userdata erstellt!")

    def get_backup_data(self):
        userdat = os.path.abspath(os.curdir)+'\\data\\userdata.json'
        userkey = os.path.abspath(os.curdir)+'\\data\\mo.key'
        userknd = os.path.abspath(os.curdir)+'\\data\\kdn.txt'
        os.remove(userdat)
        os.remove(userkey)
        os.remove(userknd)
        shutil.copy2(os.path.abspath(os.curdir)+'\\backup\\Backup-userdata.json', userdat)
        shutil.copy2(os.path.abspath(os.curdir)+'\\backup\\backup-mo.key', userkey)
        shutil.copy2(os.path.abspath(os.curdir)+'\\backup\\backup-kdn.txt', userknd)
        print("Userdata wiederhergestellt!")