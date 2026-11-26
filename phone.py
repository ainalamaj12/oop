class Phone:
     num= 0
     def __init__(self,model,storage,color):
          self.model= model
          self.storage= storage
          self.color= color
          Phone.num +=1