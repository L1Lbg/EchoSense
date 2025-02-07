// Définition des pins des LEDs
int ledRouge = 10;
int ledOrange = 11;
int ledVert = 12;
int ledIndicateur = 13;  // LED supplémentaire (par exemple, pour un piéton)

void setup() {
  // Initialisation des LEDs comme sorties
  pinMode(ledRouge, OUTPUT);
  pinMode(ledOrange, OUTPUT);
  pinMode(ledVert, OUTPUT);
  pinMode(ledIndicateur, OUTPUT);
  
  // Commencer la communication série
  Serial.begin(9600);  // Assurez-vous que la vitesse de communication correspond à celle du Raspberry Pi
}

void loop() {
  // Vérifier si des données sont disponibles dans la communication série
  if (Serial.available() > 0) {
    char commande = Serial.read();  // Lire la commande envoyée par le Raspberry Pi

    // Apagar todas las luces antes de activar la deseada
    digitalWrite(ledOrange, LOW);
    digitalWrite(ledVert, LOW);
    digitalWrite(ledIndicateur, LOW);
    digitalWrite(ledRouge, LOW);
    
    // Contrôler les LEDs en fonction de la commande reçue
    if (commande == '0') {  // Feu rouge
      digitalWrite(ledRouge, HIGH);
    } 
    else if (commande == '2') {  // Feu orange
      digitalWrite(ledOrange, HIGH);
    } 
    else if (commande == '3') {  // Feu vert
      digitalWrite(ledVert, HIGH);
    }
    else if (commande == '1') {  // Feu bleu
      digitalWrite(ledIndicateur, HIGH);
    }
  }
}
