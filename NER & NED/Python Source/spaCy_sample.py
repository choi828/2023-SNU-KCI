import spacy
# from spacy import displacy

nlp = spacy.load('en_core_web_sm')
text = u'Apple is looking at buying U.K. startup for $1 billion'
doc = nlp(text)

for token in doc:
    print(token.text, token.lemma_, token.pos_)

# displacy.render(doc, style="ent", auto_switch_port=True)

# text = "What video sharing service did Steve Chen, Chad Hurley, and Jawed Karim create in 2005?"
 
# from spacy import displacy
# displacy.render(doc, style="ent", jupyter=True)


# import spacy
# from spacy import displacy

# nlp = spacy.load("en_core_web_sm")
# doc = nlp("This is a sentence.")
# displacy.serve(doc, style="ent")