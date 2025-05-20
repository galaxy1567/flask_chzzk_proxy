from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/bypass", methods=["GET"])
def bypass():
    try:
        target_url = "https://comm-api.game.naver.com/nng_main/v1/user/getUserStatus"

        headers = {
            "User-Agent": request.headers.get("User-Agent", ""),
            "Authorization": request.headers.get("Authorization", ""),
            "Cookie": request.headers.get("Cookie", "")
        }

        response = requests.get(target_url, headers=headers, timeout=5)
        return jsonify(response.json())

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
