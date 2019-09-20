class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
      if value >= self.value:
        if  not self.right :
          self.right = BinarySearchTree(value)
        else:
          self.right.insert(value)
      else:
        if value < self.value:
          if not self.left:
            self.left = BinarySearchTree(value)
          else:
            self.left.insert(value)

    def contains(self, target):
      if target == self.value:
        return True
       
      if target > self.value: #Go to the right side
        if not self.right:
          return False
        else:
          return self.right.contains(target)

      if target < self.value:
        if not self.left:
          return False
        else:
          return self.left.contains(target)