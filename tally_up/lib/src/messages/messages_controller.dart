import 'package:flutter/material.dart';
import 'message_model.dart';

class MessagesController with ChangeNotifier {
  static final MessagesController _instance = MessagesController._internal();
  factory MessagesController() => _instance;
  MessagesController._internal();
  
  List<Message> messages = [
    // Message(
    //   title: 'Payment Received',
    //   content: 'You received \$500 from John',
    //   time: '2m ago',
    //   type: MessageType.payment,
    // ),
    // Message(
    //   title: 'Bill Due',
    //   content: 'Electricity bill due in 2 days',
    //   time: '1h ago',
    //   type: MessageType.bill,
    // ),
    // Message(
    //   title: 'Budget Alert',
    //   content: 'You\'re close to your food budget',
    //   time: '3h ago',
    //   type: MessageType.budget,
    // ),
    // Message(
    //   title: 'Subscription Renewal',
    //   content: 'Netflix subscription will renew tomorrow',
    //   time: '5h ago',
    //   type: MessageType.subscription,
    // ),
    // Message(
    //   title: 'Investment Update',
    //   content: 'Your stocks are up by 3.2% today',
    //   time: '8h ago',
    //   type: MessageType.investment,
    // ),
  ];

  void addMessage(Message message) {
    messages.add(message);
    notifyListeners();
  }
}