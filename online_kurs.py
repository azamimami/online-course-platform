import sys
from datetime import datetime
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QFont, QPalette, QColor

# ===================== VERİ SINIFLARI =====================
class Egitmen:
    def __init__(self, id, ad, soyad, uzmanlik, telefon="", email=""):
        self.id = id
        self.ad = ad
        self.soyad = soyad
        self.uzmanlik = uzmanlik
        self.telefon = telefon
        self.email = email
        self.tarih = datetime.now().strftime("%d.%m.%Y")

class Ogrenci:
    def __init__(self, id, ad, soyad, email, telefon=""):
        self.id = id
        self.ad = ad
        self.soyad = soyad
        self.email = email
        self.telefon = telefon
        self.tarih = datetime.now().strftime("%d.%m.%Y")

class Kurs:
    def __init__(self, id, ad, egitmen_id, egitmen_adi, kontenjan, fiyat, aciklama=""):
        self.id = id
        self.ad = ad
        self.egitmen_id = egitmen_id
        self.egitmen_adi = egitmen_adi
        self.kontenjan = kontenjan
        self.fiyat = fiyat
        self.aciklama = aciklama
        self.ogrenciler = []
        self.tarih = datetime.now().strftime("%d.%m.%Y")


# ===================== ANA PENCERE =====================
class KursPlatformu(QMainWindow):
    def __init__(self):
        super().__init__()

        # Veriler
        self.egitmenler = []
        self.ogrenciler = []
        self.kurslar = []

        self.egitmen_id = 1
        self.ogrenci_id = 1
        self.kurs_id = 1

        # Örnek veriler
        self.ornek_veri_ekle()

        self.setWindowTitle("📚 Online Kurs Platformu")
        self.setGeometry(100, 100, 1300, 800)

        # Stil
        self.setStyleSheet("""
            QMainWindow {
                background-color: #1e1e2e;
            }
            QTabWidget::pane {
                background-color: #2d2d3d;
                border-radius: 10px;
            }
            QTabBar::tab {
                background-color: #3d3d4d;
                color: white;
                padding: 10px 20px;
                margin: 5px;
                border-radius: 8px;
            }
            QTabBar::tab:selected {
                background-color: #5b5bff;
            }
            QTableWidget {
                background-color: #2d2d3d;
                color: #ffffff;
                gridline-color: #3d3d4d;
                border-radius: 8px;
            }
            QHeaderView::section {
                background-color: #5b5bff;
                color: white;
                padding: 8px;
                font-weight: bold;
            }
            QPushButton {
                background-color: #5b5bff;
                color: white;
                border: none;
                padding: 10px;
                border-radius: 8px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #7b7bff;
            }
            QPushButton:red {
                background-color: #ff5b5b;
            }
            QPushButton:red:hover {
                background-color: #ff7b7b;
            }
            QLineEdit, QTextEdit, QComboBox, QSpinBox, QDoubleSpinBox {
                background-color: #3d3d4d;
                color: white;
                border: 1px solid #5b5bff;
                border-radius: 6px;
                padding: 8px;
            }
            QLabel {
                color: #ffffff;
            }
            QGroupBox {
                color: #5b5bff;
                font-weight: bold;
                border: 2px solid #5b5bff;
                border-radius: 10px;
                margin-top: 10px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px 0 5px;
            }
        """)

        self.ui()

    def ornek_veri_ekle(self):
        # Eğitmenler
        e1 = Egitmen(self.egitmen_id, "Ahmet", "Yılmaz", "Python Programlama", "555-123-4567", "ahmet@kurs.com")
        self.egitmenler.append(e1)
        self.egitmen_id += 1

        e2 = Egitmen(self.egitmen_id, "Mehmet", "Demir", "Web Geliştirme", "555-234-5678", "mehmet@kurs.com")
        self.egitmenler.append(e2)
        self.egitmen_id += 1

        e3 = Egitmen(self.egitmen_id, "Ayşe", "Kaya", "Veri Bilimi", "555-345-6789", "ayse@kurs.com")
        self.egitmenler.append(e3)
        self.egitmen_id += 1

        # Öğrenciler
        o1 = Ogrenci(self.ogrenci_id, "Ali", "Veli", "ali@email.com", "555-456-7890")
        self.ogrenciler.append(o1)
        self.ogrenci_id += 1

        o2 = Ogrenci(self.ogrenci_id, "Zeynep", "Demir", "zeynep@email.com", "555-567-8901")
        self.ogrenciler.append(o2)
        self.ogrenci_id += 1

        # Kurslar
        k1 = Kurs(self.kurs_id, "Python ile Programlama", 1, "Ahmet Yılmaz", 30, 1500, "Sıfırdan ileri seviye Python")
        self.kurslar.append(k1)
        self.kurs_id += 1

        k2 = Kurs(self.kurs_id, "Web Tasarımı", 2, "Mehmet Demir", 25, 1200, "HTML, CSS, JavaScript")
        self.kurslar.append(k2)
        self.kurs_id += 1

        k3 = Kurs(self.kurs_id, "Veri Analizi", 3, "Ayşe Kaya", 20, 1800, "Pandas, NumPy, Matplotlib")
        self.kurslar.append(k3)
        self.kurs_id += 1

        # Öğrenci kayıtları
        self.kurslar[0].ogrenciler.append(o1)
        self.kurslar[1].ogrenciler.append(o2)

    def ui(self):
        # Merkezi widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Ana layout
        main_layout = QVBoxLayout(central_widget)

        # Başlık
        baslik = QLabel("📚 ONLINE KURS PLATFORMU")
        baslik.setAlignment(Qt.AlignCenter)
        baslik.setStyleSheet("font-size: 28px; font-weight: bold; color: #5b5bff; padding: 20px;")
        main_layout.addWidget(baslik)

        # Tab widget
        tabs = QTabWidget()

        # Sekmeleri ekle
        tabs.addTab(self.egitmen_tab(), "👨‍🏫 Eğitmenler")
        tabs.addTab(self.ogrenci_tab(), "👨‍🎓 Öğrenciler")
        tabs.addTab(self.kurs_tab(), "📚 Kurslar")
        tabs.addTab(self.kayit_tab(), "📝 Kursa Kayıt")
        tabs.addTab(self.istatistik_tab(), "📊 İstatistikler")

        main_layout.addWidget(tabs)

    # ===================== EGİTMEN SEKMESİ =====================
    def egitmen_tab(self):
        widget = QWidget()
        layout = QHBoxLayout(widget)

        # Sol panel - Form
        sol_panel = QFrame()
        sol_panel.setStyleSheet("background-color: #2d2d3d; border-radius: 10px;")
        sol_layout = QVBoxLayout(sol_panel)

        form_baslik = QLabel("Yeni Eğitmen Ekle")
        form_baslik.setStyleSheet("font-size: 18px; font-weight: bold; color: #5b5bff;")
        sol_layout.addWidget(form_baslik)

        self.egitmen_ad = QLineEdit()
        self.egitmen_ad.setPlaceholderText("Ad")
        sol_layout.addWidget(self.egitmen_ad)

        self.egitmen_soyad = QLineEdit()
        self.egitmen_soyad.setPlaceholderText("Soyad")
        sol_layout.addWidget(self.egitmen_soyad)

        self.egitmen_uzmanlik = QLineEdit()
        self.egitmen_uzmanlik.setPlaceholderText("Uzmanlık")
        sol_layout.addWidget(self.egitmen_uzmanlik)

        self.egitmen_tel = QLineEdit()
        self.egitmen_tel.setPlaceholderText("Telefon")
        sol_layout.addWidget(self.egitmen_tel)

        self.egitmen_email = QLineEdit()
        self.egitmen_email.setPlaceholderText("Email")
        sol_layout.addWidget(self.egitmen_email)

        btn_ekle = QPushButton("➕ Eğitmen Ekle")
        btn_ekle.clicked.connect(self.egitmen_ekle)
        sol_layout.addWidget(btn_ekle)

        btn_sil = QPushButton("🗑 Seçili Eğitmeni Sil")
        btn_sil.setStyleSheet("background-color: #ff5b5b;")
        btn_sil.clicked.connect(self.egitmen_sil)
        sol_layout.addWidget(btn_sil)

        sol_layout.addStretch()

        # Sağ panel - Tablo
        self.egitmen_tablo = QTableWidget()
        self.egitmen_tablo.setColumnCount(6)
        self.egitmen_tablo.setHorizontalHeaderLabels(["ID", "Ad", "Soyad", "Uzmanlık", "Telefon", "Email"])
        self.egitmen_tablo.setSelectionBehavior(QTableWidget.SelectRows)
        self.egitmen_tablo.horizontalHeader().setStretchLastSection(True)

        layout.addWidget(sol_panel, 1)
        layout.addWidget(self.egitmen_tablo, 2)

        self.egitmen_listele()

        return widget

    def egitmen_ekle(self):
        if not self.egitmen_ad.text() or not self.egitmen_soyad.text():
            QMessageBox.warning(self, "Uyarı", "Ad ve Soyad girmelisiniz!")
            return

        e = Egitmen(
            self.egitmen_id,
            self.egitmen_ad.text(),
            self.egitmen_soyad.text(),
            self.egitmen_uzmanlik.text(),
            self.egitmen_tel.text(),
            self.egitmen_email.text()
        )
        self.egitmenler.append(e)
        self.egitmen_id += 1

        self.egitmen_ad.clear()
        self.egitmen_soyad.clear()
        self.egitmen_uzmanlik.clear()
        self.egitmen_tel.clear()
        self.egitmen_email.clear()

        self.egitmen_listele()
        QMessageBox.information(self, "Başarılı", "Eğitmen eklendi!")

    def egitmen_listele(self):
        self.egitmen_tablo.setRowCount(0)
        for e in self.egitmenler:
            row = self.egitmen_tablo.rowCount()
            self.egitmen_tablo.insertRow(row)
            self.egitmen_tablo.setItem(row, 0, QTableWidgetItem(str(e.id)))
            self.egitmen_tablo.setItem(row, 1, QTableWidgetItem(e.ad))
            self.egitmen_tablo.setItem(row, 2, QTableWidgetItem(e.soyad))
            self.egitmen_tablo.setItem(row, 3, QTableWidgetItem(e.uzmanlik))
            self.egitmen_tablo.setItem(row, 4, QTableWidgetItem(e.telefon))
            self.egitmen_tablo.setItem(row, 5, QTableWidgetItem(e.email))

    def egitmen_sil(self):
        row = self.egitmen_tablo.currentRow()
        if row < 0:
            QMessageBox.warning(self, "Uyarı", "Silmek için bir eğitmen seçin!")
            return

        eid = int(self.egitmen_tablo.item(row, 0).text())

        # Eğitmenin kursları var mı kontrol et
        for kurs in self.kurslar:
            if kurs.egitmen_id == eid:
                QMessageBox.warning(self, "Uyarı", "Bu eğitmenin kursları var! Önce kursları silin.")
                return

        for e in self.egitmenler:
            if e.id == eid:
                self.egitmenler.remove(e)
                break

        self.egitmen_listele()
        QMessageBox.information(self, "Başarılı", "Eğitmen silindi!")

    # ===================== ÖĞRENCİ SEKMESİ =====================
    def ogrenci_tab(self):
        widget = QWidget()
        layout = QHBoxLayout(widget)

        # Sol panel
        sol_panel = QFrame()
        sol_panel.setStyleSheet("background-color: #2d2d3d; border-radius: 10px;")
        sol_layout = QVBoxLayout(sol_panel)

        form_baslik = QLabel("Yeni Öğrenci Ekle")
        form_baslik.setStyleSheet("font-size: 18px; font-weight: bold; color: #5b5bff;")
        sol_layout.addWidget(form_baslik)

        self.ogrenci_ad = QLineEdit()
        self.ogrenci_ad.setPlaceholderText("Ad")
        sol_layout.addWidget(self.ogrenci_ad)

        self.ogrenci_soyad = QLineEdit()
        self.ogrenci_soyad.setPlaceholderText("Soyad")
        sol_layout.addWidget(self.ogrenci_soyad)

        self.ogrenci_email = QLineEdit()
        self.ogrenci_email.setPlaceholderText("Email")
        sol_layout.addWidget(self.ogrenci_email)

        self.ogrenci_tel = QLineEdit()
        self.ogrenci_tel.setPlaceholderText("Telefon")
        sol_layout.addWidget(self.ogrenci_tel)

        btn_ekle = QPushButton("➕ Öğrenci Ekle")
        btn_ekle.clicked.connect(self.ogrenci_ekle)
        sol_layout.addWidget(btn_ekle)

        btn_sil = QPushButton("🗑 Seçili Öğrenciyi Sil")
        btn_sil.setStyleSheet("background-color: #ff5b5b;")
        btn_sil.clicked.connect(self.ogrenci_sil)
        sol_layout.addWidget(btn_sil)

        sol_layout.addStretch()

        # Sağ panel
        self.ogrenci_tablo = QTableWidget()
        self.ogrenci_tablo.setColumnCount(5)
        self.ogrenci_tablo.setHorizontalHeaderLabels(["ID", "Ad", "Soyad", "Email", "Telefon"])
        self.ogrenci_tablo.setSelectionBehavior(QTableWidget.SelectRows)
        self.ogrenci_tablo.horizontalHeader().setStretchLastSection(True)

        layout.addWidget(sol_panel, 1)
        layout.addWidget(self.ogrenci_tablo, 2)

        self.ogrenci_listele()

        return widget

    def ogrenci_ekle(self):
        if not self.ogrenci_ad.text() or not self.ogrenci_soyad.text():
            QMessageBox.warning(self, "Uyarı", "Ad ve Soyad girmelisiniz!")
            return

        o = Ogrenci(
            self.ogrenci_id,
            self.ogrenci_ad.text(),
            self.ogrenci_soyad.text(),
            self.ogrenci_email.text(),
            self.ogrenci_tel.text()
        )
        self.ogrenciler.append(o)
        self.ogrenci_id += 1

        self.ogrenci_ad.clear()
        self.ogrenci_soyad.clear()
        self.ogrenci_email.clear()
        self.ogrenci_tel.clear()

        self.ogrenci_listele()
        QMessageBox.information(self, "Başarılı", "Öğrenci eklendi!")

    def ogrenci_listele(self):
        self.ogrenci_tablo.setRowCount(0)
        for o in self.ogrenciler:
            row = self.ogrenci_tablo.rowCount()
            self.ogrenci_tablo.insertRow(row)
            self.ogrenci_tablo.setItem(row, 0, QTableWidgetItem(str(o.id)))
            self.ogrenci_tablo.setItem(row, 1, QTableWidgetItem(o.ad))
            self.ogrenci_tablo.setItem(row, 2, QTableWidgetItem(o.soyad))
            self.ogrenci_tablo.setItem(row, 3, QTableWidgetItem(o.email))
            self.ogrenci_tablo.setItem(row, 4, QTableWidgetItem(o.telefon))

    def ogrenci_sil(self):
        row = self.ogrenci_tablo.currentRow()
        if row < 0:
            QMessageBox.warning(self, "Uyarı", "Silmek için bir öğrenci seçin!")
            return

        oid = int(self.ogrenci_tablo.item(row, 0).text())

        # Öğrenciyi kurslardan sil
        for kurs in self.kurslar:
            for o in kurs.ogrenciler[:]:
                if o.id == oid:
                    kurs.ogrenciler.remove(o)

        for o in self.ogrenciler:
            if o.id == oid:
                self.ogrenciler.remove(o)
                break

        self.ogrenci_listele()
        self.kurs_listele()
        QMessageBox.information(self, "Başarılı", "Öğrenci silindi!")

    # ===================== KURS SEKMESİ =====================
    def kurs_tab(self):
        widget = QWidget()
        layout = QHBoxLayout(widget)

        # Sol panel
        sol_panel = QFrame()
        sol_panel.setStyleSheet("background-color: #2d2d3d; border-radius: 10px;")
        sol_layout = QVBoxLayout(sol_panel)

        form_baslik = QLabel("Yeni Kurs Ekle")
        form_baslik.setStyleSheet("font-size: 18px; font-weight: bold; color: #5b5bff;")
        sol_layout.addWidget(form_baslik)

        self.kurs_ad = QLineEdit()
        self.kurs_ad.setPlaceholderText("Kurs Adı")
        sol_layout.addWidget(self.kurs_ad)

        self.kurs_egitmen = QComboBox()
        self.kurs_egitmen.setPlaceholderText("Eğitmen Seç")
        sol_layout.addWidget(self.kurs_egitmen)

        self.kurs_kontenjan = QSpinBox()
        self.kurs_kontenjan.setRange(1, 200)
        self.kurs_kontenjan.setPrefix("📊 ")
        sol_layout.addWidget(self.kurs_kontenjan)

        self.kurs_fiyat = QDoubleSpinBox()
        self.kurs_fiyat.setRange(0, 100000)
        self.kurs_fiyat.setPrefix("💰 ₺")
        sol_layout.addWidget(self.kurs_fiyat)

        self.kurs_aciklama = QTextEdit()
        self.kurs_aciklama.setPlaceholderText("Kurs Açıklaması")
        self.kurs_aciklama.setMaximumHeight(100)
        sol_layout.addWidget(self.kurs_aciklama)

        btn_ekle = QPushButton("➕ Kurs Ekle")
        btn_ekle.clicked.connect(self.kurs_ekle)
        sol_layout.addWidget(btn_ekle)

        btn_sil = QPushButton("🗑 Seçili Kursu Sil")
        btn_sil.setStyleSheet("background-color: #ff5b5b;")
        btn_sil.clicked.connect(self.kurs_sil)
        sol_layout.addWidget(btn_sil)

        sol_layout.addStretch()

        # Sağ panel
        self.kurs_tablo = QTableWidget()
        self.kurs_tablo.setColumnCount(7)
        self.kurs_tablo.setHorizontalHeaderLabels(["ID", "Kurs Adı", "Eğitmen", "Kontenjan", "Kayıtlı", "Fiyat", "Durum"])
        self.kurs_tablo.setSelectionBehavior(QTableWidget.SelectRows)
        self.kurs_tablo.horizontalHeader().setStretchLastSection(True)

        layout.addWidget(sol_panel, 1)
        layout.addWidget(self.kurs_tablo, 2)

        self.egitmen_combo_guncelle()
        self.kurs_listele()

        return widget

    def egitmen_combo_guncelle(self):
        self.kurs_egitmen.clear()
        for e in self.egitmenler:
            self.kurs_egitmen.addItem(f"{e.ad} {e.soyad} ({e.uzmanlik})", e.id)

    def kurs_ekle(self):
        if not self.kurs_ad.text():
            QMessageBox.warning(self, "Uyarı", "Kurs adı girmelisiniz!")
            return

        if self.kurs_egitmen.count() == 0:
            QMessageBox.warning(self, "Uyarı", "Önce eğitmen eklemelisiniz!")
            return

        egitmen_id = self.kurs_egitmen.currentData()
        egitmen_adi = self.kurs_egitmen.currentText()

        k = Kurs(
            self.kurs_id,
            self.kurs_ad.text(),
            egitmen_id,
            egitmen_adi,
            self.kurs_kontenjan.value(),
            self.kurs_fiyat.value(),
            self.kurs_aciklama.toPlainText()
        )
        self.kurslar.append(k)
        self.kurs_id += 1

        self.kurs_ad.clear()
        self.kurs_kontenjan.setValue(20)
        self.kurs_fiyat.setValue(0)
        self.kurs_aciklama.clear()

        self.kurs_listele()
        QMessageBox.information(self, "Başarılı", "Kurs eklendi!")

    def kurs_listele(self):
        self.kurs_tablo.setRowCount(0)
        for k in self.kurslar:
            row = self.kurs_tablo.rowCount()
            self.kurs_tablo.insertRow(row)

            doluluk = len(k.ogrenciler)
            durum = "🟢 AÇIK" if doluluk < k.kontenjan else "🔴 DOLU"
            if doluluk >= k.kontenjan * 0.8:
                durum = "🟡 NORMAL"

            self.kurs_tablo.setItem(row, 0, QTableWidgetItem(str(k.id)))
            self.kurs_tablo.setItem(row, 1, QTableWidgetItem(k.ad))
            self.kurs_tablo.setItem(row, 2, QTableWidgetItem(k.egitmen_adi))
            self.kurs_tablo.setItem(row, 3, QTableWidgetItem(str(k.kontenjan)))
            self.kurs_tablo.setItem(row, 4, QTableWidgetItem(f"{doluluk}/{k.kontenjan}"))
            self.kurs_tablo.setItem(row, 5, QTableWidgetItem(f"₺{k.fiyat:,.0f}"))
            self.kurs_tablo.setItem(row, 6, QTableWidgetItem(durum))

    def kurs_sil(self):
        row = self.kurs_tablo.currentRow()
        if row < 0:
            QMessageBox.warning(self, "Uyarı", "Silmek için bir kurs seçin!")
            return

        kid = int(self.kurs_tablo.item(row, 0).text())

        for k in self.kurslar:
            if k.id == kid:
                self.kurslar.remove(k)
                break

        self.kurs_listele()
        QMessageBox.information(self, "Başarılı", "Kurs silindi!")

    # ===================== KAYIT SEKMESİ =====================
    def kayit_tab(self):
        widget = QWidget()
        layout = QVBoxLayout(widget)

        # Üst panel - seçimler
        ust_panel = QFrame()
        ust_panel.setStyleSheet("background-color: #2d2d3d; border-radius: 10px;")
        ust_layout = QHBoxLayout(ust_panel)

        sol_ust = QVBoxLayout()
        sol_ust.addWidget(QLabel("👨‍🎓 Öğrenci Seç:"))
        self.kayit_ogrenci = QComboBox()
        sol_ust.addWidget(self.kayit_ogrenci)
        ust_layout.addLayout(sol_ust)

        sag_ust = QVBoxLayout()
        sag_ust.addWidget(QLabel("📚 Kurs Seç:"))
        self.kayit_kurs = QComboBox()
        sag_ust.addWidget(self.kayit_kurs)
        ust_layout.addLayout(sag_ust)

        btn_kaydet = QPushButton("📝 Kursa Kaydet")
        btn_kaydet.setStyleSheet("background-color: #5b5bff; padding: 15px;")
        btn_kaydet.clicked.connect(self.kursa_kaydet)
        ust_layout.addWidget(btn_kaydet)

        layout.addWidget(ust_panel)

        # Kayıtlı öğrenciler tablosu
        self.kayit_tablo = QTableWidget()
        self.kayit_tablo.setColumnCount(6)
        self.kayit_tablo.setHorizontalHeaderLabels(["Kurs ID", "Kurs Adı", "Eğitmen", "Öğrenci", "Email", "Kayıt Tarihi"])
        self.kayit_tablo.horizontalHeader().setStretchLastSection(True)

        layout.addWidget(QLabel("📋 Kayıtlı Öğrenciler"))
        layout.addWidget(self.kayit_tablo)

        # Combo'ları güncelle
        self.kayit_combo_guncelle()
        self.kayitlari_listele()

        return widget

    def kayit_combo_guncelle(self):
        self.kayit_ogrenci.clear()
        for o in self.ogrenciler:
            self.kayit_ogrenci.addItem(f"{o.ad} {o.soyad} ({o.email})", o.id)

        self.kayit_kurs.clear()
        for k in self.kurslar:
            durum = "🟢" if len(k.ogrenciler) < k.kontenjan else "🔴"
            self.kayit_kurs.addItem(f"{durum} {k.ad} - {k.egitmen_adi} ({len(k.ogrenciler)}/{k.kontenjan})", k.id)

    def kursa_kaydet(self):
        if self.kayit_ogrenci.count() == 0:
            QMessageBox.warning(self, "Uyarı", "Öğrenci bulunmuyor!")
            return

        if self.kayit_kurs.count() == 0:
            QMessageBox.warning(self, "Uyarı", "Kurs bulunmuyor!")
            return

        oid = self.kayit_ogrenci.currentData()
        kid = self.kayit_kurs.currentData()

        ogrenci = None
        for o in self.ogrenciler:
            if o.id == oid:
                ogrenci = o
                break

        kurs = None
        for k in self.kurslar:
            if k.id == kid:
                kurs = k
                break

        if not ogrenci or not kurs:
            QMessageBox.warning(self, "Hata", "Öğrenci veya kurs bulunamadı!")
            return

        if ogrenci in kurs.ogrenciler:
            QMessageBox.warning(self, "Uyarı", "Öğrenci zaten bu kursta kayıtlı!")
            return

        if len(kurs.ogrenciler) >= kurs.kontenjan:
            QMessageBox.warning(self, "Uyarı", "Kontenjan dolu!")
            return

        kurs.ogrenciler.append(ogrenci)

        self.kurs_listele()
        self.kayit_combo_guncelle()
        self.kayitlari_listele()

        QMessageBox.information(self, "Başarılı", f"{ogrenci.ad} {ogrenci.soyad} kursa kaydedildi!")

    def kayitlari_listele(self):
        self.kayit_tablo.setRowCount(0)
        for kurs in self.kurslar:
            for ogrenci in kurs.ogrenciler:
                row = self.kayit_tablo.rowCount()
                self.kayit_tablo.insertRow(row)
                self.kayit_tablo.setItem(row, 0, QTableWidgetItem(str(kurs.id)))
                self.kayit_tablo.setItem(row, 1, QTableWidgetItem(kurs.ad))
                self.kayit_tablo.setItem(row, 2, QTableWidgetItem(kurs.egitmen_adi))
                self.kayit_tablo.setItem(row, 3, QTableWidgetItem(f"{ogrenci.ad} {ogrenci.soyad}"))
                self.kayit_tablo.setItem(row, 4, QTableWidgetItem(ogrenci.email))
                self.kayit_tablo.setItem(row, 5, QTableWidgetItem(kurs.tarih))

    # ===================== İSTATİSTİK SEKMESİ =====================
    def istatistik_tab(self):
        widget = QWidget()
        layout = QVBoxLayout(widget)

        # İstatistik kartları
        kart_layout = QHBoxLayout()

        self.toplam_kurs = self.istatistik_karti("📚 Toplam Kurs", "0", "#5b5bff")
        self.toplam_ogrenci = self.istatistik_karti("👨‍🎓 Toplam Öğrenci", "0", "#10b981")
        self.toplam_egitmen = self.istatistik_karti("👨‍🏫 Toplam Eğitmen", "0", "#f59e0b")
        self.toplam_kayit = self.istatistik_karti("📝 Toplam Kayıt", "0", "#ef4444")

        kart_layout.addWidget(self.toplam_kurs)
        kart_layout.addWidget(self.toplam_ogrenci)
        kart_layout.addWidget(self.toplam_egitmen)
        kart_layout.addWidget(self.toplam_kayit)

        layout.addLayout(kart_layout)

        # Gelir bilgisi
        gelir_karti = self.istatistik_karti("💰 Toplam Gelir", "0 TL", "#8b5cf6")
        layout.addWidget(gelir_karti)

        # Detaylı tablo
        layout.addWidget(QLabel("📊 Kurs Bazlı Detaylar"))
        self.istatistik_tablo = QTableWidget()
        self.istatistik_tablo.setColumnCount(6)
        self.istatistik_tablo.setHorizontalHeaderLabels(["Kurs Adı", "Eğitmen", "Kontenjan", "Kayıtlı", "Doluluk", "Gelir"])
        self.istatistik_tablo.horizontalHeader().setStretchLastSection(True)
        layout.addWidget(self.istatistik_tablo)

        self.istatistik_guncelle(gelir_karti)

        return widget

    def istatistik_karti(self, baslik, deger, renk):
        kart = QFrame()
        kart.setStyleSheet(f"""
            QFrame {{
                background-color: #2d2d3d;
                border-radius: 12px;
                border: 2px solid {renk};
            }}
        """)

        layout = QVBoxLayout()

        baslik_label = QLabel(baslik)
        baslik_label.setStyleSheet("font-size: 14px; color: #a0a0a0;")
        baslik_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(baslik_label)

        self.deger_label = QLabel(deger)
        self.deger_label.setStyleSheet(f"font-size: 28px; font-weight: bold; color: {renk};")
        self.deger_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.deger_label)

        kart.setLayout(layout)
        return kart

    def istatistik_guncelle(self, gelir_karti):
        # Kartları güncelle
        for child in self.toplam_kurs.findChildren(QLabel):
            if child.text() != "📚 Toplam Kurs":
                child.setText(str(len(self.kurslar)))
                break

        for child in self.toplam_ogrenci.findChildren(QLabel):
            if child.text() != "👨‍🎓 Toplam Öğrenci":
                child.setText(str(len(self.ogrenciler)))
                break

        for child in self.toplam_egitmen.findChildren(QLabel):
            if child.text() != "👨‍🏫 Toplam Eğitmen":
                child.setText(str(len(self.egitmenler)))
                break

        toplam_kayit = sum(len(k.ogrenciler) for k in self.kurslar)
        for child in self.toplam_kayit.findChildren(QLabel):
            if child.text() != "📝 Toplam Kayıt":
                child.setText(str(toplam_kayit))
                break

        toplam_gelir = sum(len(k.ogrenciler) * k.fiyat for k in self.kurslar)
        for child in gelir_karti.findChildren(QLabel):
            if child.text() != "💰 Toplam Gelir":
                child.setText(f"₺{toplam_gelir:,.0f}")
                break

        # Tablo
        self.istatistik_tablo.setRowCount(0)
        for k in self.kurslar:
            row = self.istatistik_tablo.rowCount()
            self.istatistik_tablo.insertRow(row)

            doluluk = (len(k.ogrenciler) / k.kontenjan) * 100 if k.kontenjan > 0 else 0
            gelir = len(k.ogrenciler) * k.fiyat

            self.istatistik_tablo.setItem(row, 0, QTableWidgetItem(k.ad))
            self.istatistik_tablo.setItem(row, 1, QTableWidgetItem(k.egitmen_adi))
            self.istatistik_tablo.setItem(row, 2, QTableWidgetItem(str(k.kontenjan)))
            self.istatistik_tablo.setItem(row, 3, QTableWidgetItem(str(len(k.ogrenciler))))
            self.istatistik_tablo.setItem(row, 4, QTableWidgetItem(f"{doluluk:.1f}%"))
            self.istatistik_tablo.setItem(row, 5, QTableWidgetItem(f"₺{gelir:,.0f}"))

            # Doluluk rengi
            if doluluk >= 90:
                self.istatistik_tablo.item(row, 4).setForeground(QColor("#ff5b5b"))
            elif doluluk >= 70:
                self.istatistik_tablo.item(row, 4).setForeground(QColor("#f59e0b"))
            else:
                self.istatistik_tablo.item(row, 4).setForeground(QColor("#10b981"))


# ===================== ÇALIŞTIR =====================
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    window = KursPlatformu()
    window.show()
    sys.exit(app.exec_())
