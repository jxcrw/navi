package industries.AO.introduction;

public class TaxCalculator2020 extends AbstractTaxCalculator {
  private double taxableIncome;

  public TaxCalculator2020(double taxableIncome) {
    this.taxableIncome = taxableIncome;
  }

  @Override
  public double calculateTax() {
    return taxableIncome * 0.3;
  }
}
