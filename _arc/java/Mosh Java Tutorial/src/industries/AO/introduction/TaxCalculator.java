package industries.AO.introduction;

public interface TaxCalculator {
  float minimumTax = 100; // Interface fields like this are generally thought to be bad practice
  double calculateTax();

  // Shouldn't put static methods in interfaces either even though you can apparently do that now
}
