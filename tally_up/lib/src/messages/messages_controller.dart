import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'message_model.dart';
import '../config/api_config.dart';

class MessagesController with ChangeNotifier {
  static final MessagesController _instance = MessagesController._internal();
  factory MessagesController() => _instance;
  MessagesController._internal();
  
  final _apiConfig = ApiConfig();
  List<Message> messages = [];

  Future<void> addMessage(Message message) async {
    messages.add(message);
    
    try {
      final payload = {
        'email': 'randmEmail@example.com',
        'sms_payload': message.toJson()
      };

      final response = await http.post(
        Uri.parse(_apiConfig.messagesUrl),
        headers: {
          'Content-Type': 'application/json',
        },
        body: jsonEncode(payload),
      );

      if (response.statusCode != 200 && response.statusCode != 201) {
        print('Failed to send message to server: ${response.statusCode}');
        print('Response: ${response.body}');
      }
    } catch (e) {
      print('Error sending message to server: $e');
    }

    notifyListeners();
  }
}