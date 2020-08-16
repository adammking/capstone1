"""
Crisis Program Outline: 
Questions:  Are you currently having suicidal thoughts or thinking about killing yourself?
                - Do you have a plan or a way to kill yourself?
                - Do you have access to items you could use to carry out your plan?

            Are you currenty having homicidal thoughts or thinking about killing someone else (Stranger, Friend, Family Member)?
                - Do you have a plan or a way to kill someone else?
                - Do you have access to items you could use to carry out your plan?

            Are you currently hallucinating?
                -Are you  hearing voices talk to you when you are alone?
                    -Do the voices you hear tell you to kill or hurt yourself?
                -Are you seeing people when you are alone?

            Have you used any alcohol or Illegal drugs (not prescibed) today/night?
            
Other needed info: risk_score = int
"""


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

    def calculate_score(self, lst):
        score = 0
        for itm of lst:
            if itm == "Yes":
                score + 1
        return score

    crisis = Crisis_Program(
        "Crisis Program",
     [
        Question("Are you currently having suicidal thoughts or thinking about killing yourself?"),
        Question("Are you currently having homicidal thoughts or thinking about killing someone else (Stranger, Friend, Family Member)?"),
        Question("Are you currently hallucinating?")
    ]


        
    

    
