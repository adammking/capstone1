


class Question:
    """Question on a questionnaire."""

    def __init__(self, question, choices=None, allow_text=False):
        """Create question (assume Yes/No for choices."""

        if not choices:
            choices = ["Yes", "No"]

        self.question = question
        self.choices = choices
        self.allow_text = allow_text

class Crisis_Program():
    
    def __init__(self, title, questions):

        self.questions = questions
        self.title = title

    def calculate_score(responses):
        score = 0
        for itm in responses:
            if itm == "Yes":
                score += 1
        return score

crisis = Crisis_Program(
    "Crisis Program",
    [
    Question("Are you currently having suicidal thoughts or thinking about killing yourself?"),
    Question("Are you currently having homicidal thoughts or thinking about killing someone else (Stranger, Friend, Family Member)?"),
    Question("Are you currently hallucinating? (Hearing or seeing things when alone)")
    ]
)





        
    

    
