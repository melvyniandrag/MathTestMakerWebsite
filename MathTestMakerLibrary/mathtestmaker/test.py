from mathtestmaker import MathTestMaker
from customPrettyPrinter import CustomPrettyPrinter

testmaker = MathTestMaker()
question_requests = \
		[
			{
				'category': 'linear_equations',
				'name': 'Find the integer x intercept of a line in slope intercept form with nonzero slope.',
				'numChoices': 4,
				'points': 10
			},
		]
questions, errors = testmaker.getSelectedQuestions( question_requests )
for i, q in enumerate(questions):
    print("================ {} ===================".format(i))
    CustomPrettyPrinter().pprint(q)

