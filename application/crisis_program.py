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
    
    suicide_questions = [
        Question("Are you currently having suicidal thoughts or thinking about killing yourself?"),
        Question("Do you have a plan or a way to kill yourself?"),
        Question("Do you have access to items you could use to carry out your plan?")
    ]

    homicide_questions = [
        Question("Are you currently having homicidal thoughts or thinking about killing someone else (Stranger, Friend, Family Member)?"),
        Question("Do you have a plan or a way to kill someone else?"),
        Question("Do you have access to items you could use to carry out your plan?"),
        Question("Do you have a specific person you want to kill?")
    ]

    psychosis_questions = [
        Question("Are you currently hallucinating?"),
        Question("Are you hearing voices talk to you when you are alone?"),
        Question("Are you seeing people when you are alone?"),
        Question("Do the voices you hear tell you to kill or hurt yourself?")
    ]

        
    

    
