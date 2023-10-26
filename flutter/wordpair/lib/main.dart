import 'package:english_words/english_words.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';


void main() {
  runApp(MyApp());
}


class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return ChangeNotifierProvider(
      create: (context) => MyAppState(),
      child: MaterialApp(
        title: 'tagg',
        theme: ThemeData(
          useMaterial3: true,
          colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
        ),
        home: MyHomePage(),
      ),
    );
  }
}


class MyAppState extends ChangeNotifier {
  var wordpair = WordPair.random();
  var faves = <WordPair>[];

  void getNext() {
    wordpair = WordPair.random();
    notifyListeners();
  }

  void toggleFave() {
    if (faves.contains(wordpair)) {
      faves.remove(wordpair);
    } else {
      faves.add(wordpair);
    }
    notifyListeners();
  }
}


class MyHomePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    var appState = context.watch<MyAppState>();
    var wordpair = appState.wordpair;

    IconData iconFave = (appState.faves.contains(wordpair)) ? Icons.favorite : Icons.favorite_border;

    return Scaffold(
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            BigCard(wordpair: wordpair),
            SizedBox(height: 10),
            Row(
              mainAxisSize: MainAxisSize.min,
              children: [
                ElevatedButton.icon(
                  onPressed: () {
                    appState.toggleFave();
                  },
                  icon: Icon(iconFave),
                  label: Text('Like'),
                ),
                SizedBox(width: 10),
                ElevatedButton(
                  onPressed: () {
                    appState.getNext();
                  },
                  child: Icon(Icons.refresh),
                ),
              ],
            )
          ],
        ),
      ),
    );
  }
}


class BigCard extends StatelessWidget {
  const BigCard({
    super.key,
    required this.wordpair,
  });

  final WordPair wordpair;

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);
    final style = theme.textTheme.displayMedium!.copyWith(
      color: theme.colorScheme.onPrimary,
    );

    return Card(
      color: theme.colorScheme.primary,
      child: Padding(
        padding: const EdgeInsets.all(20),
        child: Text(
          wordpair.asLowerCase,
          style: style,
          semanticsLabel: "${wordpair.first} ${wordpair.second}",
        ),
      ),
    );
  }
}
