package industries.AO.introduction;

public abstract class UIControl {
  private boolean isEnabled;
  //
  // public UIControl(boolean isEnabled) {
  //   this.isEnabled = isEnabled;
  //   // System.out.println("UIControl");
  // }

  public void enable() {
    isEnabled = true;
  }

  public void disable() {
    isEnabled = false;
  }

  public abstract void render();

  public boolean isEnabled() {
    return isEnabled;
  }
}
