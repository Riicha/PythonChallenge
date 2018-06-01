paragraphs ="""Adam Wayne, the conqueror, with his face flung back and his mane like a lion's, 
stood with his great sword point upwards, the red raiment of his office flapping 
around him like the red wings of an archangel. And the King saw, he knew not how, 
something new and overwhelming. The great green trees and the great red robes swung 
together in the wind. The preposterous masquerade, born of his own mockery, towered 
over him and embraced the world. This was the normal, this was sanity, this was nature,
 and he himself, with his rationality, and his detachment and his black frock-coat, he 
was the exception and the accident - a blot of black upon a world of crimson and gold."""
sentences = paragraphs.split(".")

# Counting the number of sentences
theSentenceCounter = 0
for theSentence in sentences:
    if (theSentence != ''): # check for space 
        theSentenceCounter += 1 # sentence counter


# Counting the number of words
words =[] 
for sentence in sentences:
   words.append(sentence.split(" ")) # splitting the sentences on every " "
iSentenceCounter = 0
totalWords = 0 

# total number of words 
for word in words:
    totalWords += len(words[iSentenceCounter])
    #print("Words in Sentence :" +str(iSentenceCounter) +str(len(words.count())))
    iSentenceCounter += 1


print ("Paragraph Analysis")
print("-------------------------------")
print("Approximate Word Count: " + str(totalWords))
print("Approximate Sentence Count new: " +str(theSentenceCounter))
print("Average Letter Count: " + str(sum([len(x) for x in paragraphs.split(" ")])/len(sentences)))
print("Average Sentence Length: " + str(totalWords/len(sentences)))

