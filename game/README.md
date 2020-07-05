# Define function
def get_bow_from_docs(docs, stop_words=[]):
    
    # In the function, first define the variables you will use such as `corpus`, `bag_of_words`, and `term_freq`.
    corpus = []
    bag_of_words = []
    term_freq = []
    
    
    """
    Loop `docs` and read the content of each doc into a string in `corpus`.
    Remember to convert the doc content to lowercases and remove punctuation.
    """
    for doc in docs:
        with open(doc, 'r') as file:
            corpus.append(file.read().replace('\n', ''))

    # Remove commas and low all the letters
    corpus = [ line.replace('.','').lower() for line in corpus]

    '''for doc in docs:
        #read the content of the file and add it to corpus
        file = open(doc,'r')
        text= file.read().replace('\n', '')
        
        #convert to lowercases
        text = text.lower()
        
        #split into wordy by white space
        corpus += text.split()
        
        #close the file
        file.close()
 
      
    #remove punctuation from each word
    table = str.maketrans('', '', string.punctuation)
    corpus = [word.translate(table) for word in corpus] '''
    
    
    """
    Loop `corpus`. Append the terms in each doc into the `bag_of_words` array. The terms in `bag_of_words` 
    should be unique which means before adding each term you need to check if it's already added to the array.
    In addition, check if each term is in the `stop_words` array. Only append the term to `bag_of_words`
    if it is not a stop word.
    """
    
    #convert the list with the stop words to a set
    stop_words_set = set(stop_words)
    
    # Fill up the BoW
    for line in corpus:
        line = line.split()
        for word in line:
            if (word not in bag_of_words) and (word not in stop_words):
                bag_of_words.append(word)
    
    
    """
    Loop `corpus` again. For each doc string, count the number of occurrences of each term in `bag_of_words`. 
    Create an array for each doc's term frequency and append it to `term_freq`.
    """
    
    for line in corpus:
        line = line.split()
    
        # auxiliar variable
        aux = []
        
        for word in bag_of_words:
            aux.append(line.count(word))    
        term_freq.append(aux)
    
    # Now return your output as an object
    return {
        "bag_of_words": bag_of_words,
        "term_freq": term_freq
    }
    