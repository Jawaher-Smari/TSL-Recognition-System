import 'dart:math';
import 'package:flutter/material.dart';
import 'package:tsl_app/widgets/custom_button.dart';
import 'package:video_player/video_player.dart';

class GameImageWordScreen extends StatefulWidget {
  const GameImageWordScreen({super.key});

  @override
  State<GameImageWordScreen> createState() => _GameImageWordScreenState();
}

class _GameImageWordScreenState extends State<GameImageWordScreen> {
  final Map<String, List<Map<String, String>>> _wordImagePairs = {
    "الحروف": [
      {"word": "A", "media": "assets/images/alphabet/A.jpg"},
      {"word": "B", "media": "assets/images/alphabet/B.jpg"},
      {"word": "C", "media": "assets/images/alphabet/C.jpg"},
      {"word": "D", "media": "assets/images/alphabet/D.jpg"},
      {"word": "E", "media": "assets/images/alphabet/E.jpg"},
      {"word": "F", "media": "assets/images/alphabet/F.jpg"},
      {"word": "G", "media": "assets/images/alphabet/G.jpg"},
      {"word": "H", "media": "assets/images/alphabet/H.jpg"},
      {"word": "I", "media": "assets/images/alphabet/I.jpg"},
      {"word": "J", "media": "assets/images/alphabet/J.jpg"},
      {"word": "K", "media": "assets/images/alphabet/K.jpg"},
      {"word": "L", "media": "assets/images/alphabet/L.jpg"},
      {"word": "M", "media": "assets/images/alphabet/M.jpg"},
      {"word": "N", "media": "assets/images/alphabet/N.jpg"},
      {"word": "O", "media": "assets/images/alphabet/O.jpg"},
      {"word": "P", "media": "assets/images/alphabet/P.jpg"},
      {"word": "Q", "media": "assets/images/alphabet/Q.jpg"},
      {"word": "R", "media": "assets/images/alphabet/R.jpg"},
      {"word": "S", "media": "assets/images/alphabet/S.jpg"},
      {"word": "T", "media": "assets/images/alphabet/T.jpg"},
      {"word": "U", "media": "assets/images/alphabet/U.jpg"},
      {"word": "V", "media": "assets/images/alphabet/V.jpg"},
      {"word": "W", "media": "assets/images/alphabet/W.jpg"},
      {"word": "X", "media": "assets/images/alphabet/X.jpg"},
      {"word": "Y", "media": "assets/images/alphabet/Y.jpg"},
      {"word": "Z", "media": "assets/images/alphabet/Z.mp4"},
    ],
    "العائلة": [
      {"word": "بابا", "media": "assets/images/family/father.mp4"},
      {"word": "أمي", "media": "assets/images/family/mother.jpg"},
      {"word": "خويا", "media": "assets/images/family/brother.mp4"},
      {"word": "أختي", "media": "assets/images/family/sister.mp4"},
    ],
    "الأيام": [
      {"word": "الأحد", "media": "assets/images/days/sunday.mp4"},
      {"word": "الإثنين", "media": "assets/images/days/monday.mp4"},
      {"word": "الثلاثاء", "media": "assets/images/days/tuesday.mp4"},
      {"word": "الأربعاء", "media": "assets/images/days/wednesday.mp4"},
      {"word": "الخميس", "media": "assets/images/days/thursday.mp4"},
      {"word": "الجمعة", "media": "assets/images/days/friday.mp4"},
      {"word": "السبت", "media": "assets/images/days/saturday.mp4"},
    ],
    "الأطباق": [
      {"word": "شربة", "media": "assets/images/plats/chorba.mp4"},
      {"word": "كفتاجي", "media": "assets/images/plats/kafteji.mp4"},
      {"word": "كسكسي", "media": "assets/images/plats/kosksi.mp4"},
      {"word": "لبلابي", "media": "assets/images/plats/lablebi.mp4"},
      {"word": "سلاطة مشوية", "media": "assets/images/plats/slata_meshwiya.mp4"},
      {"word": "Express", "media": "assets/images/plats/express.jpg"},
    ],
    "التّحيّة": [
      {"word": "عسلامة", "media": "assets/images/greetings/salam.mp4"},
      {"word": "إسمي", "media": "assets/images/greetings/esmi.jpg"},
      {"word": "Merci", "media": "assets/images/greetings/merci.mp4"},
      {"word": "ْيعيشك", "media": "assets/images/greetings/yaayshek.jpg"},
    ],
    "الصفات": [
      {"word": "أصمّ", "media": "assets/images/adjectif/asam.mp4"},
      {"word": "باهي", "media": "assets/images/adjectif/behi.jpg"},
      {"word": "خايب", "media": "assets/images/adjectif/khayeb.mp4"},
      {"word": "طقس سخون", "media": "assets/images/adjectif/skhouna.mp4"},
      {"word": "طقس بارد", "media": "assets/images/adjectif/berda.jpg"},
      {"word": "طويل", "media": "assets/images/adjectif/twil.jpg"},
      {"word": "قصير", "media": "assets/images/adjectif/ksir.jpg"},
      {"word": "فايق", "media": "assets/images/adjectif/fayek.jpg"},
      {"word": "راقد", "media": "assets/images/adjectif/raked.jpg"},
      {"word": "تجاوبني", "media": "assets/images/adjectif/tjewbni.jpg"},
      {"word": "نجاوبك", "media": "assets/images/adjectif/njewbek.jpg"},
      {"word": "مصدوم", "media": "assets/images/adjectif/masdoum.jpg"},
      {"word": "متغشش", "media": "assets/images/adjectif/metghashesh.jpg"},
      {"word": "Ça va", "media": "assets/images/adjectif/cv.mp4"},
      {"word": "تونسي", "media": "assets/images/adjectif/tounsi.mp4"},
      {"word": "يخدم", "media": "assets/images/adjectif/yekhdem.jpg"},
      {"word": "يقرأ", "media": "assets/images/adjectif/yakra.jpg"},
      {"word": "يمشي", "media": "assets/images/adjectif/yemshi.jpg"},
      {"word": "هايج", "media": "assets/images/adjectif/hayej.jpg"},
      {"word": "بالحق", "media": "assets/images/adjectif/belhak.jpg"},
      {"word": "بالشوية", "media": "assets/images/adjectif/beshwaya.jpg"},
      {"word": "فهمتك", "media": "assets/images/adjectif/fhemt.mp4"},
    ],
  };

