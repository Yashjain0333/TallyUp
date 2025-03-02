import 'package:flutter/services.dart';

class SmsReaderPlugin {
  static const _methodChannel = MethodChannel('com.example.tally_up/sms');
  
  Future<List<SmsMessage>> readMonthSMS() async {
    try {
      final List<dynamic> messages = await _methodChannel.invokeMethod('readMonthSMS');
      return messages.map((msg) => SmsMessage.fromMap(Map<String, dynamic>.from(msg))).toList();
    } catch (e) {
      print("Error reading SMS: $e");
      return [];
    }
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
