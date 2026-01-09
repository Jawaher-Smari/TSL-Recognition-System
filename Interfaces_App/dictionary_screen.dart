import 'package:flutter/material.dart';
import 'package:tsl_app/widgets/video_player.dart';

class DictionaryScreen extends StatefulWidget {
  const DictionaryScreen({super.key});

  @override
  State<DictionaryScreen> createState() => _DictionaryScreenState();
}

class _DictionaryScreenState extends State<DictionaryScreen> {
  String selectedCategory = "الحروف";

  final Map<String, List<Map<String, String>>> categories = {
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

  @override
  Widget build(BuildContext context) {
    final List<Map<String, String>> currentList = categories[selectedCategory]!;

    return Scaffold(
      backgroundColor: Colors.white,
      appBar: AppBar(
        title: const Directionality(
          textDirection: TextDirection.rtl,
          child: Text('قاموس الإشارات'),
        ),
        centerTitle: true,
        backgroundColor: Colors.purple[100],
        elevation: 3,
      ),
      body: Padding(
        padding: const EdgeInsets.all(10.0),
        child: Column(
          children: [
            SizedBox(
              height: 50,
              child: ListView(
                scrollDirection: Axis.horizontal,
                children: categories.keys.map((category) {
                  final bool isSelected = category == selectedCategory;
                  return Padding(
                    padding: const EdgeInsets.symmetric(horizontal: 6.0),
                    child: ElevatedButton(
                      style: ElevatedButton.styleFrom(
                        backgroundColor: isSelected ? Colors.purple[200] : Colors.grey[200],
                        foregroundColor: isSelected ? Colors.white : Colors.black,
                        shape: RoundedRectangleBorder(
                          borderRadius: BorderRadius.circular(20),
                        ),
                      ),
                      onPressed: () {
                        setState(() {
                          selectedCategory = category;
                        });
                      },
                      child: Text(category, style: const TextStyle(fontSize: 16)),
                    ),
                  );
                }).toList(),
              ),
            ),
            const SizedBox(height: 20),
            Expanded(
              child: SingleChildScrollView(
                scrollDirection: Axis.vertical,
                child: DataTable(
                  columnSpacing: 20,
                  headingRowHeight: 60,
                  dataRowHeight: 130,
                  columns: [
                    DataColumn(
                      label: SizedBox(
                        width: MediaQuery.of(context).size.width * 0.4,
                        child: const Center(
                          child: Text(
                            'الكلمة',
                            style: TextStyle(
                              fontWeight: FontWeight.bold,
                              fontSize: 18,
                              color: Colors.black87,
                            ),
                            textDirection: TextDirection.rtl,
                          ),
                        ),
                      ),
                    ),
                    DataColumn(
                      label: SizedBox(
                        width: MediaQuery.of(context).size.width * 0.4,
                        child: const Center(
                          child: Text(
                            'الصورة / الفيديو',
                            style: TextStyle(
                              fontWeight: FontWeight.bold,
                              fontSize: 18,
                              color: Colors.black87,
                            ),
                            textDirection: TextDirection.rtl,
                          ),
                        ),
                      ),
                    ),
                  ],
                  rows: currentList.map((entry) {
                    String word = entry["word"]!;
                    String mediaPath = entry["media"]!;
                    return DataRow(cells: [
                      DataCell(
                        Center(
                          child: Text(
                            word,
                            style: const TextStyle(
                              fontSize: 20,
                              fontWeight: FontWeight.bold,
                              color: Colors.black87,
                            ),
                            textDirection: TextDirection.rtl,
                          ),
                        ),
                      ),
                      DataCell(
                        Center(
                          child: Container(
                            width: 100,
                            height: 100,
                            decoration: BoxDecoration(
                              borderRadius: BorderRadius.circular(12),
                              boxShadow: [
                                BoxShadow(
                                  color: Colors.black26,
                                  blurRadius: 5,
                                  offset: Offset(2, 2),
                                ),
                              ],
                            ),
                            child: ClipRRect(
                              borderRadius: BorderRadius.circular(12),
                              child: mediaPath.endsWith(".mp4")
                                  ? VideoPlayerWidget(key: UniqueKey(), videoPath: mediaPath)
                                  : Image.asset(
                                mediaPath,
                                width: 100,
                                height: 100,
                                fit: BoxFit.cover,
                              ),
                            ),
                          ),
                        ),
                      ),
                    ]);
                  }).toList(),
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
