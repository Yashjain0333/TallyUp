import 'package:flutter/material.dart';
import '../home/home_view.dart';

class LoginController extends ChangeNotifier {
  final formKey = GlobalKey<FormState>();
  final emailController = TextEditingController();
  final passwordController = TextEditingController();
  
  bool _isLoading = false;
  bool get isLoading => _isLoading;
  set isLoading(bool value) {
    _isLoading = value;
    notifyListeners();
  }

  void handleLogin(BuildContext context) async {
    if (!formKey.currentState!.validate()) return;

    isLoading = true;
    await Future.delayed(const Duration(seconds: 1));
    isLoading = false;

    if (context.mounted) {
      Navigator.of(context).pushNamedAndRemoveUntil(
        HomeView.routeName,
        (route) => false,
      );
    }
  }

  @override
  void dispose() {
    emailController.dispose();
    passwordController.dispose();
    super.dispose();
  }
}