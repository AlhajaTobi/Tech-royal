import java.util.Scanner;

public class CreditCardValidator {

    // Method to extract digits from the card number string
    public static int[] extractDigits(String cardNumber) {
        // Create an array to hold the digits
        int[] digits = new int[cardNumber.length()];

        // Loop through each character in the string
        for (int i = 0; i < cardNumber.length(); i++) {
            // Convert the character to its numeric value and store it in the array
            digits[i] = Character.getNumericValue(cardNumber.charAt(i));
        }
        return digits; // Return the array of digits
    }

    // Method to validate the card number using the Luhn algorithm
    public static boolean luhnAlgorithm(String cardNumber) {
        // Extract digits from the card number
        int[] digits = extractDigits(cardNumber);
        int totalSum = 0; // Variable to hold the sum of the digits

        // Process the digits in reverse order for Luhn calculation
        for (int i = digits.length - 1; i >= 0; i--) {
            int currentDigit = digits[i]; // Get the current digit

            // Double every second digit from the right
            if ((digits.length - 1 - i) % 2 == 1) {
                currentDigit *= 2; // Double the digit
                // If the result is greater than 9, subtract 9
                if (currentDigit > 9) {
                    currentDigit -= 9;
                }
            }
            // Add the processed digit to the total sum
            totalSum += currentDigit;
        }

        // The card is valid if the total sum modulo 10 is 0
        return totalSum % 10 == 0;
    }

    // Method to determine the card type based on the starting digits
    public static String getCardType(String cardNumber) {
        // Check the starting digits to determine the card type
        if (cardNumber.startsWith("4")) {
            return "Visa Card"; // Visa cards start with 4
        } else if (cardNumber.startsWith("5")) {
            return "MasterCard"; // MasterCards start with 5
        } else if (cardNumber.startsWith("6")) {
            return "Discover Card"; // Discover cards start with 6
        } else if (cardNumber.startsWith("37")) {
            return "American Express Card"; // American Express cards start with 37
        } else {
            return "Unknown Card"; // Card type not recognized
        }
    }

    // Method to check the validity of the credit card number
    public static String checkCreditCard(String cardNumber) {
        // Use the Luhn algorithm to check validity
        if (luhnAlgorithm(cardNumber)) {
            // If valid, get the card type
            return "Valid " + getCardType(cardNumber);
        } else {
            return "Invalid Card Number"; // If invalid, return error message
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in); // Create a scanner for user input
        System.out.print("Enter your credit card number: "); // Prompt user for input

        String cardNumber = scanner.nextLine(); // Read user input

        // Validate input: check if all characters are digits
        if (!cardNumber.matches("\\d+")) {
            System.out.println("Invalid input. Please enter a numeric card number."); // Error message for invalid input
        } else {
            // Check and display the validity and type of the credit card
            System.out.println(checkCreditCard(cardNumber));
        }

    }
}