  late List<Map<String, dynamic>> _questions;
  int _currentQuestionIndex = 0;
  String _feedbackMessage = "";
  Color _feedbackColor = Colors.black;
  VideoPlayerController? _videoController;

  @override
  void initState() {
    super.initState();
    _questions = generateQuestions();
    loadMedia(_questions[_currentQuestionIndex]["media"]);
  }

  @override
  void dispose() {
    _videoController?.dispose();
    super.dispose();
  }

  void loadMedia(String mediaPath) {
    _videoController?.dispose();
    _videoController = null;

    if (mediaPath.endsWith('.mp4')) {
      _videoController = VideoPlayerController.asset(mediaPath)
        ..initialize().then((_) {
          setState(() {});
          _videoController!.play();
          _videoController!.setLooping(true);
        });
    }
  }

  List<Map<String, dynamic>> generateQuestions() {
    final random = Random();
    final allPairs = _wordImagePairs.values.expand((list) => list).toList();
    allPairs.shuffle(random);
    final List<Map<String, dynamic>> questions = [];

    for (var pair in allPairs) {
      final correctWord = pair["word"]!;
      final mediaPath = pair["media"]!;
      final wrongWords = allPairs
          .where((p) => p["word"] != correctWord)
          .map((p) => p["word"]!)
          .toList()
        ..shuffle(random);
      final options = [...wrongWords.take(2), correctWord]..shuffle(random);
      questions.add({
        "media": mediaPath,
        "correct": correctWord,
        "options": options,
      });
    }
    return questions;
  }

  void _checkAnswer(String selectedWord) {
    setState(() {
      if (selectedWord == _questions[_currentQuestionIndex]["correct"]) {
        _feedbackMessage = "أحسنت! إجابة جيدة";
        _feedbackColor = Colors.green[900]!;

        Future.delayed(const Duration(seconds: 1), () {
          setState(() {
            if (_currentQuestionIndex < _questions.length - 1) {
              _currentQuestionIndex++;
              _feedbackMessage = "";
              loadMedia(_questions[_currentQuestionIndex]["media"]);
            }
          });
        });
      } else {
        _feedbackMessage = "عفوا! إجابة خاطئة";
        _feedbackColor = Colors.red[900]!;
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    final question = _questions[_currentQuestionIndex];

    return Scaffold(
      appBar: AppBar(backgroundColor: Colors.purple[100]),
      body: Padding(
        padding: const EdgeInsets.all(20),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Container(
              margin: const EdgeInsets.symmetric(vertical: 10),
              width: 200,
              height: 200,
              decoration: BoxDecoration(
                borderRadius: BorderRadius.circular(12),
                boxShadow: [
                  BoxShadow(
                    color: Colors.black26,
                    blurRadius: 5,
                    offset: const Offset(2, 2),
                  ),
                ],
              ),
              child: ClipRRect(
                borderRadius: BorderRadius.circular(12),
                child: question["media"].endsWith(".mp4") &&
                    _videoController != null &&
                    _videoController!.value.isInitialized
                    ? AspectRatio(
                  aspectRatio: _videoController!.value.aspectRatio,
                  child: VideoPlayer(_videoController!),
                )
                    : Image.asset(question["media"], fit: BoxFit.cover),
              ),
            ),
            const SizedBox(height: 80),
            Column(
              children: question["options"].map<Widget>((option) {
                return Padding(
                  padding: const EdgeInsets.symmetric(vertical: 5),
                  child: CustomButton(
                    text: option,
                    onPressed: () => _checkAnswer(option),
                  ),
                );
              }).toList(),
            ),
            const SizedBox(height: 20),
            Text(
              _feedbackMessage,
              style: TextStyle(
                fontSize: 18,
                fontWeight: FontWeight.bold,
                color: _feedbackColor,
              ),
            ),
          ],
        ),
      ),
    );
  }
}
