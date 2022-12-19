package industries.AO.generics;

public class GenericsMain {
  public static void main(String[] args) {
    var myList = new List();
    myList.add(1);

    var integerList = new GenericList<Integer>();
    integerList.add(1);
    int number = integerList.get(0);

    var numbers = new GenericList<Integer>();
    numbers.add(1); // Boxing
    int myNumber = numbers.get(0); // Unboxing

    new GenericList<Integer>();

    var user1 = new User(10);
    var user2 = new User(20);
    if (user1.compareTo(user2) < 0)
      System.out.println("user1 < user2");
    else if (user1.compareTo(user2) == 0)
      System.out.println("user1 == user2");
    else
      System.out.println("user1 > user2");

    var max = Utilities.max(1, 3);
    System.out.println(max);
    System.out.println(Utilities.max(user1, user2));

    Utilities.print(1, "🔥");

    var user = new Instructor(10);
    Utilities.printUser(user);

    var instructors = new GenericList<Instructor>();
    Utilities.printUsers(instructors);

    var list = new GenericList<String>();
    list.add("a");
    list.add("b");
    for (var item: list)
      System.out.println(item);
  }
}
