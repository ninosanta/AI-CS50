from logic import *

rain = Symbol("rain")  # It is raining
hagrid = Symbol("hagrid")  # Harry visited Hagrid
dumbledore = Symbol("dumbledore")  # Harry visited Dumbledore

sentence = And(rain,hagrid)  # And object
print("Ran AND Hagrid - Fromula: " + sentence.formula())

knowledge = And(  # and of multiple sentences
    Implication(Not(rain), hagrid),  # Not rain -> Harry visited Hagrid
    Or(hagrid, dumbledore),  # Harry visited Hagrid or Dumbledore
    Not(And(hagrid, dumbledore)),  # Harry did not visit both Hagrid and Dumbledore
    dumbledore  # Harry visited Dumbledore
)

print("Knowledge Base: " + knowledge.formula())
print("Is it raining? - Model Check:", model_check(knowledge, rain))
print(f"Is it raining? - Model Check: {model_check(knowledge, hagrid)}")
