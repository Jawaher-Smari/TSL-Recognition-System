import 'package:flutter/material.dart';
import 'package:tflite/tflite.dart';

class DetectionScreen extends StatefulWidget {
  const DetectionScreen({Key? key}) : super(key: key);

  @override
  State<DetectionScreen> createState() => _DetectionScreenState();
}

class _DetectionScreenState extends State<DetectionScreen> {
  bool _modelLoaded = false;
  bool _isRunning = false;

  @override
  void initState() {
    super.initState();
    _loadModel();
  }

  @override
  void dispose() {
    if (_isRunning) {
      _stopDetection();
    }
    Tflite.close();
    super.dispose();
  }

  Future<void> _loadModel() async {
    try {
      String? res = await Tflite.loadModel(
        model: "assets/model/tsl_model.tflite",
      );
      if (res == "Success") {
        setState(() {
          _modelLoaded = true;
        });
        debugPrint("Modèle chargé avec succès");
      } else {
        debugPrint("Erreur lors du chargement du modèle : $res");
      }
    } catch (e) {
      debugPrint("Exception pendant le chargement : $e");
    }
  }

  void _startDetection() {
    if (!_modelLoaded) return;

    setState(() {
      _isRunning = true;
    });
    debugPrint("Détection démarrée");
  }

  void _stopDetection() {
    if (!_modelLoaded) return;

    setState(() {
      _isRunning = false;
    });
    debugPrint("Détection arrêtée");
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Directionality(
          textDirection: TextDirection.rtl,
          child: Text('تصوير الإشارات'),
        ),
        centerTitle: true,
        backgroundColor: Colors.purple[100],
        elevation: 3,
      ),
      body: Column(
        children: [
          Expanded(
            flex: 2,
            child: Container(
              width: double.infinity,
              color: Colors.grey.shade200,
              child: Center(
                child: !_modelLoaded
                    ? Column(
                  mainAxisSize: MainAxisSize.min,
                  children: const [
                    CircularProgressIndicator(),
                    SizedBox(height: 12),
                    Text(
                      "...جاري التّحميل",
                      style: TextStyle(fontSize: 16),
                    ),
                  ],
                )
                    : Text(
                  _isRunning
                      ? "Le modèle est chargé et la détection est : ACTIVÉE"
                      : "Le modèle est chargé et la détection est : ARRÊTÉE",
                  textAlign: TextAlign.center,
                  style: TextStyle(
                    fontSize: 18,
                    color: _isRunning ? Colors.green : Colors.orange,
                    fontWeight: FontWeight.w500,
                  ),
                ),
              ),
            ),
          ),
          Expanded(
            flex: 1,
            child: Padding(
              padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 8),
              child: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  ElevatedButton(
                    onPressed: (!_modelLoaded || _isRunning) ? null : _startDetection,
                    style: ElevatedButton.styleFrom(
                      padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 12),
                      backgroundColor: Colors.green[300],
                      shape: RoundedRectangleBorder(
                        borderRadius: BorderRadius.circular(8),
                      ),
                    ),
                    child: const Text(
                      "ابدأ التصوير",
                      style: TextStyle(fontSize: 16),
                    ),
                  ),
                  const SizedBox(height: 16),
                  ElevatedButton(
                    onPressed: (!_modelLoaded || !_isRunning) ? null : _stopDetection,
                    style: ElevatedButton.styleFrom(
                      padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 12),
                      backgroundColor: Colors.red[300],
                      shape: RoundedRectangleBorder(
                        borderRadius: BorderRadius.circular(8),
                      ),
                    ),
                    child: const Text(
                      "أوقف التصوير",
                      style: TextStyle(fontSize: 16),
                    ),
                  ),
                ],
              ),
            ),
          ),
        ],
      ),
    );
  }
}
