import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Mountain Watch',
      theme: ThemeData(
        // This is the theme of your application.
        //
        // TRY THIS: Try running your application with "flutter run". You'll see
        // the application has a purple toolbar. Then, without quitting the app,
        // try changing the seedColor in the colorScheme below to Colors.green
        // and then invoke "hot reload" (save your changes or press the "hot
        // reload" button in a Flutter-supported IDE, or press "r" if you used
        // the command line to start the app).
        //
        // Notice that the counter didn't reset back to zero; the application
        // state is not lost during the reload. To reset the state, use hot
        // restart instead.
        //
        // This works for code too, not just values: Most code changes can be
        // tested with just a hot reload.
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.blue),
      ),
      home: const MyHomePage(title: 'Is The Mountain Out?'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key, required this.title});

  // This widget is the home page of your application. It is stateful, meaning
  // that it has a State object (defined below) that contains fields that affect
  // how it looks.

  // This class is the configuration for the state. It holds the values (in this
  // case the title) provided by the parent (in this case the App widget) and
  // used by the build method of the State. Fields in a Widget subclass are
  // always marked "final".

  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  int _correctCount = 0;
  int _wrongCount = 0;

  void _incrementCorrect() {
    setState(() {
      _correctCount++;
    });
  }

  void _incrementWrong() {
    setState(() {
      _wrongCount++;
    });
  }

  @override
  Widget build(BuildContext context) {
    // This method is rerun every time setState is called, for instance as done
    // by the _incrementCorrect and _incrementWrong methods above.
    //
    // The Flutter framework has been optimized to make rerunning build methods
    // fast, so that you can just rebuild anything that needs updating rather
    // than having to individually change instances of widgets.
    return Scaffold(
      appBar: AppBar(
        // TRY THIS: Try changing the color here to a specific color (to
        // Colors.amber, perhaps?) and trigger a hot reload to see the AppBar
        // change color while the other colors stay the same.
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        // Here we take the value from the MyHomePage object that was created by
        // the App.build method, and use it to set our appbar title.
        title: Text(widget.title),
      ),
      body: Stack(
        children: [
          Column(
            children: [
              // Top half - Mt. Rainier image
              Expanded(
                flex: 1,
                child: Container(
                  width: double.infinity,
                  child: Image.network(
                    'https://upload.wikimedia.org/wikipedia/commons/e/eb/Mount_Rainier_from_west.jpg',
                    fit: BoxFit.cover,
                  ),
                ),
              ),
              // Bottom half - Stats and buttons
              Expanded(
                flex: 1,
                child: Container(
                  padding: const EdgeInsets.all(16.0),
                  child: Column(
                    children: [
                      // Stats
                      Row(
                        mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                        children: [
                          Column(
                            children: [
                              const Text(
                                'Visible Days',
                                style: TextStyle(fontSize: 16),
                              ),
                              Text(
                                '$_correctCount',
                                style: Theme.of(context).textTheme.headlineMedium,
                              ),
                            ],
                          ),
                          Column(
                            children: [
                              const Text(
                                'Hidden Days',
                                style: TextStyle(fontSize: 16),
                              ),
                              Text(
                                '$_wrongCount',
                                style: Theme.of(context).textTheme.headlineMedium,
                              ),
                            ],
                          ),
                        ],
                      ),
                      // Question text
                      Expanded(
                        child: Center(
                          child: Text(
                            'Is the mountain out?',
                            style: Theme.of(context).textTheme.headlineSmall,
                          ),
                        ),
                      ),
                      // Buttons at the bottom
                      Row(
                        children: [
                          Expanded(
                            child: Padding(
                              padding: const EdgeInsets.symmetric(horizontal: 16.0),
                              child: SizedBox(
                                height: 56,
                                child: ElevatedButton(
                                  onPressed: _incrementCorrect,
                                  style: ElevatedButton.styleFrom(
                                    backgroundColor: Colors.green,
                                    shape: RoundedRectangleBorder(
                                      borderRadius: BorderRadius.circular(8),
                                    ),
                                  ),
                                  child: const Icon(Icons.check, size: 30),
                                ),
                              ),
                            ),
                          ),
                          Expanded(
                            child: Padding(
                              padding: const EdgeInsets.symmetric(horizontal: 16.0),
                              child: SizedBox(
                                height: 56,
                                child: ElevatedButton(
                                  onPressed: _incrementWrong,
                                  style: ElevatedButton.styleFrom(
                                    backgroundColor: Colors.red,
                                    shape: RoundedRectangleBorder(
                                      borderRadius: BorderRadius.circular(8),
                                    ),
                                  ),
                                  child: const Icon(Icons.close, size: 30),
                                ),
                              ),
                            ),
                          ),
                        ],
                      ),
                      SizedBox(height: 20), // Bottom padding
                    ],
                  ),
                ),
              ),
            ],
          ),
        ],
      ),
    );
  }
}
