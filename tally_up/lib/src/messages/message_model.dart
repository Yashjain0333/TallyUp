import 'package:flutter/material.dart';

class Message {
  final String title;
  final String content;
  final String time;
  final String sender;
  final MessageType type;

  Message({
    required this.content,
    required this.time,
    required this.sender,
    this.title = '',
    this.type = MessageType.uncategorized,
  });

  Map<String, String> toJson() {
    return {
      'content': content,
      'time': time,
      'sender': sender,
      'type': type.toString(),
    };
  }
}

enum MessageType {
  payment(Icons.payment, Color(0xFF1E88E5)),
  bill(Icons.warning_amber, Colors.orange),
  budget(Icons.restaurant, Colors.red),
  subscription(Icons.subscriptions, Colors.purple),
  investment(Icons.trending_up, Colors.green),
  uncategorized(Icons.network_cell, Colors.grey);


  final IconData icon;
  final Color color;

  const MessageType(this.icon, this.color);
}