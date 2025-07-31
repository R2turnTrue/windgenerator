// A0 - 빨강
// A1 - 보라
// A2 - 노랑
// A3 - 검정

void setup() {
  Serial.begin(9600);
}

void loop() {
  int A = 1024-analogRead(A0);
  int B = 1024-analogRead(A1);
  int C = 1024-analogRead(A2);
  int D = 1024-analogRead(A3);

  Serial.print(A);
  Serial.print('/');
  Serial.print(B);
  Serial.print('/');
  Serial.print(C);
  Serial.print('/');
  Serial.println(D);
  delay(50);
}