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

class Crisis_Program():

    def __init__(self):

        self.suicide_qestions = {
            "current": "Are you currently having suicidal thoughts or thinking about killing yourself?",
            "plan": "Do you have a plan or a way to kill yourself?",
            "intent": "Do you have access to items you could use to carry out your plan?"
            "score": 0
        }

        self.homicide_qestions = {
            "current": "Are you currently having homicidal thoughts or thinking about killing someone else (Stranger, Friend, Family Member)?",
            "plan": "Do you have a plan or a way to kill someone else?",
            "intent": "Do you have access to items you could use to carry out your plan?",
            "target": "Do you have a specific person you want to kill?"
            "score": 0
        }

        self.psychosis_qestions = {
            "current": "Are you currently hallucinating?",
            "audio": "Are you hearing voices talk to you when you are alone?",
            "visual": "Are you seeing people when you are alone?",
            "commands": "Do the voices you hear tell you to kill or hurt yourself?"
            "score": 0
        }
        
        self.risk_score = 0 
    
