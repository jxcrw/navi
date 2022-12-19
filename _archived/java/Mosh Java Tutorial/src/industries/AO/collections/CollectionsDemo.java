package industries.AO.collections;

import java.util.*;

public class CollectionsDemo {
  public static void show() {
    // Collection interface
    Collection<String> collection = new ArrayList<>();
    collection.add("a");
    collection.add("b");
    collection.add("c");
    for (var item: collection)
      System.out.println(item);
    System.out.println(collection);

    Collections.addAll(collection, "e", "f", "g");
    System.out.println(collection);

    System.out.println(collection.size());

    collection.remove("e");
    System.out.println(collection);

    System.out.println(collection.contains("f"));

    var objectArray = collection.toArray();
    var stringArray = collection.toArray(new String[0]);

    Collection<String> other = new ArrayList<>();
    other.addAll(collection);
    System.out.println(collection == other);
    System.out.println(collection.equals(other));

    collection.clear();
    System.out.println(collection.isEmpty());

    // List interface

    List<String> list = new ArrayList<>();
    list.add("a");
    list.add("b");
    list.add("c");
    list.add(0, "🔥");
    Collections.addAll(list,"e", "f", "g");

    System.out.println(list.get(0));

    list.set(0, "💣");
    System.out.println(list.get(0));

    list.remove(0);
    System.out.println(list);

    System.out.println(list.indexOf("e"));
    System.out.println(list.indexOf("ಠ_ಠ"));
    System.out.println(list.lastIndexOf("f"));

    System.out.println(list.subList(0, 4));

  }
}
