import 'package:flutter/material.dart';
import 'package:video_player/video_player.dart';

class VideoPlayerWidget extends StatefulWidget {
  final String videoPath;
  const VideoPlayerWidget({Key? key, required this.videoPath}) : super(key: key);
  //Une Key est un identifiant unique que Flutter utilise pour savoir quel widget
  // correspond à quoi lorsque l’interface est reconstruite.
  // Sans clé, Flutter peut se tromper et réutiliser un ancien widget à la
  // mauvaise position, ce qui cause des bugs visuels ou des états mal conservés.

  @override
  _VideoPlayerWidgetState createState() => _VideoPlayerWidgetState();
}

class _VideoPlayerWidgetState extends State<VideoPlayerWidget> {
  late VideoPlayerController _controller;
  bool _showPlayButton = true;

  @override
  void initState() {
    super.initState();
    _controller = VideoPlayerController.asset(widget.videoPath)
      ..initialize().then((_) {
        setState(() {});
      });
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  void _togglePlayPause() {
    setState(() {
      if (_controller.value.isPlaying) {
        _controller.pause();
        _showPlayButton = true;
      } else {
        _controller.play();
        _showPlayButton = false;
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    return _controller.value.isInitialized
        ? GestureDetector(
      onTap: _togglePlayPause, // tap n'importe où pour jouer/pause
      child: Stack(
        alignment: Alignment.center,
        children: [
          AspectRatio(
            aspectRatio: _controller.value.aspectRatio,
            child: VideoPlayer(_controller),
          ),
          if (_showPlayButton)
            Container(
              color: Colors.black26,
              child: Icon(
                Icons.play_circle_fill,
                size: 30,
                color: Colors.white,
              ),
            ),
        ],
      ),
    )
        : const Center(child: CircularProgressIndicator());
  }
}
