def capitalize_words(sentence):
    words = sentence.split()
    capitalized_words = [word.capitalize() for word in words]
    capitalized_sentence = ' '.join(capitalized_words)
    return capitalized_sentence
  
  

new_sentence = input("")
capitalized_sentence = capitalize_words(new_sentence)
print("Capitalized sentence:", capitalized_sentence)
