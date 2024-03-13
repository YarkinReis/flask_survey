from flask import Flask , render_template ,redirect , session ,flash , request
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app=Flask(__name__,template_folder='templates')
app.config['SECRET_KEY'] = "secret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

RESPONSES_KEY = "responses"

@app.route("/")
def show_survey():
    """Please Select Survey"""

    return render_template("survey.html",survey=survey)

@app.route("/questions/<int:id>")
def show_question(mid):
    """Display question"""
    responses = session.get(RESPONSES_KEY)

    if (responses is None):
        return redirect("/")
    
    if (len(responses) != mid):
        flash(f"Invalid question id: {mid}")
        return redirect(f"/questions/{len(responses)}")
    
    if (len(responses) == mid):
        return redirect("/complete")
    
    question = survey.questions[mid]
    return render_template("questions.html", questions_num=mid)

@app.route("/complete")
def complete():
    """Survey completed"""
    return render_template("completion.html")

