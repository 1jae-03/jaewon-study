from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/api/get-test", methods=['GET'])
def getTest():

    print("API 호출 발생!")

    response = {
        "result": "성공하였습니다!"
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)