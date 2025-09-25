#include <LiquidCrystal.h>

#define RELAY_PIN 2      
#define SENSOR_PIN A0     
#define NEM_ESIK 800      // Toprak kuru eşik değeri (0-1023 arası)

// LCD pinleri: RS, E, D4, D5, D6, D7
LiquidCrystal lcd(7, 8, 9, 10, 11, 12);

void setup() {
  pinMode(RELAY_PIN, OUTPUT);
  digitalWrite(RELAY_PIN, HIGH); // Röle başlangıçta kapalı
  Serial.begin(9600);

  // LCD başlat - daha uzun bekleme süresi
  lcd.begin(16, 2);
  delay(1000); // LCD'nin tam olarak başlatılması için daha uzun bekleme
  
  // Başlangıç mesajı
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Sulama Sistemi");
  lcd.setCursor(0, 1);
  lcd.print("Baslatiliyor...");
  delay(2000);
  
  // Ekranı temizle
  lcd.clear();
}

void loop() {
  int nemDegeri = analogRead(SENSOR_PIN);  
  Serial.print("Nem Degeri: ");
  Serial.println(nemDegeri);

  // Her seferinde ekranı tamamen temizle
  lcd.clear();
  
  // 1. satır: nem değeri
  lcd.setCursor(0, 0);
  lcd.print("Nem: ");
  lcd.print(nemDegeri);
  lcd.print("     "); // Kalan karakterleri temizle

  // 2. satır: sulama durumu
  lcd.setCursor(0, 1);
  if (nemDegeri > NEM_ESIK) {
      digitalWrite(RELAY_PIN, LOW);  
      Serial.println("Toprak kuru → Sulama basladi");
      lcd.print("Sulama: ACILDI");
  } else {
      digitalWrite(RELAY_PIN, HIGH); 
      Serial.println("Toprak nemli → Sulama kapali");
      lcd.print("Sulama: KAPALI");
  }

  delay(1000); // 1 saniye bekle
}