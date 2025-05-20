from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

CHZZK_URL = "https://comm-api.game.naver.com/nng_main/v1/user/getUserStatus"

@app.route("/get_status", methods=["GET"])
def get_status():
    headers = {
        "User-Agent": request.headers.get("User-Agent", "Mozilla/5.0"),
        "Authorization": request.headers.get("Authorization", "")
    }

    try:
        resp = requests.get(CHZZK_URL, headers=headers)
        return jsonify(resp.json()), resp.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run()
