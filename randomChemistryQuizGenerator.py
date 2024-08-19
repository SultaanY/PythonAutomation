# randomChemistryQuizGenerator = Do you know your elements
import random
# The quiz data. Keys are symbols and values are their Chemicals.
elements = {
    "H": "Hydrogen",
    "He": "Helium",
    "Li": "Lithium",
    "Be": "Beryllium",
    "B": "Boron",
    "C": "Carbon",
    "N": "Nitrogen",
    "O": "Oxygen",
    "F": "Fluorine",
    "Ne": "Neon",
    "Na": "Sodium",
    "Mg": "Magnesium",
    "Al": "Aluminum",
    "Si": "Silicon",
    "P": "Phosphorus",
    "S": "Sulfur",
    "Cl": "Chlorine",
    "Ar": "Argon",
    "K": "Potassium",
    "Ca": "Calcium",
    "Sc": "Scandium",
    "Ti": "Titanium",
    "V": "Vanadium",
    "Cr": "Chromium",
    "Mn": "Manganese",
    "Fe": "Iron",
    "Co": "Cobalt",
    "Ni": "Nickel",
    "Cu": "Copper",
    "Zn": "Zinc",
    "Ga": "Gallium",
    "Ge": "Germanium",
    "As": "Arsenic",
    "Se": "Selenium",
    "Br": "Bromine",
    "Kr": "Krypton",
    "Rb": "Rubidium",
    "Sr": "Strontium",
    "Y": "Yttrium",
    "Zr": "Zirconium",
    "Nb": "Niobium",
    "Mo": "Molybdenum",
    "Tc": "Technetium",
    "Ru": "Ruthenium",
    "Rh": "Rhodium",
    "Pd": "Palladium",
    "Ag": "Silver",
    "Cd": "Cadmium",
    "In": "Indium",
    "Sn": "Tin",
    "Sb": "Antimony"
}

elementItems = list(elements.items()) #returns each item as a tuple

# Generate any number of quiz files and associated answer file
for quizNum in range(2):
    quizFile = open('elementsquiz%s.txt' % (quizNum + 1), 'w')
    answerKeyFile = open('elementsquiz_answers%s.txt' % (quizNum +1), 'w')

    quizFile.write('Name:\n\nDate:\n\nClass:\n\n')
    quizFile.write((' '* 20) + 'State Capitals Quiz (Form %s)' % (quizNum+1))
    quizFile.write('\n\n')

    symbols = list(elements.keys())
    random.shuffle(symbols)

    # Loop through 50 chemical symbols, make a question for each

    for questionNum in range(50):

        correctAnswer = elements[symbols[questionNum]]
        wrongAnswers = list(elements.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        quizFile.write('%s. What is the chemical name of %s?\n' % (questionNum +1,symbols[questionNum]))
        for i in range(4):
            quizFile.write('     %s. %s\n' % ('ABCD'[i], answerOptions[i]))
        quizFile.write('\n')
        
        #write the answer to answer key sheet
        answerKeyFile.write('%s.  %s\n' % (questionNum + 1, 'ABCD' [answerOptions.index(correctAnswer)]))
    quizFile.close()
    answerKeyFile.close()