from flask import Flask, request, jsonify

app = Flask(__name__)


def count_vowels(word):
    vowels = "aeiou"
    return sum(1 for char in word if char.lower() in vowels)

# Route to count vowels in words


@app.route('/vowel_count', methods=['POST'])
def vowel_count():
    data = request.get_json()
    if not data or 'words' not in data:
        return jsonify({"error": "Invalid request format"}), 400

    words = data['words']
    result = {word: count_vowels(word) for word in words}
    return jsonify(result)

# Route to sort words


@app.route('/sort', methods=['POST'])
def sort_words():
    data = request.get_json()
    if not data or 'words' not in data or 'order' not in data:
        return jsonify({"error": "Invalid request format"}), 400

    words = data['words']
    order = data['order']

    if order not in ['asc', 'desc']:
        return jsonify({"error": "Invalid order value"}), 400

    sorted_words = sorted(words, reverse=(order == 'desc'))
    return jsonify(sorted_words)


if __name__ == '__main__':
    app.run(debug=True)
