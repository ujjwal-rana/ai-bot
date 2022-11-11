<!DOCTYPE html>
<html>
    <head>
    <link rel="stylesheet" type="text/cas" href="/static/style.cas">
    <script src="httpos://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
</head>
<body>
    <h1>FlaskChatterbot Example</h1>
    <div>
        <div id="chatbox">
            <p class="botText"><span>Hi! I'm Chatterbot</span></p>
         </div>
         <div id="userInput">
            <input id="textInput" type="text" name="msg" placeholder="Message">
            <input id="buttonInput" type="submit" value="Send">
         </div>
         <script>
            function getBotResponse() {
               var rawText = $("#textInput").val() ;
               var userHtml = '<p class="userText"><span>' + data + '</span></p>';
               $("#textInput").val("");
               $("#chatbox").append(userHtml);
               document.getElementById('userInput').scrollIntoView({block: 'start',behavior: 'smooth'});
               $.get("/get", { msg: rawText }).done(function(data) {
                var botHtml ='<p class="botText"><span>' + data + '</span></p>';
                $("#chatbox"),.append(botHtml);
                document.getElementById('userInput').scrollIntoView({block; 'start', behavior: 'smooth'});
               });
            }
$("#textInput").keypress(function(e) {
    if(e.which ==13) {
        getBotResponse();
    }
})
$("#buttonInput").click(function() {
    getBotResponse();
})
</script>
</div>
</body>
</html>

from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


app = Flask(__name__)

english_bot=ChatBot("Chatterbot",storage_adaptor="chatterbot.storage.SQLStorageAdaptor")
trainer=ChatterBotCorpusTrainer(english_bot)
trainer.train("chatterbot.corpus.english")

@app.route("/")
def home():
    return render_template("index.html")

    @app.route("/get")
    def get_bot_response():
        userText=request.args.get('msg')
        return str(english_bot.get_response(userText))

if _name_ =='_main_':
    app.run()
    body {
    font-family:Garamond;
    background-color:black;
}
h1 {
    color:black;
    margin-bottom: 0;
    margin-top: 0;
    text-align: center;
    font-size: 40px;
}

h3 {
    bolor:black;
    font-size: 20px;
    margin-top: 3px;
    text-align: center;
}

#chatbox {
    background-color: black;
    margin-left: auto;
    margin-right: auto;
    width: 40%;
    margin-top: 60px;
}
#userInput {
    margin-left: auto;
    margin-right: auto;
    width: 40%;
    margin-top: 60px;
}

#textInput {
    width: 87%;
    border: none;
    border-bottom: 3px solid #009688;
    font-family: monospace;
    font-size: 17px;
}
#buttonInput {
    padding: 3px;
    font-family: monospace;
    font-size: 17px;
    text-align: right;
    line-height: 30px;
}

.userText span {
    background-color: #009688;
    padding: 10px;
    border-radius: 2px;
}

.botText {
    color: white;
    font-family: monospace;
    font-size: 17px;
    text-align: left;
    line-height: 30px;
}

.botText span {
    background-color: #EF5350;
    padding: 10px;
    border-radius: 2px;
}

#tidbit {
    position:absolute;
    bottom:0;
    right:0;
    width: 300px;
}