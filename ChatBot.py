#Chat Bot Class
__author__ = 'William Cleghorn'
__version__ = '0.01'
__lastEditDate__ = '3.9.18'

class ChatBot:
  
  def __init__(self):
    self.name = ''
    
    """
    
    These are the ChatBot's conversation checks and responses, these are simple checks and responses and don't legitimately communicate but rather just give a responses
    later plan to add sentence comprehension, topics, train of thought, later use web scraping to pull information about topics. Robot will not form opinions so when asked a
    question it doesn't have an opinion on it will say something along the lines of "i cant say much about that"
    
    """
    self.checkLibrary =[greetingChecks]
    self.responseLibrary = [greetingResponse]
  
    self.greetingChecks = [0,"hi", "hey", "hello"]
    self.greetingResponse = [0,"hi", "hey", "hello"]
   
    self.goodbyeChecks
  
  def respond(self, check, response, strInput):
    
    
    #Add String spacings
    strInput = " " + strInput + " "
    check = " " + check + " "    
    
    
    #Checks in string for word
    if check in strInput:
      return response;
    else:
      return "sorry i cant respond to that";
    
    
  def respondDict(self, checkDict, responseDict, inStr):
    
    for x in range (0, len(checkDict)):
      
      if checkDict[x] in inStr:
        
        return respondDict[randrange(0, len(respondDict))];
                                     
  def analyzeString(self, checkLibrary, responseLibrary, string):
    pass
    
    
