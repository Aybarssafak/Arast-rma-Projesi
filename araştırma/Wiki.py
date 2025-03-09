from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


url = "https://tr.wikipedia.org/wiki/Anasayfa"
aranılan = "ceza" #Bu kısımda ne aratmak isterseniz onu girebilirsiniz.
kaynak = aranılan+".doc"#dosya türünü ayarlayın.

class Wiki:
    def __init__(self, url, aranılan):
        self.url = url
        self.aranılan = aranılan
        self.kaynak = kaynak
        self.driver = webdriver.Chrome()

    def arama(self):
        self.driver.get(url)
        time.sleep(1)

        self.driver.fullscreen_window()
        self.driver.find_element(By.NAME, "search").send_keys(self.aranılan)
        self.driver.find_element(By.CSS_SELECTOR, ".cdx-button.cdx-search-input__end-button").click()
        time.sleep(2)

    def getContent(self, kaynak):
        paragraflar = self.driver.find_elements(By.TAG_NAME, "p")

        with open(kaynak, "w", encoding="utf-8") as dosya:
            dosya.write("")
            for p in paragraflar:
                text = p.text.strip()
                if text:  # Boş olmayan paragrafları yaz
                    dosya.write(text + "\n\n")

        print("Paragraflar başarıyla kaydedildi.")
        time.sleep(2)


AybarsWiki = Wiki(url, aranılan)
AybarsWiki.arama()
AybarsWiki.getContent(kaynak)
