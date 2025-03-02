import 'package:flutter/material.dart';
import 'package:flutter_gen/gen_l10n/app_localizations.dart';
import 'package:flutter_localizations/flutter_localizations.dart';
import 'package:permission_handler/permission_handler.dart';
import 'package:tally_up/src/messages/messages_controller.dart';
import 'package:tally_up/src/messages/message_model.dart';
import 'settings/settings_controller.dart';
import 'settings/settings_view.dart';
import 'login/login_view.dart';
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
    getPermission().then((value) {
      print("SMS Permission status: $value");
      if (value) {
        print("Starting SMS listener...");
        SmsReaderPlugin().smsStream().listen(
          (event) {
            print("SMS Received: ${event.message} from ${event.sender}");
            MessagesController().addMessage(Message(
              content: event.message,
              time: event.date,
              sender: event.sender,
            ));
          },
          onError: (error) {
            print("SMS Stream error: $error");
          },
        );
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
    return ListenableBuilder(
      listenable: widget.settingsController,
      builder: (BuildContext context, Widget? child) {
        return MaterialApp(
          // Providing a restorationScopeId allows the Navigator built by the
          // MaterialApp to restore the navigation stack when a user leaves and
          // returns to the app after it has been killed while running in the
          // background.
          restorationScopeId: 'app',

          // Provide the generated AppLocalizations to the MaterialApp. This
          // allows descendant Widgets to display the correct translations
          // depending on the user's locale.
          localizationsDelegates: const [
            AppLocalizations.delegate,
            GlobalMaterialLocalizations.delegate,
            GlobalWidgetsLocalizations.delegate,
            GlobalCupertinoLocalizations.delegate,
          ],
          supportedLocales: const [
            Locale('en', ''), // English, no country code
          ],

          // Use AppLocalizations to configure the correct application title
          // depending on the user's locale.
          //
          // The appTitle is defined in .arb files found in the localization
          // directory.
          onGenerateTitle: (BuildContext context) =>
              AppLocalizations.of(context)!.appTitle,

          // Define a light and dark color theme. Then, read the user's
          // preferred ThemeMode (light, dark, or system default) from the
          // SettingsController to display the correct theme.
          theme: ThemeData(),
          darkTheme: ThemeData.dark(),
          themeMode: widget.settingsController.themeMode,

          // Define a function to handle named routes in order to support
          // Flutter web url navigation and deep linking.
          // Add initialRoute
          initialRoute: LoginView.routeName,

          onGenerateRoute: (RouteSettings routeSettings) {
            return MaterialPageRoute<void>(
              settings: routeSettings,
              builder: (BuildContext context) {
                switch (routeSettings.name) {
                  case LoginView.routeName:
                    return const LoginView();
                  case HomeView.routeName:
                    return const HomeView();
                  case SettingsView.routeName:
                    return SettingsView(controller: widget.settingsController);
                  case MessagesView.routeName:
                    return const MessagesView();
                  default:
                    return const LoginView();
                }
              },
            );
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
