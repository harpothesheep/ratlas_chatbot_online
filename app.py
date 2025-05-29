from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

conversation_states = {}

def get_response(user_input, user_id):
    if user_id not in conversation_states:
        conversation_states[user_id] = {"state": "main_menu"}

    state = conversation_states[user_id]["state"]

    if state == "main_menu":
        if user_input.lower() in ["learn about my services", "1", "services"]:
            conversation_states[user_id]["state"] = "services_menu"
            return "You have selected to learn about my services.\nHere are some options:\n1. Python training for treats\n2. DevOps consulting for pets\n3. Cloud migration services for beef patty\n4. Go back to main menu"
        elif user_input.lower() in ["contact my wife ralfa (support)", "2", "contact", "ralfa"]:
            return "You can reach Ralfa (support) at ralfa@ramoyedsarebetterthanyou.com"
        elif user_input.lower() in ["exit", "3"]:
            conversation_states[user_id]["state"] = "exit"
            return "Fine leave then...rupid human!"
        elif user_input.lower() == "ratlas!":
            return "RHAT RELSE COULD YOU ROSSIBLY RANT!"
        elif user_input.lower() == "ralfa!":
            conversation_states[user_id]["state"] = "ralfa_menu"
            return "how may ry help rou darling?\nheres rhat i ran do\n1. emotional support\n2. file a complaint about my rusband\n3. actual enquestions about our ratbot\n4. Go back to main menu"
        else:
            return "Welcome I am ramoyed named Ratlas\nHow can you help me today?\n1. Learn about my services\n2. Contact my wife Ralfa (support)\n3. Exit"

    elif state == "services_menu":
        if user_input in ["1", "python training for treats"]:
            conversation_states[user_id]["state"] = "python_training"
            return "Python training for treats is a great choice!\nHere are some Python training options:\n1. Basic obedience commands\n2. Advanced trick training\n3. Treat-themed coding challenges\n4. Go back to services menu"
        elif user_input in ["2", "devops consulting for pets"]:
            return "DevOps consulting for pets is a runique service!"
        elif user_input in ["3", "cloud migration services for beef patty"]:
            return "Cloud migration services for beef patty is a tasty option...for me!"
        elif user_input in ["4", "go back to main menu"]:
            conversation_states[user_id]["state"] = "main_menu"
            return "Welcome I am ramoyed named Ratlas\nHow can you help me today?\n1. Learn about my services\n2. Contact my wife Ralfa (support)\n3. Exit"
        else:
            return "You have selected to learn about my services.\nHere are some options:\n1. Python training for treats\n2. DevOps consulting for pets\n3. Cloud migration services for beef patty\n4. Go back to main menu"

    elif state == "python_training":
        if user_input in ["1", "basic obedience commands"]:
            return "Basic obedience commands it is!"
        elif user_input in ["2", "advanced trick training"]:
            return "Advanced trick training coming right up!"
        elif user_input in ["3", "treat-themed coding challenges"]:
            return "Treat-themed coding challenges!"
        elif user_input in ["4", "go back to services menu"]:
            conversation_states[user_id]["state"] = "services_menu"
            return "You have selected to learn about my services.\nHere are some options:\n1. Python training for treats\n2. DevOps consulting for pets\n3. Cloud migration services for beef patty\n4. Go back to main menu"
        else:
            return "Here are some Python training options:\n1. Basic obedience commands\n2. Advanced trick training\n3. Treat-themed coding challenges\n4. Go back to services menu"

    elif state == "ralfa_menu":
        if user_input in ["1", "emotional support"]:
            return "I'm ro sorry my rusband has reen mean to you I'll reak rith him"
        elif user_input in ["2", "file a complaint about my rusband"]:
            return "please rill out the rourm ry rill make sure hr reads through rhis"
        elif user_input in ["3", "actual enquestions about our ratbot"]:
            return "ry have never rad romeone actually request this rind of relp im rorry"
        elif user_input in ["4", "go back to main menu"]:
            conversation_states[user_id]["state"] = "main_menu"
            return "Welcome I am ramoyed named Ratlas\nHow can you help me today?\n1. Learn about my services\n2. Contact my wife Ralfa (support)\n3. Exit"
        else:
            return "how may ry help rou darling?\nheres rhat i ran do\n1. emotional support\n2. file a complaint about my rusband\n3. actual enquestions about our ratbot\n4. Go back to main menu"

    elif state == "exit":
        return "Fine leave then...rupid human!"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_input = request.form['user_input']
        user_id = request.remote_addr
        response = get_response(user_input, user_id)
        return jsonify({'response': response})
    except Exception as e:
        return jsonify({'response': 'An error occurred: ' + str(e)})

if __name__ == '__main__':
    app.run(debug=True)