import 'package:flutter/material.dart';
import 'package:permission_handler/permission_handler.dart';
import 'package:tally_up/src/messages/messages_controller.dart';
import 'package:tally_up/src/messages/message_model.dart';
import 'settings/settings_controller.dart';
import 'settings/settings_view.dart';
import 'login/login_view.dart';
import 'login/signup_view.dart';
import 'home/home_view.dart';
import 'plugins/sms_reader_plugin.dart';
import 'messages/messages_view.dart';

/// The Widget that configures your application.
class MyApp extends StatefulWidget {
  const MyApp({
    super.key,
    required this.settingsController,
  });

  final SettingsController settingsController;

  @override
  State<MyApp> createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {

  @override
  void initState() {
    super.initState();
    getPermission().then((value) async {
      print("SMS Permission status: $value");
      if (value) {
        final messages = await SmsReaderPlugin().readMonthSMS();
        for (var msg in messages) {
          MessagesController().addMessage(Message(
            content: msg.message,
            time: msg.date,
            sender: msg.sender,
            type: MessageType.uncategorized,
          ));
          break;
        }
      }
    });
  }

  @override
  void dispose() {
    // Clean up any controllers or subscriptions here
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      initialRoute: '/signup',  // Change this line
      onGenerateRoute: (RouteSettings routeSettings) {
        return MaterialPageRoute<void>(
          settings: routeSettings,
          builder: (BuildContext context) {
            switch (routeSettings.name) {
              case SignupView.routeName:
                return const SignupView();
              case LoginView.routeName:
                return const LoginView();
              case HomeView.routeName:
                return const HomeView();
              case SettingsView.routeName:
                return SettingsView(controller: widget.settingsController);
              case MessagesView.routeName:
                return const MessagesView();
              default:
                return const SignupView();
            }
          },
        );
      },
    );
  }

  Future<bool> getPermission() async {
    if (await Permission.sms.status == PermissionStatus.granted) {
      return true;
    } else {
      if (await Permission.sms.request() == PermissionStatus.granted) {
        return true;
      } else {
        return false;
      }
    }
  }
}
