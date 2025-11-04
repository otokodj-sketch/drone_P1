#include <M5Unified.h>

void setup() {
  auto cfg = M5.config();
  M5.begin(cfg);
  Serial.begin(115200);
  delay(1000);
  Serial.println("M5StickC Plus2 Gyro Test Start");
}

void loop() {
  M5.update();

  float gx, gy, gz;
  M5.Imu.getGyroData(&gx, &gy, &gz);  // ジャイロ値を取得 [deg/s]

  Serial.print(gx); Serial.print(",");
  Serial.print(gy); Serial.print(",");
  Serial.println(gz);

  delay(100);
}
