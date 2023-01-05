package industries.AO.exceptions;

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.text.ParseException;
import java.text.SimpleDateFormat;

public class ExceptionsDemo {

  public static void show() throws IOException {
    try (
        var reader = new FileReader("file.txt");
        var writer = new FileWriter("...");
      ) {
      var value = reader.read();
      new SimpleDateFormat().parse("");
      System.out.println("File opened.");
    } catch (IOException | ParseException e) {
      System.out.println("Could not read data.");
    }

    var account = new Account();
    try {
      account.deposit(5);
    } catch (IOException e) {
      System.out.println("Logging");
      throw e;
    }

    try {
      account.withdraw(10);
    } catch (AccountException e) {
      // System.out.println(e.getMessage());
      e.printStackTrace();
    }
  }

  public static void sayHello(String name) {
    System.out.println(name.toUpperCase());
  }

}
