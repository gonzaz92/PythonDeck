#include <Wire.h> 
#include <LiquidCrystal_I2C.h>
//encoder 1
#define clk A1 //número define pin
#define dt A0
//encoder 2
int der = 9; //clk
int izq = 10; //dt
//pines y botones
const int buttonA = 0; //Funciona
const int buttonB = 12; //Funciona
const int buttonC = A3; //Funciona
const int buttonD = 3; // Funciona
const int buttonE = 4; // Funciona
const int buttonF = 5; //Funciona
const int buttonG = 2; //Funciona
const int buttonH = 7; //Funciona
const int buttonI = 8; //Funciona
const int btnJ = A2; //Funciona
const int but = 11; //Funciona
//estado
int buttonState = 0;
int led = HIGH;

LiquidCrystal_I2C lcd(0x27, 16, 2);

//Menú
String opciones[] = {"Escritorio" , "Streaming", "OBS", "Edicion", "Redes", "Apagar"};
int max_opciones = sizeof(opciones)/sizeof(opciones[0]);

int state_clk_old;
int state_der_old;
int count = 0;

void setup() {
  Serial.begin(9600);
  lcd.begin();
  lcd.backlight();
  pinMode (clk, INPUT);
  pinMode (dt, INPUT);
  pinMode (btnJ, INPUT_PULLUP);
  pinMode (buttonA, INPUT_PULLUP);
  pinMode (buttonB, INPUT_PULLUP);
  pinMode (buttonC, INPUT_PULLUP);
  pinMode (buttonD, INPUT_PULLUP);
  pinMode (buttonE, INPUT_PULLUP);
  pinMode (buttonF, INPUT_PULLUP);
  pinMode (buttonG, INPUT_PULLUP);
  pinMode (buttonH, INPUT_PULLUP);
  pinMode (buttonI, INPUT_PULLUP);
  pinMode (der, INPUT);
  pinMode (izq, INPUT);
  pinMode (but, INPUT_PULLUP);
  
  
  state_clk_old = digitalRead(clk);
  state_der_old = digitalRead(der);
  mostrar_modo();
  }
void loop() {
    
    encoderA();
    
    if(count != 5 && led == HIGH){
    encoderB();
    
    botones();
    }
    apagar();
}
 //encoder del menú
void encoderA(){
    int state_clk = digitalRead(clk);
    int state_dt = digitalRead(dt);
    if(state_clk_old == HIGH && state_clk == LOW){
    if(state_dt == LOW){
      count--;
    }else{
      count++;
    }
    if(count < 0) count = max_opciones - 1;
    if(count > max_opciones-1) count = 0;
    
    mostrar_modo();
  }
    delay(5);
    state_clk_old = state_clk;
}
//encoder para pc
void encoderB(){
  static unsigned long ultimocorte = 0;
  unsigned long corte = millis();
  int state_der = digitalRead(der);
  int state_izq = digitalRead(izq);
  if(corte - ultimocorte > 10){
    if(state_der_old == LOW){
      Serial.println(opciones[count] + "," + "der");
    }else if(state_izq == LOW){
        Serial.println(opciones[count] + "," + "izq");
    }
  }
  delay(5);
  state_der_old = state_der;
  ultimocorte = corte;
}
void mostrar_modo(){
  lcd.clear();
  lcd.setCursor(0,0);
  lcd.print("Modo:");
  lcd.setCursor(0,1);
  lcd.print(opciones[count]);
}
void botones(){
  buttonState = digitalRead(buttonA);
  if(buttonState == LOW){
    Serial.println(opciones[count] + "," + "BtnA");
    delay(150);
  }
  buttonState = digitalRead(buttonB);
  if(buttonState == LOW){
    Serial.println(opciones[count] + "," + "BtnB");
    delay(150);
    }
  buttonState = digitalRead(buttonC);
  if(buttonState == LOW){
    Serial.println(opciones[count] + "," + "BtnC");
    delay(150);
    }
  buttonState = digitalRead(buttonD);
  if(buttonState == LOW){
    Serial.println(opciones[count] + "," + "BtnD");
    delay(150);
    }
  buttonState = digitalRead(buttonE);
  if(buttonState == LOW){
    Serial.println(opciones[count] + "," + "BtnE");
    delay(150);
    }
  buttonState = digitalRead(buttonF);
  if(buttonState == LOW){
    Serial.println(opciones[count] + "," + "BtnF");
    delay(150);
    }
  buttonState = digitalRead(buttonG);
  if(buttonState == LOW){
    Serial.println(opciones[count] + "," + "BtnG");
    delay(150);
    }
  buttonState = digitalRead(buttonH);
  if(buttonState == LOW){
    Serial.println(opciones[count] + "," + "BtnH");
    delay(150);
    }
  buttonState = digitalRead(buttonI);
  if(buttonState == LOW){
    Serial.println(opciones[count] + "," + "BtnI");
    delay(150);
    }
  buttonState = digitalRead(btnJ);
  if(buttonState == LOW){
    Serial.println(opciones[count] + "," + "btnJ");
    delay(150);
  }
  buttonState = digitalRead(but);
  if(buttonState == LOW){
    Serial.println(opciones[count] + "," + "but");
    delay(150);
  }
}
void apagar(){
  buttonState = digitalRead(but);
  if(count == 5 && led == HIGH && buttonState == LOW){
    lcd.noDisplay();
    lcd.noBacklight();
    led = LOW;
  }
  buttonState = digitalRead(btnJ);
  if(count == 5 && led == LOW && buttonState == LOW){
    lcd.begin();
    lcd.backlight();
    mostrar_modo();
    led = HIGH;
  }
 }
