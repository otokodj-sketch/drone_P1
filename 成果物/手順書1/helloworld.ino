#include <M5StickCPlus2.h>​

void setup() {​
    M5.begin();  // 初期化​
    M5.Lcd.setRotation(3);  // 画面の向きを設定​
    M5.Lcd.fillScreen(BLACK);  // 画面を黒でクリア​
    M5.Lcd.setTextColor(WHITE);​
    M5.Lcd.setTextSize(2);​
    M5.Lcd.setCursor(10, 10);​
    M5.Lcd.println("Hello World!");​
}​
​
void loop() {​
    // ここにメインの処理を記述​
}
