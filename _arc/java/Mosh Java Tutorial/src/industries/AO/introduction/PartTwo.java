package industries.AO.introduction;

public class PartTwo {

  public static void main(String[] args) {
    // Creating objects
    var textBox1 = new TextBox();
    textBox1.setText("Box 1");
    System.out.println(textBox1.getText().toUpperCase());

    var textBox2 = new TextBox();
    textBox2.setText("Box 2");
    System.out.println(textBox2.getText());
    System.out.println("─────────────────────────────────────────────────────────────────────");

    // Memory allocation
    var textBox3 = new TextBox();
    var textBox4 = textBox3;
    textBox4.setText("🔥");
    System.out.println(textBox3.getText());
    System.out.println("─────────────────────────────────────────────────────────────────────");

    // Procedural programming
    int baseSalary = 50_000;
    int extraHours = 10;
    int hourlyRate = 20;

    int wage1 = calculateWage(baseSalary, extraHours, hourlyRate);
    System.out.println(wage1);
    System.out.println("─────────────────────────────────────────────────────────────────────");

    // Encapsulation, getters and setters
    var employee = new Employee(50_000, 20);
    int wage = employee.calculateWage();
    System.out.println(wage);
    System.out.println(Employee.numberOfEmployees);
    System.out.println("─────────────────────────────────────────────────────────────────────");

    // Abstraction
    // Coupling
    // Reducing coupling
    var browser = new Browser();
    // browser.

    // Overloading constructors
    var employee2 = new Employee(50_000, 20);
    var employee3 = new Employee(60_000);

    // Static members
    System.out.println(Employee.numberOfEmployees);
    Employee.printNumberOfEmployees();
    System.out.println("─────────────────────────────────────────────────────────────────────");




  }

  public static int calculateWage(int baseSalary, int extraHours, int hourlyRate) {
    return baseSalary + (extraHours * hourlyRate);
  }
}
