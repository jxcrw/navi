package industries.AO.introduction;

public class TaxMain {
  public static void main(String[] args) {
    // // Constructor injection (most common)
    // var calculator = new TaxCalculator2020(100_000);
    // var report = new TaxReport(calculator);
    // report.show();
    //
    // // Setter injection
    // report.setCalculator(new TaxCalculator2021());
    // report.show();

    // Method injection
    var calculator = new TaxCalculator2020(100_000);
    var report = new TaxReport();
    report.show(calculator);
    report.show(new TaxCalculator2021());
  }

  public void doSomething(TaxCalculator calculator) {
  }
}
