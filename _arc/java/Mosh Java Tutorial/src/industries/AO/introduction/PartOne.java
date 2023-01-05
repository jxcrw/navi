package industries.AO.introduction;

import java.text.NumberFormat;
import java.util.Arrays;
import java.util.Date;
import java.util.Locale;
import java.util.Scanner;

public class PartOne {
  public static void main(String[] args) {
    // Types, Variables, Primitive Types, Reference Types
    byte age = 35;
    long viewCount = 3_123_456_789L;
    float price = 10.99F;
    char letter = 'A';
    Date now = new Date();
    System.out.println(now);
    System.out.println(age + "\n");

    // Primitive Types versus Reference Types
    byte x = 1;
    byte y = x;
    x = 2;
    System.out.println(y);
    Point point1 = new Point(1, 1);
    Point point2 = point1;
    point1.x = 2;
    System.out.println(point2);

    // Strings
    String message = "🔥" + " ಠ_ಠ 🔥 XYZ   ";
    System.out.println(message);
    System.out.println(message.endsWith("🔥"));
    System.out.println(message.startsWith("Δ"));
    System.out.println(message.length());
    System.out.println(message.indexOf("ಠ_ಠ"));
    System.out.println(message.replace("🔥", "¯\\_(ツ)_/¯"));
    System.out.println(message.replace("test", "pizza"));
    System.out.println(message);
    System.out.println(message.toLowerCase().trim() + "\n");

    // Escape sequences
    String escapeSequence = "\\🔥\\";
    System.out.println(escapeSequence + "\n");

    // Arrays
    int[] numbers = new int[5];
    numbers[0] = 1;
    numbers[1] = 2;
    System.out.println(numbers);
    System.out.println(Arrays.toString(numbers));

    int[] moreNumbers = {2, 3, 5, 1, 4};
    System.out.println(moreNumbers.length);
    Arrays.sort(moreNumbers);
    System.out.println(Arrays.toString(moreNumbers) + "\n");

    // Multi-dimensional arrays
    int[][] multiNumbers = new int[2][3];
    multiNumbers[0][0] = 5;
    System.out.println(Arrays.deepToString(multiNumbers));

    int[][] twoDNumbers = { {1, 2, 3}, {4, 5, 6} };
    System.out.println(Arrays.deepToString(twoDNumbers) + "\n");

    // Constants
    final float PI = 3.14F;

    // Arithmetic expressions
    double result = (double)10 / (double)3;
    System.out.println(result);
    int a = 1;
    a++;
    System.out.println(a);
    int b = 1;
    int c = b++;
    System.out.println(c);
    int d = ++b;
    System.out.println(d);
    d += 2; // Also -= , *=, /=
    System.out.println(d);

    // Casting
    short myX = 1; // Implicit casting ⇒ byte > short > int > long > float > double
    int myY = myX + 2;
    System.out.println(myY);
    double myA = 1.1;
    double myB = myA + 2; // 2 ⇒ 2.0
    System.out.println(myB);
    double myD = 1.1;
    int e = (int)myD + 2; // Explicit casting
    System.out.println(e);

    String f = "1.1";
    double g = Double.parseDouble(f) + 2;
    System.out.println(g + "\n");

    // The Math class
    float myNumber = 1.1F;
    System.out.println(Math.round(myNumber));
    System.out.println(Math.ceil(myNumber));
    System.out.println(Math.floor(myNumber));
    System.out.println(Math.max(1, 2));
    System.out.println(Math.min(1, 2));
    System.out.println(Math.round(Math.random() * 100));

    // Formatting numbers
    NumberFormat currency = NumberFormat.getCurrencyInstance(Locale.US);
    String currencyString = currency.format(1234567.891);
    System.out.println(currencyString);

    NumberFormat percent = NumberFormat.getPercentInstance();
    String percentString = percent.format(0.089);
    System.out.println(percentString);
    System.out.println(NumberFormat.getPercentInstance().format(0.89) + "\n");

    // Reading input
    Scanner scanner = new Scanner(System.in);
    System.out.print("Enter your age: ");
    String myAge = scanner.nextLine().trim();
    System.out.println("You are: " + myAge);

    // Comparison operators
    int cx = 1;
    int cy = 1;
    System.out.println(cx == cy);
    System.out.println((cx != cy) + "\n");

    // Logical operators
    int temperature = 22;
    boolean isWarm = temperature > 20 && temperature < 30;
    System.out.println(isWarm);

    boolean hasHighIncome = true;
    boolean hasGoodCredit = true;
    boolean hasCriminalRecord = false;
    boolean isEligible = (hasHighIncome || hasGoodCredit) && !hasCriminalRecord;
    System.out.println(isEligible);

    // If statements
    int temp = 32;
    if (temp > 30) {
      System.out.println("It's a hot day\nDrink water");
    } else if (temp > 20) {
      System.out.println("It's a beautiful day");
    } else {
      System.out.println("It's a cold day");
    }

    // Simplifying if statements
    int income = 120_000;
    boolean hasHighIncome2 = (income > 100_000);
    System.out.println(hasHighIncome2);

    // The ternary operator
    int income2 = 120_000;
    String className = income2 > 100_000 ? "First" : "Economy";

    // Switch statements
    String role = "admin";
    if (role == "admin") {
      System.out.println("You are an admin");
    } else if (role == "moderator") {
      System.out.println("You are a moderator");
    } else {
      System.out.println("You are a guest");
    }

    switch (role) {
      case "admin":
        System.out.println("You are an admin");
        break;
      case "moderator":
        System.out.println("You are a moderator");
        break;
      default:
        System.out.println("You are a guest");
    }

    // For loops
    for (int i = 0; i < 5; i++) {
      System.out.println("🔥 " + i);
    }

    // While loops
    int i = 5;
    while (i > 0) {
      System.out.println("🔥 " + i);
      i--;
    }

    String input = "";
    Scanner myScanner = new Scanner(System.in);
    while (!input.equals("quit")) {
      System.out.print("Input: ");
      input = myScanner.next().toLowerCase();
      System.out.println(input);
    }

    // Do while loops (rarer, usually prefer to use while loops)
    String myInput = "";
    Scanner myScanner2 = new Scanner(System.in);
    do {
      System.out.print("Input: ");
      myInput = myScanner2.next().toLowerCase();
      System.out.println(myInput);
    } while (!myInput.equals("quit"));

    // Break and continue
    String input2 = "";
    Scanner scanner2 = new Scanner(System.in);
    while (true) {
      System.out.print("Input: ");
      input2 = scanner2.next().toLowerCase().trim();
      if (input2.equals("pass")) {
        continue;
      } else if (input2.equals("quit")) {
        break;
      }
      System.out.println(input2);
    }

    // For each loop
    String[] fruits = {"Apple", "Mango", "Orange"};
    for (String s : fruits) {
      System.out.println(s);
    }

    for (String fruit : fruits) {
      System.out.println(fruit);
    }

    // Creating methods
    String name = greetUser("🔥", "McGee");

    // Debugging
    System.out.println("Start");
    printNumbers(4);
    System.out.println("Finish");
  }

  // Creating methods
  public static String greetUser(String firstName, String lastName) {
    System.out.println("Hello " + firstName + " " + lastName);
    return "Hello " + firstName + " " + lastName;
  }

  // Debugging
  public static void printNumbers(int limit) {
    for (int i = 0; i <= limit; i++) {
      System.out.println(i);
    }
  }
}
