## Class definitions to represent a SUTime entity
#
# Date: 9/23/17
#
# Programmer Name: Amy Olex

import json

## Class to define a SUTime entity parsed from the json output of SUTime
# @author Amy Olex
# @param id Unique numerical ID
# @param text The text parsed out by SUTime
# @param start_span The location of the first character
# @param end_span The location of the last character
# @param type The type of temporal entity parsed by SUTime.  Can be one of DATE, TIME, SET, DURATION, RANGE...I think!
# @param value The normalized date/time value from SUTime.
class sutimeEntity :
    
    ## The constructor
    def __init__(self, id, text, start_span, end_span, sutype, suvalue) :
        self.id = id
        self.text = text
        self.start_span = start_span
        self.end_span = end_span
        self.sutype = sutype
        self.suvalue = suvalue
      
    ## String representation    
    def __str__(self) :
        span_str = "" if self.start_span is None else (" <" + str(self.start_span) + "," + str(self.end_span) + "> ")
        return str(self.id) + " " + self.text + span_str + self.sutype  + " " + self.suvalue
    

    #### Methods to SET properties ###
    
    ## Sets the entity's ID
    #  @param id The ID to set it to
    def setID(self, id) :
        self.id = id

    ## Sets the entity's text
    #  @param text The text to set it to
    def setText(self, text) :
        self.text = text
        
    ## Sets the entity's span
    #  @param start The start index
    #  @param end The ending index
    def setSpan(self, start, end) :
        self.start_span = start
        self.end_span = end
        
    ## Sets the entity's type
    #  @param sutype The type of SUTime temporal expression
    def setPos(self, sutype) :
        self.sutype = sutype
        
    ## Sets the entity's SUTime normalized value
    #  @param suvalue The entities normalized SUTime value
    def setTemporal(self, suvalue) :
        self.suvalue = suvalue
        
    #### Methods to GET properties ####
    
    ## Gets the entity's ID
    def getID(self) :
        return(self.id)
        
    ## Gets the entity's text
    def getText(self) :
        return(self.text)
        
    ## Gets the entity's span
    def getSpan(self) :
        return(self.start_span, self.end_span)
        
    ## Gets the entity's sutype
    def getPos(self, sutype) :
        return(self.sutype)
        
    ## Gets the entity's suvalue
    def isTemporal(self, suvalue) :
        return(self.suvalue)

## Function to convert json output of sutime to a list of sutimeEntities
# @author Amy Olex
# @param sut_json The SUTime parsed json string (required)
# @param id_counter The number the ID counter should start at. Default is 0.
# @output A list of sutimeEntity objects in the same order as the input json list.
def import_SUTime(sut_json, id_counter=0) :
    su_list = []
    for j in sut_json:
        su_list.append(sutimeEntity(id=id_counter, text=j['text'], start_span=j['start'], end_span=j['end'], sutype=j['type'], suvalue=j['value']))
        id_counter = id_counter +1
        
    return su_list
