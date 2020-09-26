from tkinter import *
from tkinter import messagebox
import random
import sqlite3 as sql
import os

class Uygulama(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.columnconfigure(0, weight = 1)
        self.rowconfigure(0, weight = 1)

        self.canvas = Canvas(self)
        self.canvas.grid()

        container = Frame(self.canvas)
        container.grid()

        kaydırma_y = Scrollbar(self, command = self.canvas.yview)
        kaydırma_y.grid(row = 0, column = 1, sticky = "ns")

        kaydırma_x = Scrollbar(self, orient = "horizontal", command = self.canvas.xview)
        kaydırma_x.grid(sticky = "we")

        self.canvas.configure(yscrollcommand = kaydırma_y.set)
        self.canvas.configure(xscrollcommand = kaydırma_x.set)

        self.canvas.create_window((4, 4), window = container, anchor = "nw",
                             tags = "container")
        
        container.bind("<Configure>", self.onFrameConfigure)

        self.frames = {}

        self.frames["Ana_Sayfa"] = Ana_Sayfa(parent = container, controller = self)
        self.frames["Ana_Sayfa"].grid(row = 0, column = 0, sticky = "news")

        self.frames["Öğrenci_Kayıt"] = Öğrenci_Kayıt(parent = container, controller = self)
        self.frames["Öğrenci_Kayıt"].grid(row = 0, column = 0, sticky = "news")

        self.frames["Öğrenci_Giriş"] = Öğrenci_Giriş(parent = container, controller = self)
        self.frames["Öğrenci_Giriş"].grid(row = 0, column = 0, sticky = "news")

        self.frames["Öğretmen_Giriş"] = Öğretmen_Giriş(parent = container, controller = self)
        self.frames["Öğretmen_Giriş"].grid(row = 0, column = 0, sticky = "news")

        self.frames["Öğrenci_Sayfası"] = Öğrenci_Sayfası(parent = container, controller = self)
        self.frames["Öğrenci_Sayfası"].grid(row = 0, column = 0, sticky = "news")

        self.frames["Menu1_Notlar"] = Menu1_Notlar(parent = container, controller = self)
        self.frames["Menu1_Notlar"].grid(row = 0, column = 0, sticky = "news")

        self.frames["Menu1_Devamsızlık"] = Menu1_Devamsızlık(parent = container, controller = self)
        self.frames["Menu1_Devamsızlık"].grid(row = 0, column = 0, sticky = "news")

        self.frames["Menu1_Alınan_Belgeler"] = Menu1_Alınan_Belgeler(parent = container, controller = self)
        self.frames["Menu1_Alınan_Belgeler"].grid(row = 0, column = 0, sticky = "news")

        self.frames["Menu1_Ders_Programı"] = Menu1_Ders_Programı(parent = container, controller = self)
        self.frames["Menu1_Ders_Programı"].grid(row = 0, column = 0, sticky = "news")

        self.frames["Menu1_Duyrular"] = Menu1_Duyrular(parent = container, controller = self)
        self.frames["Menu1_Duyrular"].grid(row = 0, column = 0, sticky = "news")

        self.frames["Menu1_Kulüpler"] = Menu1_Kulüpler(parent = container, controller = self)
        self.frames["Menu1_Kulüpler"].grid(row = 0, column = 0, sticky = "news")

        self.frames["Menu1_Etkinlikler"] = Menu1_Etkinlikler(parent = container, controller = self)
        self.frames["Menu1_Etkinlikler"].grid(row = 0, column = 0, sticky = "news")

        self.frames["Menu1_Mevcut_Geziler"] = Menu1_Mevcut_Geziler(parent = container, controller = self)
        self.frames["Menu1_Mevcut_Geziler"].grid(row = 0, column = 0, sticky = "news")

        self.frames["Menu1_Gezi_Ücretleri"] = Menu1_Gezi_Ücretleri(parent = container, controller = self)
        self.frames["Menu1_Gezi_Ücretleri"].grid(row = 0, column = 0, sticky = "news")

        self.frames["Menu1_Basketbol"] = Menu1_Basketbol(parent = container, controller = self)
        self.frames["Menu1_Basketbol"].grid(row = 0, column = 0, sticky = "news")

        self.frames["Menu1_Futbol"] = Menu1_Futbol(parent = container, controller = self)
        self.frames["Menu1_Futbol"].grid(row = 0, column = 0, sticky = "news")

        self.frames["Menu1_Tenis"] = Menu1_Tenis(parent = container, controller = self)
        self.frames["Menu1_Tenis"].grid(row = 0, column = 0, sticky = "news")

        self.frames["Menu1_Masa_Tenisi"] = Menu1_Masa_Tenisi(parent = container, controller = self)
        self.frames["Menu1_Masa_Tenisi"].grid(row = 0, column = 0, sticky = "news")

        self.frames["Menu1_İletişim_Bilgileri"] = Menu1_İletişim_Bilgileri(parent = container, controller = self)
        self.frames["Menu1_İletişim_Bilgileri"].grid(row = 0, column = 0, sticky = "news")

        self.frames["Menu1_Hakkında"] = Menu1_Hakkında(parent = container, controller = self)
        self.frames["Menu1_Hakkında"].grid(row = 0, column = 0, sticky = "news")
        
        self.frames["Öğretmen_Sayfası"] = Öğretmen_Sayfası(parent = container, controller = self)
        self.frames["Öğretmen_Sayfası"].grid(row = 0, column = 0, sticky = "news")

        self.frames["Menu2_9a_Not_Girişi"] = Menu2_9a_Not_Girişi(parent = container, controller = self)
        self.frames["Menu2_9a_Not_Girişi"].grid(row = 0, column = 0, sticky = "news")

        self.frames["Menu2_9a_Devamsızlık_Girişi"] = Menu2_9a_Devamsızlık_Girişi(parent = container, controller = self)
        self.frames["Menu2_9a_Devamsızlık_Girişi"].grid(row = 0, column = 0, sticky = "news")

        self.frames["Menu2_9a_Davranış_Durumu"] = Menu2_9a_Davranış_Durumu(parent = container, controller = self)
        self.frames["Menu2_9a_Davranış_Durumu"].grid(row = 0, column = 0, sticky = "news")

        self.frames["Menu2_9b_Not_Girişi"] = Menu2_9b_Not_Girişi(parent = container, controller = self)
        self.frames["Menu2_9b_Not_Girişi"].grid(row = 0, column = 0, sticky = "news")

        self.frames["Menu2_9b_Devamsızlık_Girişi"] = Menu2_9b_Devamsızlık_Girişi(parent = container, controller = self)
        self.frames["Menu2_9b_Devamsızlık_Girişi"].grid(row = 0, column = 0, sticky = "news")

        self.frames["Menu2_9b_Davranış_Durumu"] = Menu2_9b_Davranış_Durumu(parent = container, controller = self)
        self.frames["Menu2_9b_Davranış_Durumu"].grid(row = 0, column = 0, sticky = "news")

        self.frames["Menu2_9c_Not_Girişi"] = Menu2_9c_Not_Girişi(parent = container, controller = self)
        self.frames["Menu2_9c_Not_Girişi"].grid(row = 0, column = 0, sticky = "news")

        self.frames["Menu2_9c_Devamsızlık_Girişi"] = Menu2_9c_Devamsızlık_Girişi(parent = container, controller = self)
        self.frames["Menu2_9c_Devamsızlık_Girişi"].grid(row = 0, column = 0, sticky = "news")

        self.frames["Menu2_9c_Davranış_Durumu"] = Menu2_9c_Davranış_Durumu(parent = container, controller = self)
        self.frames["Menu2_9c_Davranış_Durumu"].grid(row = 0, column = 0, sticky = "news")
               
        self.show_frame("Ana_Sayfa")

    def show_frame(self, sayfa_adı):
        frame = self.frames[sayfa_adı]
        frame.tkraise()

    def onFrameConfigure(self, event = None):
        self.canvas.configure(scrollregion = self.canvas.bbox("all"))

class Ana_Sayfa(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        frame_öğrenci = Frame(self)
        frame_öğrenci.grid(row = 0, column = 0, sticky = "news")

        frame_öğretmen = Frame(self)
        frame_öğretmen.grid(row = 0, column = 1, sticky = "news")
        
        label1 = Label(frame_öğrenci, text = "ÖĞRENCİ İŞLEMLERİ")
        label1.grid(row = 0, column = 0, padx = 25)

        button1 = Button(frame_öğrenci,  text = "Kayıt", width = 10,
                         command = lambda: controller.show_frame("Öğrenci_Kayıt"))
        button1.grid(row = 1, column = 0)

        button2 = Button(frame_öğrenci, text = "Giriş", width = 10,
                         command = lambda: controller.show_frame("Öğrenci_Giriş"))
        button2.grid(row = 2, column = 0)

        label2 = Label(frame_öğretmen, text = "ÖĞRETMEN GİRİŞİ")
        label2.grid(row = 0, column = 0, padx = 60)

        button3 = Button(frame_öğretmen, text = "Giriş", width = 10,
                         command = lambda: controller.show_frame("Öğretmen_Giriş"))
        button3.grid(row = 1, column = 0)
        #pencere araçlarını self'e bağlamadık
        #çünkü zaten bir çerçeveye bağlılar ve o çerçeve de self'e bağlı
        #eğer pencere araçlarını self'e bağlarsak program hata verir
class Öğrenci_Kayıt(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        
        self.controller = controller

        self.doğrulama = self.register(self.sadece_sayı), "%S"

        label_ad = Label(self, text = "Ad: ")
        label_ad.grid(row = 0, column = 0, sticky = "e")

        self.entry_ad = Entry(self)
        self.entry_ad.grid(row = 0, column = 1, sticky = "news")

        label_soyad = Label(self, text = "Soyad: ")
        label_soyad.grid(row = 1, column = 0, sticky = "e")

        self.entry_soyad = Entry(self)
        self.entry_soyad.grid(row = 1, column = 1, sticky = "news")

        label_tc = Label(self, text = "T.C Kimlik NO: ")
        label_tc.grid(row = 2, column = 0, sticky = "e")

        self.entry_tc = Entry(self, validate = "key",
                              validatecommand = self.doğrulama)
        self.entry_tc.grid(row = 2, column = 1, sticky = "news")

        label_tel = Label(self, text = "Telefon: ")
        label_tel.grid(row = 3, column = 0, sticky = "e")

        self.entry_tel = Entry(self, validate = "key",
                               validatecommand = self.doğrulama)
        self.entry_tel.grid(row = 3, column = 1, sticky = "news")

        label_email = Label(self, text = "E-Mail: ")
        label_email.grid(row = 4, column = 0, sticky = "e")

        self.entry_email = Entry(self)
        self.entry_email.grid(row = 4, column = 1, sticky = "news")

        label_adres = Label(self, text = "Adres: ")
        label_adres.grid(row = 5, column = 0, sticky = "e")

        self.entry_adres = Entry(self)
        self.entry_adres.grid(row = 5, column = 1, sticky = "news")

        self.v = IntVar()
        self.v.set(0)

        self.checkbutton = Checkbutton(self, text = "Yukarıdaki bilgilerimi onaylıyorum", variable = self.v)
        self.checkbutton.grid(row = 6, column = 1, sticky = "news")

        button_kaydol = Button(self, text = "Kaydol",
                               command = self.kaydol2)
        button_kaydol.grid(row = 7, column = 1, sticky = "news")
        
        button = Button(self, text = "Ana Sayfa",
                        command = lambda: [controller.show_frame("Ana_Sayfa"), self.temizle()])
        button.grid(row = 8, column = 0, sticky = "w")

    def kaydol(self):
        self.mesaj = messagebox.showinfo("Hey!",
                                         "Kayıt olmak istediğinizden emin misiniz?!",
                                         type = "yesno")
        if self.mesaj == "yes":
            self.öğrenci_no()

            self.vt = sql.connect(r"C:\Users\Abdussamet\vt_öğrenci.sqlite")
            self.im = self.vt.cursor()

            self.im.execute("""SELECT "Öğrenci No" FROM ogrenci""")
            self.no = self.im.fetchall()

            while True:
                for i in self.no:
                    if i == self.detay:
                        self.öğrenci_no()
                        
                break

            self.vt.close()
            
            self.sınıflar = "ABC"
            self.sınıf = random.choice(self.sınıflar)
            self.sınıf = "9-{}".format(self.sınıf)
            
            self.vt_öğrenci()
            self.tebrik = messagebox.showinfo("Tebrikler!",
                                              "Artık bizim öğrencimizsiniz!",
                                              detail = "Öğrenci Numaranız: {}".format(self.detay),
                                              type = "ok")
            if self.tebrik == "ok":
                self.controller.show_frame("Ana_Sayfa")
                self.temizle()

        else:
            self.controller.show_frame("Ana_Sayfa")
            self.temizle()
        
    def kaydol2(self):
        self.veri1 = self.entry_ad.get()
        self.veri2 = self.entry_soyad.get()
        self.veri3 = self.entry_tc.get()
        self.veri4 = self.entry_tel.get()
        self.veri5 = self.entry_email.get()
        self.veri6 = self.entry_adres.get()

        if not self.veri1 or not self.veri2 or not self.veri3 or not self.veri4 or not self.veri5 or not self.veri6:
            self.hata = messagebox.showerror("Uyarı!",
                                             "Lütfen tüm bilgilerinizi giriniz!")
        
        elif self.v.get() == 0:
            self.uyarı = messagebox.showerror("Uyarı",
                                             "Bilgilerinizi onaylamadan kayıt olamazsınız!")

        elif len(self.veri3) != 11:
            self.uyarı2 = messagebox.showerror("Uyarı!",
                                               "TC No 11 haneli olmak zorundadır!",
                                               type = "ok")
            if self.uyarı2 == "ok":
                self.uzunluk = len(self.entry_tc.get())
                for i in range(self.uzunluk):
                    self.entry_tc.delete(0, 1)
                    
                    
        
        else:
            self.kaydol()

    def sadece_sayı(self, değer):
        if değer in "0123456789":
            return True
            
        else:
            return False

    def temizle(self):
        self.entry_ad.delete(0, "end")
        self.entry_soyad.delete(0, "end")

        for i in range(len(self.entry_tc.get())):
            self.entry_tc.delete(0, 1)
        
        for i in range(len(self.entry_tel.get())):
            self.entry_tel.delete(0, 1)
        
        self.entry_email.delete(0, "end")
        self.entry_adres.delete(0, "end")
        self.v.set(0)
        self.entry_ad.focus_set()#entry_ad'a odakladık

    def öğrenci_no(self):
        self.öğrenci_numarası = []
        for i in range(10):
            self.sayı = random.randint(0, 9)
            self.öğrenci_numarası.append(self.sayı)
            
            
        self.detay = "{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}".format(self.öğrenci_numarası[0],
                                                             self.öğrenci_numarası[1],
                                                             self.öğrenci_numarası[2],
                                                             self.öğrenci_numarası[3],
                                                             self.öğrenci_numarası[4],
                                                             self.öğrenci_numarası[5],
                                                             self.öğrenci_numarası[6],
                                                             self.öğrenci_numarası[7],
                                                             self.öğrenci_numarası[8],
                                                             self.öğrenci_numarası[9])

    def vt_öğrenci(self):
        self.dosya = r"C:\Users\Abdussamet\vt_öğrenci.sqlite"

        self.vt = sql.connect(self.dosya)
        self.im = self.vt.cursor()

        self.im.execute("""CREATE TABLE IF NOT EXISTS ogrenci
                           (Ad, Soyad, Tc, Tel, E_Mail, Adres, "Öğrenci No", Sınıf)""")

        self.veri1 = self.entry_ad.get()
        self.veri2 = self.entry_soyad.get()
        self.veri3 = self.entry_tc.get()
        self.veri4 = self.entry_tel.get()
        self.veri5 = self.entry_email.get()
        self.veri6 = self.entry_adres.get()
        self.veri7 = self.detay
        self.veri8 = self.sınıf

        self.veriler = ("{}".format(self.veri1), "{}".format(self.veri2), "{}".format(self.veri3),
                        "{}".format(self.veri4), "{}".format(self.veri5), "{}".format(self.veri6),
                        "{}".format(self.veri7), "{}".format(self.veri8))
        
        self.im.execute("""INSERT INTO ogrenci VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", self.veriler)
        self.vt.commit()

        self.vt.close()

class Öğrenci_Giriş(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        
        self.controller = controller
        self.parent = parent

        self.doğrulama = self.register(self.sadece_sayı), "%S"

        self.label_no = Label(self, text = "Öğrenci No: ")
        self.label_no.grid(row = 0, column = 0, sticky = "news")

        self.entry_no = Entry(self, validate ="key",
                              validatecommand = self.doğrulama)
        self.entry_no.grid(row = 0, column = 1, sticky = "news")

        self.label_tc = Label(self, text = "T.C Kimlik No:")
        self.label_tc.grid(row = 1, column = 0, sticky = "news")

        self.entry_tc = Entry(self, validate = "key",
                              validatecommand = self.doğrulama)
        self.entry_tc.grid(row = 1, column = 1, sticky = "news")

        self.label_sınıf = Label(self, text = "Sınıf: ")
        self.label_sınıf.grid(row = 2, column = 0, sticky = "news")

        self.entry_sınıf = Entry(self)
        self.entry_sınıf.grid(row = 2, column = 1, sticky = "news")

        self.harfler = "abcçdefgğhıijklmnoöprsştuüvyzxwqABCÇDEFGĞHIİJKLMNOÖPRESŞTUÜVYZXWQ"
        self.sayılar = "0123456789"
        self.öge1 = random.choice(self.harfler)
        self.öge2 = random.choice(self.sayılar)
        self.öge3 = random.choice(self.harfler)
        self.öge4 = random.choice(self.sayılar)
        self.öge5 = random.choice(self.harfler)
        self.öge6 = random.choice(self.sayılar)

        self.kontrol = "{0}{1}{2}{3}{4}{5}".format(self.öge1, self.öge2,
                                                   self.öge3, self.öge4,
                                                   self.öge5, self.öge6)
        
        self.label_kontrol = Label(self, text = "{}".format(self.kontrol))
        self.label_kontrol.grid(row = 3, column = 0, sticky = "news")

        #hem dış kısmına hemd de iç kısma self koyduk
        #çünkü eğer dış kısma koymazsak
        #fonksiyon entry_kontrol'ü bulamıyor çünkü
        #bu sınıfın bir nesnesi değil şeklinde uyarı veriyor
        #iç kısma vermemizin sebebi bu aracı çerçeveye bağlamak, pencereye değil
        self.entry_kontrol = Entry(self, width = 10)
        self.entry_kontrol.grid(row = 3, column = 1, sticky = "w")

        button_gir = Button(self, text = "Gir",
                            command = lambda: self.gir(), width = 8)
        button_gir.grid(row = 4, column = 1, sticky = "w")

        self.button = Button(self, text = "Ana Sayfa",
                             command = lambda: [controller.show_frame("Ana_Sayfa"), self.temizle()])
        self.button.grid()

    def gir(self):
        self.veri1 = self.entry_no.get()
        self.veri2 = self.entry_tc.get()
        self.veri3 = self.entry_sınıf.get()
        self.veri4 = self.entry_kontrol.get()

        if len(self.veri1) == 0:
            messagebox.showerror("Hata!",
                                 "Öğrenci no'ya hiçbir şey girmediniz!",
                                 detail = "Lütfen öğrenci no'nuzu giriniz!",
                                 type = "ok")

        elif len(self.veri1) != 10:
            self.mesaj1 = messagebox.showerror("Uyarı!",
                                               "Öğrenci No 10 basamaklı olmalı!",
                                               type = "ok")
            if self.mesaj1 == "ok":
                for i in range(len(self.veri1)):
                    self.entry_no.delete(0, 1)

        
        elif len(self.veri2) == 0:
            messagebox.showerror("Hata!",
                                 "Tc No'ya hiçbir şey girmediniz!",
                                 detail = "Lütfen Tc No'nuzu giriniz!",
                                 type = "ok")

        elif len(self.veri2) != 11:
            self.mesaj2 = messagebox.showerror("Uyarı!",
                                               "Tc No 11 haneli olamlı!",
                                               type = "ok")
            if self.mesaj2 == "ok":
                for i in range(len(self.veri2)):
                    self.entry_tc.delete(0, 1)

        elif not self.veri3:
            self.mesaj3 = messagebox.showerror("Uyarı",
                                               "Sınıfınızı girmediniz!",
                                               detail = "Lütfen sınıfınızı büyük harfle giriniz!",
                                               type = "ok")
            
        
        elif self.veri4 == self.kontrol:
            self.vt = sql.connect(r"C:\Users\Abdussamet\vt_öğrenci.sqlite")
            self.im = self.vt.cursor()

            self.im.execute("""SELECT Ad FROM ogrenci WHERE "Öğrenci No" = ? AND Tc = ? AND
                               Sınıf = ?""", (self.veri1, self.veri2, self.veri3))
            
            self.data = self.im.fetchone()
            self.vt.close()

            self.vt = sql.connect(r"C:\Users\Abdussamet\vt_notlar.sqlite")
            self.im = self.vt.cursor()

            self.im.execute("""SELECT "1.Sınav", "2.Sınav", "1.Sözlü", "2.Sözlü" FROM notlar_9a WHERE Öğrenciler = ? """, self.data)

            global not_verisi
            #veriyi global yaparak diğer sınıflardan da ulaşabiliriz
            
            not_verisi = self.im.fetchall()
            self.vt.close()

            Menu1_Notlar(self.parent, self.controller).veri_gir()

            if self.data:
                self.mesaj4 = messagebox.showinfo("Sisteme Hoş Geldin {}!".format(self.data),
                                                  "İstediğiniz öğrenci işlerini gerçekleştirebilirsiniz!",
                                                  type = "okcancel")
                if self.mesaj4 == "ok":
                    self.after(2000, self.controller.show_frame("Öğrenci_Sayfası"))
                    self.after(0, Öğrenci_Sayfası.new_menu(self))

                    self.temizle()
                

                else:
                    #alt satırdaki kodu yazmazsak, if'deki after'ın süresi işler
                    #yani iptale tıklasak bile iki saniye sonra sayfa açılır
                    #biz iptalde bunu yapmasını istemiyoruz
                    #bu yüzden bir daha süre belirtip bunu sıfır yaptık
                    self.after(0, self.controller.show_frame("Ana_Sayfa"))
                
                    self.temizle()
                    

            else:
                self.veri_hatası = messagebox.showerror("Uyarı",
                                                        "Girdiğiniz bilgiler uyuşmuyor!",
                                                        detail = "Lütfen bilgilerinizi doğru girdiğinizden emin olunuz!",
                                                        type = "ok")
                if self.veri_hatası == "ok":
                    for i in range(len(self.veri1)):
                        self.entry_no.delete(0, 1)

                    for j in range(len(self.veri2)):
                        self.entry_tc.delete(0, 1)
                    
                    self.entry_sınıf.delete(0, "end")
                    self.temizle_kontrol()

                    self.entry_no.focus_set()


        else:
            messagebox.showinfo("Uayrı!", "Lütfen bir daha deneyiniz!")
 
            self.temizle_kontrol()


    def sadece_sayı(self, değer):
        if değer in "0123456789":
            return True
            
        else:
            return False

    def temizle(self):
        self.temizle_kontrol()
        
        for i in range(len(self.entry_no.get())):
            self.entry_no.delete(0, 1)

        for i in range(len(self.entry_tc.get())):
            self.entry_tc.delete(0, 1)

        self.entry_sınıf.delete(0, "end")
        self.entry_no.focus_set()

    def temizle_kontrol(self):
        self.entry_kontrol.delete(0, "end")
                
        self.öge1 = random.choice(self.harfler)
        self.öge2 = random.choice(self.sayılar)
        self.öge3 = random.choice(self.harfler)
        self.öge4 = random.choice(self.sayılar)
        self.öge5 = random.choice(self.harfler)
        self.öge6 = random.choice(self.sayılar)

        self.kontrol = "{0}{1}{2}{3}{4}{5}".format(self.öge1, self.öge2,
                                                   self.öge3, self.öge4,
                                                   self.öge5, self.öge6)
                
        self.label_kontrol["text"] = "{}".format(self.kontrol)
    
class Öğretmen_Giriş(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller
        self.parent = parent

        self.doğrulama = self.register(self.sadece_sayı), "%S"

        label_tc = Label(self, text = "T.C Kimlik No: ")
        label_tc.grid(row = 0, column = 0, sticky = "news")

        self.entry_tc = Entry(self, validate = "key",
                         validatecommand = self.doğrulama)
        self.entry_tc.grid(row = 0, column = 1, sticky = "news")

        label_şifre = Label(self, text = "Şifre: ")
        label_şifre.grid(row = 1, column = 0, sticky = "news")

        self.entry_şifre = Entry(self)
        self.entry_şifre.grid(row = 1, column = 1, sticky = "news")

        button_gir = Button(self, text = "Gir", width = 10,
                            command = lambda: self.gir())
        button_gir.grid(row = 2, column = 1, sticky = "e")
        #bir command'a birden fazla görev atamak istersek köşeli parantezler arsında yazılabilir
        
        button = Button(self, text = "Ana Sayfa",
                        command = lambda: [controller.show_frame("Ana_Sayfa"), self.temizle()])
        button.grid()

        self.vt_öğretmen()

    def gir(self):
        if len(self.entry_tc.get()) == 0:
            messagebox.showerror("Hata!",
                                 "TC No'ya hiçbir şey girmediniz!",
                                  detail = "Lütfen TC No'nuzu giriniz!",
                                  type = "ok")

        elif len(self.entry_tc.get()) != 11:
            self.mesaj = messagebox.showerror("Uyarı!",
                                              "TC No 11 haneli olmalı!",
                                               type = "ok")
            if self.mesaj == "ok":
                for i in range(len(self.entry_tc.get())):
                    self.entry_tc.delete(0, 1)

        elif not self.entry_şifre.get():
            messagebox.showerror("Dikkat!",
                                 "Şifrenizi girmediniz!",
                                  detail = "Lütfen şifrenizi giriniz!",
                                  type = "ok")

        else:
            self.veri1 = self.entry_tc.get()
            self.veri2 = self.entry_şifre.get()
            
            self.vt = sql.connect(r"C:\Users\Abdussamet\vt_öğretmen.sqlite")
            self.im = self.vt.cursor()

            self.im.execute("""SELECT Ad FROM ogretmen WHERE Tc = ? AND Şifre = ?""", (self.veri1, self.veri2))
            self.data = self.im.fetchone()

            self.im.execute("""SELECT Alan FROM ogretmen WHERE Tc = ? AND  Şifre = ? """, (self.veri1, self.veri2))
            global öğretmen_alanı
            öğretmen_alanı = self.im.fetchone()

            self.vt.close()

            if self.data:
                self.mesaj2 = messagebox.showinfo("Sisteme Hoşgeldiniz Sayın {}!".format(self.data),
                                                  "Öğrencilerinizle ilgili işlemleri yapabilirsiniz!!",
                                                   type = "ok")
                if self.mesaj2 == "ok":
                    self.controller.show_frame("Öğretmen_Sayfası")
                    Öğretmen_Sayfası.new_menu(self)
                    self.temizle()

            else:
                self.mesaj3 = messagebox.showerror("Uyarı!",
                                                   "Girdiğiniz bilgiler uyuşmuyor!",
                                                    detail = "Lütfen bir daha deneyiniz!",
                                                    type = "ok")
                if self.mesaj3 == "ok":
                    self.temizle()

    def sadece_sayı(self, değer):
        if değer in "0123456789":
            return True
            
        else:
            return False

    def temizle(self):
        for i in range(len(self.entry_tc.get())):
            self.entry_tc.delete(0, 1)

        self.entry_şifre.delete(0, "end")
        self.entry_tc.focus_set()

    def vt_öğretmen(self):
        self.dosya = r"C:\Users\Abdussamet\vt_öğretmen.sqlite"
        self.dosya_mevcut = os.path.exists(self.dosya)

        self.vt = sql.connect(self.dosya)
        self.im = self.vt.cursor()

        self.im.execute("""CREATE TABLE IF NOT EXISTS ogretmen
                           (Ad, Soyad,  Tc, Alan, Şifre)""")

        self.veriler = [("Mustafa", "Han", "12345678901", "Matematik", "1234"),
                        ("Elif", "Su", "98765432109", "Fizik", "4321"),
                        ("Kerem", "Akarsu", "23456789012", "Kimya", "2341"),
                        ("Tuğçe", "Öztürk", "34567890123", "Biyoloji", "3412")]

        if not self.dosya_mevcut:
            for i in self.veriler:
                self.im.execute("""INSERT INTO ogretmen VALUES (?, ?, ?, ?, ?)""", i)

            self.vt.commit()

        self.vt.close()

class Öğrenci_Sayfası(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller
        self.parent = parent

        label = Label(self, text = "Burası Öğrenci Sayfasıdır.")
        label.grid()

        button = Button(self, text = "Ana Sayfa",
                        command = lambda: [controller.show_frame("Ana_Sayfa"), self.empty_menu()])
        button.grid()

    def new_menu(self):
        self.menu = Menu(self)
        self.controller.config(menu = self.menu)

        self.öğrenci_sayfası = Menu(self.menu, tearoff= 0)
        self.menu.add_cascade(label="Öğrenci Sayfası", menu = self.öğrenci_sayfası)
        self.öğrenci_sayfası.add_command(label = "Öğrenci Sayfası", command = lambda: self.controller.show_frame("Öğrenci_Sayfası"))
        
        self.durum = Menu(self.menu, tearoff = 0)
        self.menu.add_cascade(label = "Durum", menu = self.durum)
        self.durum.add_command(label = "Notlar", command = lambda: self.controller.show_frame("Menu1_Notlar"))
        self.durum.add_command(label = "Devamsızlık", command = lambda: self.controller.show_frame("Menu1_Devamsızlık"))
        self.durum.add_command(label = "Alınan Belgeler", command = lambda: self.controller.show_frame("Menu1_Alınan_Belgeler"))
        self.durum.add_command(label = "Ders Programı", command = lambda: self.controller.show_frame("Menu1_Ders_Programı"))
        self.durum.add_command(label = "Duyrular", command = lambda: self.controller.show_frame("Menu1_Duyrular"))

        self.yeni = Menu(self.durum, tearoff = 0)
        self.durum.add_cascade(label = "Yeni", menu = self.yeni)
        self.yeni.add_command(label = "Kulüpler", command = lambda: self.controller.show_frame("Menu1_Kulüpler"))
        self.yeni.add_command(label = "Etkinlikler", command = lambda: self.controller.show_frame("Menu1_Etkinlikler"))

        self.aktiviteler = Menu(self.menu, tearoff = 0)
        self.menu.add_cascade(label = "Aktiviteler", menu = self.aktiviteler)

        self.geziler = Menu(self.aktiviteler, tearoff = 0)
        self.aktiviteler.add_cascade(label = "Geziler", menu = self.geziler)
        self.geziler.add_command(label = "Mevcut Geziler", command = lambda: self.controller.show_frame("Menu1_Mevcut_Geziler"))
        self.geziler.add_command(label = "Gezi Ücretleri", command = lambda: self.controller.show_frame("Menu1_Gezi_Ücretleri"))

        self.spor = Menu(self.aktiviteler, tearoff = 0)
        self.aktiviteler.add_cascade(label = "Spor", menu = self.spor)
        self.spor.add_command(label = "Basketbol", command = lambda: self.controller.show_frame("Menu1_Basketbol"))
        self.spor.add_command(label = "Futbol", command = lambda: self.controller.show_frame("Menu1_Futbol"))
        self.spor.add_command(label = "Tenis", command = lambda: self.controller.show_frame("Menu1_Tenis"))
        self.spor.add_command(label = "Masa Tenisi", command = lambda: self.controller.show_frame("Menu1_Masa_Tenisi"))

        self.öğretmenler = Menu(self.menu, tearoff = 0)
        self.menu.add_cascade(label = "Öğretmenler", menu = self.öğretmenler)
        self.öğretmenler.add_command(label = "İletişim Bilgileri", command = lambda: self.controller.show_frame("Menu1_İletişim_Bilgileri"))
        self.öğretmenler.add_command(label = "Hakkında", command = lambda: self.controller.show_frame("Menu1_Hakkında"))
        
    def empty_menu(self):
        self.menu = Menu(self)
        self.controller.config(menu = self.menu)

class Menu1_Notlar(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller
        self.parent = parent

        self.label = Label(self, text = "Burası notlar sayfasıdır.")
        self.label.grid(row = 0, column = 0)

        label_dersler = Label(self, text = "Dersler")
        label_dersler.grid(row = 1, column = 0, sticky = "w")

        label_1sınav = Label(self, text = "1.Sınav")
        label_1sınav.grid(row = 1, column = 1, sticky = "w")

        label_2sınav = Label(self, text = "2.Sınav")
        label_2sınav.grid(row = 1, column = 2, sticky = "w")

        label_1sözlü = Label(self, text = "1.Sözlü")
        label_1sözlü.grid(row = 1, column = 3, sticky = "w")

        label_2sözlü = Label(self, text = "2.Sözlü")
        label_2sözlü.grid(row = 1, column = 4, sticky = "w")

        label_ort = Label(self, text = "Ortalama")
        label_ort.grid(row = 1, column = 5, sticky = "w")

        label_mat = Label(self, text = "Matematik")
        label_mat.grid(row = 2, column = 0, sticky = "w")

        label_fizik = Label(self, text = "Fizik")
        label_fizik.grid(row = 3, column = 0, sticky = "w")

        label_kimya = Label(self, text = "Kimya")
        label_kimya.grid(row = 4, column = 0, sticky = "w")

        label_bio = Label(self, text = "Biyoloji")
        label_bio.grid(row = 5, column = 0, sticky = "w")

        r = 2
        c = 1
        self.entries = [] #çok fazla sayıda entry olduğu için ve herbir entryden
        #farklı farklı veriler alabilmemiz için bir listeye attık
        while r < 6:
            for n in range(4 * 4):
                self.entries.append(Entry(self, state = "disabled"))
                self.entries[n].grid(row = r, column = c, sticky = "w")
            
                c += 1

                if c % 5 == 0:
                    c = 1
                    r += 1

        self.button = Button(self, text = "Notlarını Gör", command = self.veri_gir)
        self.button.grid(sticky = "w")

    def veri_gir(self):
        n = 0
        a = 0
        while True:
            for i in not_verisi[a]:
                self.entries[n]["state"] = "normal"
                self.entries[n].insert(0, i)
                self.entries[n]["state"] = "disabled"
                n += 1
    
                if n % 4 == 0:
                    a += 1
                
                else:
                    continue
                
            if a == 4:
                break
            

class Menu1_Devamsızlık(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        label = Label(self, text = "Burası devamsızlık sayfasıdır.")
        label.grid(row = 0, column = 0)

        label1 = Label(self, text = "Raporlu")
        label1.grid(row = 1, column = 0, sticky = "w")

        label2 = Label(self, text = "Raporsuz")
        label2.grid(row = 1, column =1, sticky = "w")

        entry1 = Entry(self, state = "disabled")
        entry1.grid(row = 2, column = 0, sticky = "w")

        entry2 = Entry(self, state = "disabled")
        entry2.grid(row = 2, column = 1, sticky = "w")

class Menu1_Alınan_Belgeler(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        label = Label(self, text = "Burası alınan belgeler sayfasıdır.")
        label.grid()

        

class Menu1_Ders_Programı(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        label = Label(self, text = "Burası ders programı sayfasıdır")
        label.grid()

class Menu1_Duyrular(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        label = Label(self, text = "Burası duyrular sayfasıdır.")
        label.grid()

class Menu1_Kulüpler(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        label = Label(self, text = "Burası kulüpler sayfasıdır.")
        label.grid()

class Menu1_Etkinlikler(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        label = Label(self, text = "Burası etkinlik sayfasıdır.")
        label.grid()

class Menu1_Mevcut_Geziler(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        label = Label(self, text = "Burası geziler sayfasıdır")
        label.grid()

class Menu1_Gezi_Ücretleri(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        label = Label(self, text = "Burası gezi ücretleri sayfasıdır.")
        label.grid()

class Menu1_Basketbol(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        label = Label(self, text = "Burası basketbol sayfasıdır.")
        label.grid()

class Menu1_Futbol(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        label = Label(self, text = "Burası Futbol sayfasıdır")
        label.grid()

class Menu1_Tenis(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        label = Label(self, text = "Burası tenis sayfasıdır.")
        label.grid()

class Menu1_Masa_Tenisi(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        label = Label(self, text = "Burası masa tenisi sayfasıdır.")
        label.grid()

class Menu1_İletişim_Bilgileri(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        label = Label(self, text = "Burası iletişim bilgileri sayfasıdır.")
        label.grid()

class Menu1_Hakkında(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        label = Label(self, text = "Burası hakkında sayfasıdır.")
        label.grid()

class Öğretmen_Sayfası(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        label = Label(self, text = "Burası Öğretmen Sayfasıdır")
        label.grid(row = 0, column = 0)

        button = Button(self, text = "Ana Sayfa",
                        command = lambda: [controller.show_frame("Ana_Sayfa"), self.empty_menu()])
        button.grid()

    def new_menu(self):
        self.menu = Menu(self)
        self.controller.config(menu = self.menu)

        self.öğretmen_sayfası = Menu(self.menu, tearoff = 0)
        self.menu.add_cascade(label = "Öğretmen Sayfası", menu = self.öğretmen_sayfası)
        self.öğretmen_sayfası.add_command(label = "Öğretmen Sayfası", command = lambda: self.controller.show_frame("Öğretmen_Sayfası"))

        self.sınıflar = Menu(self.menu, tearoff = 0)
        self.menu.add_cascade(label = "Sınıflar", menu = self.sınıflar)

        self._9a = Menu(self.sınıflar, tearoff = 0)
        self.sınıflar.add_cascade(label = "9-A", menu = self._9a)
        self._9a.add_command(label = "Not Girişi", command = lambda: self.controller.show_frame("Menu2_9a_Not_Girişi"))
        self._9a.add_command(label = "Devamsızlık Girişi", command = lambda: self.controller.show_frame("Menu2_9a_Devamsızlık_Girişi"))
        self._9a.add_command(label = "Davranış Durumu", command = lambda: self.controller.show_frame("Menu2_9a_Davranış_Durumu"))

        self._9b = Menu(self.sınıflar, tearoff = 0)
        self.sınıflar.add_cascade(label = "9-B", menu = self._9b)
        self._9b.add_command(label = "Not Girişi", command = lambda: self.controller.show_frame("Menu2_9b_Not_Girişi"))
        self._9b.add_command(label = "Devamsızlık Girişi", command = lambda: self.controller.show_frame("Menu2_9b_Devamsızlık_Girişi"))
        self._9b.add_command(label = "Davranış Durumu", command = lambda: self.controller.show_frame("Menu2_9b_Davranış_Durumu"))

        self._9c = Menu(self.sınıflar, tearoff = 0)
        self.sınıflar.add_cascade(label = "9-C", menu = self._9c)
        self._9c.add_command(label = "Not Girişi", command = lambda: self.controller.show_frame("Menu2_9c_Not_Girişi"))
        self._9c.add_command(label = "Devamsızlık Girişi", command = lambda: self.controller.show_frame("Menu2_9c_Devamsızlık_Girişi"))
        self._9c.add_command(label = "Davranış Durumu", command = lambda: self.controller.show_frame("Menu2_9c_Davranış_Durumu"))

    def empty_menu(self):
        self.menu = Menu(self)
        self.controller.config(menu = self.menu)

class Menu2_9a_Not_Girişi(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        label = Label(self, text = "Burası 9a not girişi sayfasıdır.")
        label.grid()

        self.vt = sql.connect(r"C:\Users\Abdussamet\vt_öğrenci.sqlite")
        self.im = self.vt.cursor()

        self.im.execute("""SELECT Ad FROM ogrenci WHERE Sınıf = "9-A" """)
        self.ad = self.im.fetchall()

        label1 = Label(self, text= "Öğrenciler")
        label1.grid(row = 1, column = 0, sticky = "w")

        label2 = Label(self, text = "1.Sınav")
        label2.grid(row = 1, column = 1, sticky = "w")

        label3 = Label(self, text = "2.Sınav")
        label3.grid(row = 1, column = 2, sticky = "w")

        label4 = Label(self, text = "1.Sözlü")
        label4.grid(row = 1, column = 3, sticky = "w")

        label5 = Label(self, text = "2.Sözlü")
        label5.grid(row = 1, column = 4, sticky = "w")

        label6 = Label(self, text = "Ortalama")
        label6.grid(row = 1, column = 5, sticky = "w")


        r = 2
        c = 0

        while r < len(self.ad) + 1:
            for i in self.ad:
                i = str(i)
                i = i[2:-3]
                Label(self, text = "{}".format(i)).grid(row = r, column = c,
                                                        sticky = "w")
                r += 1
            break

        r = 2
        c = 1
        self.entries = [] #çok fazla sayıda entry olduğu için ve herbir entryden
        #farklı farklı veriler alabilmemiz için bir listeye attık
        while r < len(self.ad) + 2:
            for n in range(len(self.ad) * 4):
                self.entries.append(Entry(self))
                self.entries[n].grid(row = r, column = c, sticky = "w")
            
                c += 1

                if c % 5 == 0:
                    c = 1
                    r += 1

        #label_ort1 = Label(self, text = "{}".format())
        #label_ort1.grid(row = 3, column = 5, sticky = "w")

        #label_ort2 = Label(self, text = "{}".format())
        #label_ort2.grid(row = 4, column = 5, sticky = "w")
        
        #label_ort3 = Label(self, text = "{}".format())
        #label_ort3.grid(row = 5, column = 5, sticky = "w")

        button = Button(self, text = "Uygula",
                        command = self.vt_notlar)
        button.grid()

    def vt_notlar(self):
        self.vt = sql.connect(r"C:\Users\Abdussamet\vt_notlar.sqlite")
        self.im = self.vt.cursor()

        self.im.execute("""CREATE TABLE IF NOT EXISTS notlar_9a
                           (Öğrenciler ,"1.Sınav", "2.Sınav", "1.Sözlü", "2.Sözlü", "Alan")""")

        self.im.execute("""SELECT * FROM notlar_9a""")
        self.veri = self.im.fetchone()

        self.im.execute("""SELECT Alan FROM notlar_9a""")
        self.alanlar = self.im.fetchall()

        if not self.veri:
            n = 0
            for i in range(len(self.ad)):
                self.data1 = self.ad[i]
                self.data1 = str(self.data1)
                self.data1 = self.data1[2:-3]
                self.data2 = self.entries[n].get()
                self.data3 = self.entries[n + 1].get()
                self.data4 = self.entries[n + 2].get()
                self.data5 = self.entries[n + 3].get()
                self.data6 = öğretmen_alanı
                self.data6 = str(self.data6)
                self.data6 = self.data6[2:-3]

            
                self.datas = ("{}".format(self.data1), "{}".format(self.data2), "{}".format(self.data3),
                              "{}".format(self.data4), "{}".format(self.data5), "{}".format(self.data6))
           
                self.im.execute("""INSERT INTO notlar_9a VALUES (?, ?, ?, ?, ?, ?)""", self.datas)
                self.vt.commit()

                n += 4#çünkü veri tabanında 4 tanesütun var
            
        elif öğretmen_alanı in self.alanlar:
            self.güncelle()
        else:
            n = 0
            for a in range(len(self.ad)):
                self.data1 = self.ad[a]
                self.data1 = str(self.data1)
                self.data1 = self.data1[2:-3]
                self.data2 = self.entries[n].get()
                self.data3 = self.entries[n + 1].get()
                self.data4 = self.entries[n + 2].get()
                self.data5 = self.entries[n + 3].get()
                self.data6 = öğretmen_alanı
                self.data6 = str(self.data6)
                self.data6 = self.data6[2:-3]
                    
                self.datas = ("{}".format(self.data1), "{}".format(self.data2), "{}".format(self.data3),
                              "{}".format(self.data4), "{}".format(self.data5), "{}".format(self.data6))
                    
                self.im.execute("""INSERT INTO notlar_9a VALUES (?, ?, ?, ?, ?, ?)""", self.datas)
                self.vt.commit()

                n += 4

        self.vt.close()

    def güncelle(self):
        self.vt = sql.connect(r"C:\Users\Abdussamet\vt_notlar.sqlite")
        self.im = self.vt.cursor()

        n = 0
        for i in range(len(self.ad)):
            self.data1 = self.ad[i]
            self.data1 = str(self.data1)
            self.data1 = self.data1[2:-3]
            self.data2 = self.entries[n].get()
            self.data3 = self.entries[n + 1].get()
            self.data4 = self.entries[n + 2].get()
            self.data5 = self.entries[n + 3].get()
            self.data6 = öğretmen_alanı
            self.data6 = str(self.data6)
            self.data6 = self.data6[2:-3]

            self.im.execute("""UPDATE notlar_9a SET "1.Sınav" = ?, "2.Sınav" = ?, "1.Sözlü" = ?, "2.Sözlü" = ?
                               WHERE Öğrenciler = ? AND Alan = ?""", (str(self.data2), str(self.data3), str(self.data4), str(self.data5), str(self.data1), str(self.data6)))
            self.vt.commit()

            n += 4
        
        self.vt.close()

class Menu2_9a_Devamsızlık_Girişi(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        label = Label(self, text = "Burası 9a devamsızlık girişi sayfasıdır")
        label.grid()

class Menu2_9a_Davranış_Durumu(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        label = Label(self, text = "Burası 9a davranış durumu sayfasıdır.")
        label.grid()

class Menu2_9b_Not_Girişi(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        label = Label(self, text = "Burası 9b not girişi sayfasıdır.")
        label.grid()

class Menu2_9b_Devamsızlık_Girişi(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        label = Label(self, text = "Burası 9b devamsızlık girişi sayfasıdır")
        label.grid()

class Menu2_9b_Davranış_Durumu(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        label = Label(self, text = "Burası 9b davranış durumu sayfasıdır.")
        label.grid()


class Menu2_9c_Not_Girişi(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        label = Label(self, text = "Burası 9c not girişi sayfasıdır.")
        label.grid()

class Menu2_9c_Devamsızlık_Girişi(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        label = Label(self, text = "Burası 9c devamsızlık girişi sayfasıdır")
        label.grid()

class Menu2_9c_Davranış_Durumu(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        label = Label(self, text = "Burası 9c davranış durumu sayfasıdır.")
        label.grid()
    
if __name__ == "__main__":#uygulama çalıştığında nesneyi oluşturacak
    uygulama = Uygulama()
    mainloop()
#bazı yerlerde self'leri içte yazdık çünkü bir pencerede sayfa depiştirmek
#istersek her bir sayfayı ayrı bir sınıf olarak adlandırmalıyız
#ve pencere araçlarını Frame'i miras olarak aldığımız
#sınıflardaki çerçevelere(sayfalara) bağlamalıyız
