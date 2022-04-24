class Rectangle: 
  def __init__(self, x=0, y=0, h=0, w=0):
    '''
    Initialize the rectangle object. 
    args: (Int) The rectangle parameters. 
    return: (Int) Saves them as instance variables. 
    '''
    if x<0: 
      x=0
    if y<0: 
      y=0
    if h<0: 
      h=0
    if w<0: 
      w=0
    self.x = x
    self.y = y
    self.height = h
    self.width = w 

  def __str__(self):
    '''
    Initialize the rectangle object while saving a filename. 
    args: (str, Int) Sets the rectangle up. 
    return: (str) Rectangles top length, bottom length, height and width as strings. 
    '''
    return 'top x =' + str(self.x) + ', bottom y =' + str(self.y) + ', height h ='+ str(self.height) + ', width = ' + str(self.width)