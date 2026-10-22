class AtbashCipher {
  static const String _alphabet = 'abcdefghijklmnopqrstuvwxyz';
  static final String _reversedAlphabet = _alphabet.split('').reversed.join();

  static final Map<String, String> _cipherMap = {
    for (var i = 0; i < _alphabet.length; i++)
      _alphabet[i]: _reversedAlphabet[i],
  };

  /// Encodes plaintext into grouped ciphertext.
  String encode(String plaintext, [int groupSize = 5]) {
    final cleanedChars = _transform(plaintext);
    final buffer = StringBuffer();

    for (var i = 0; i < cleanedChars.length; i++) {
      if (i > 0 && i % groupSize == 0) {
        buffer.write(' ');
      }
      buffer.write(cleanedChars[i]);
    }

    return buffer.toString();
  }

  /// Decodes ciphertext back into plaintext.
  String decode(String ciphertext) {
    return _transform(ciphertext).join();
  }

  /// Internal transformation engine.
  List<String> _transform(String input) {
    final result = <String>[];

    for (final char in input.toLowerCase().codeUnits) {
      final strChar = String.fromCharCode(char);

      if (_cipherMap.containsKey(strChar)) {
        result.add(_cipherMap[strChar]!);
      } else if (char >= 48 && char <= 57) {
        // ASCII check for '0'-'9'
        result.add(strChar);
      }
    }

    return result;
  }
}