from Rectangle import Rectangle

class Surface:
  def __init__(self, filename, x, y, h, w):
    '''
    Initialize the rectangle object while saving a filename. 
    args: (str, Int) stores the filename of the image as a str. 
    return: (str) The filename. 
    '''
    self.image = filename
    self.rect = Rectangle(x, y, h, w)

  def getRect(self):
    '''
    Returns the rectangle object. 
    args: (str, Int) The rectangle information itself. 
    return: (str) The rectangle object. 
    '''
    return self.rect