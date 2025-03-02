import 'package:flutter/services.dart';

class SmsReaderPlugin {
  static const _eventChannel = EventChannel('com.example.tally_up/smsStream');
  
  Stream<SmsMessage> smsStream() {
    print("Starting SMS stream...");
    return _eventChannel
        .receiveBroadcastStream()
        .map((dynamic event) {
          print("Raw SMS event received: $event");
          return SmsMessage.fromMap(Map<String, dynamic>.from(event));
        });
  }
}

class SmsMessage {
  final String message;
  final String date;
  final String sender;

  SmsMessage({
    required this.message,
    required this.date,
    required this.sender,
  });

  factory SmsMessage.fromMap(Map<String, dynamic> map) {
    return SmsMessage(
      message: map['message'] ?? '',
      date: map['date'] ?? DateTime.now().toString(),
      sender: map['sender'] ?? 'Unknown',
    );
  }
}
