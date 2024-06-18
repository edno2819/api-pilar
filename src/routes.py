from flask import request, jsonify, current_app as app
from .utils import vowal
from .cache import cache, make_cache_key


@app.route('/', methods=['GET'])
def hellou():
    result = {"msg": "Hellou world!"}
    return jsonify(result)


@app.route('/vowel_count', methods=['POST'])
@cache.cached(timeout=60, key_prefix=make_cache_key)
def vowel_count():
    """
    Endpoint to count vowels in a list of words.

    Expected JSON format:
    {
        "words": ["word1", "word2", ...]
    }

    Returns:
        JSON with the count of vowels for each word.
    """
    data = request.get_json()
    if not data or 'words' not in data or not isinstance(data['words'], list):
        return jsonify({"error": "Invalid request format"}), 400

    words = data['words']
    if not all(isinstance(word, str) for word in words):
        return jsonify({"error": "All elements in 'words' must be strings"}), 400

    try:
        result = {}
        for word in words:
            result[word] = vowal.count_vowels(word)
    except Exception as e:
        app.logger.error('Error processing words: %s', e)
        return jsonify({"error": "An error occurred while processing words"}), 500

    return jsonify(result)


@app.route('/sort', methods=['POST'])
@cache.cached(timeout=60, key_prefix=make_cache_key)
def sort_words():
    """
    Endpoint to sort a list of words.

    Expected JSON format:
    {
        "words": ["word1", "word2", ...],
        "order": "asc" or "desc" (optional, default is "asc")
    }

    Returns:
        JSON with the sorted list of words.
    """
    data = request.get_json()
    if not data or 'words' not in data or not isinstance(data['words'], list):
        return jsonify({"error": "Invalid request format"}), 400

    words = data['words']
    if not all(isinstance(word, str) for word in words):
        return jsonify({"error": "All elements in 'words' must be strings"}), 400

    order = data.get('order', 'asc')

    if order not in ['asc', 'desc']:
        app.logger.info('Invalid order option: %s', order)
        return jsonify({"error": "Invalid order option"}), 400

    sorted_words = sorted(words, reverse=(order == 'desc'))
    return jsonify(sorted_words)


@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404


@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({"error": "Method not allowed"}), 405
