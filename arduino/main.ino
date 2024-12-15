void setup() {
    // Initialize serial communication at 9600 bits per second
    Serial.begin(9600);
}

void loop() {
    // Loop from 1 to 100
    for (int i = 1; i <= 100; i++) {
        // Print the current number
        Serial.println(i);
        // Wait for 1 second (1000 milliseconds)
        delay(1000);
    }
    // Stop the loop after printing 1 to 100
    while (true) {
        // Do nothing, effectively halting the program
    }
}
