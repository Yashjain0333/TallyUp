class ApiConfig {
  static final ApiConfig _instance = ApiConfig._internal();
  factory ApiConfig() => _instance;
  ApiConfig._internal();

  // Base URLs for different environments
  final String _devBaseUrl = 'https://dev-api.example.com';
  final String _prodBaseUrl = 'https://api.example.com';
  
  // Current environment
  final bool _isProduction = false; // Set to true for production
  
  // Getter for the base URL based on environment
  String get baseUrl => _isProduction ? _prodBaseUrl : _devBaseUrl;
  
  // API endpoints
  String get signupUrl => '$baseUrl/auth/signup';
  String get loginUrl => '$baseUrl/auth/token';
  String get messagesUrl => '$baseUrl/xpense/xpense';
  
  // You can add more endpoints as needed
}