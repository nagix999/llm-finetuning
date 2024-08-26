from prefixer import Prefixer

    
class Option:
    def __init__(self, chioce_string, split_string="\n"):
        self.choice_string = chioce_string
        self.options = self.transform(chioce_string, split_string)
        
    @property
    def count(self):
        return len(self.options) 
    
    def add_prefix(self, prefixer: Prefixer, start: int):
        add_options = [prefixer.add(option, idx) for idx, option in enumerate(self.options, start)]
        return "\n".join(add_options)
        
    def transform(self, chioce_string, split_string="\n"):
        return chioce_string.split(split_string)
    
class MultipleChoiceExam:
    def __init__(self, multiple_choice_questions, ground_truths=None, answers=None, prefixer=None):
        questions = []
        _answers = []
        
        for question, *answer in multiple_choice_questions:
            questions.append(question)
            if answer:
                _answers.append(answer[0])
            
            
        if ground_truths is not None:
            self.ground_truths = ground_truths
            
        if answers is not None:
            self.answers = answers
        else:
            self.answers = _answers
            
        self.questions, options = self._split(questions)
        options = [Option(option) for option in options]
        
        if prefixer is not None:
            self.options = [option.add_prefix(prefixer, 0) for option in options]
        else:
            self.options = options
    
    @property
    def queries(self):
        return [f"{question}\n\n{option}" for question, option in zip(self.questions, self.options)]
        
    def _split(self, multiple_choice_questions):
        splits = [mcq.split("\n\n") for mcq in multiple_choice_questions]
        questions = ["\n\n".join(split[:-1]) for split in splits]
        options = [split[-1] for split in splits]
        return questions, options
    
    def grade(self):
        if len(self.multiple_choice_questions) != len(self.ground_truths) != len(self.answers):
            raise ValueError()
        
        if self.ground_truths is None:
            raise ValueError()
        
        if self.answer is None:
            raise ValueError()
        
        self.marks = [True if gt == answer else False for gt, answer in zip(self.ground_truths, self.answers)]
        return sum(self.marks)