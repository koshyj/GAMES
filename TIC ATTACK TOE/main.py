import sys


# TIC TAC TOE CLASS and DEFINITIONS


# BOX Class
class Box:

    def __init__(self):
        # Boxes named with position relative to self
        self.lb = None
        self.rb = None
        self.ub = None
        self.db = None

        # VAL 0: No mark, VAL 1: o, VAL 2: x
        self.value = 0


    
    # GETTERS
    def get_left_box(self):
        return self.lb
    
    def get_right_box(self):
        return self.rb
    
    def get_up_box(self):
        return self.ub

    def get_down_box(self):
        return self.db

    
    def get_value(self):
        return self.value
    


    # MODIFIERS
    def add_left_box(self, box):
        self.lb = box
        box.rb = self
    
    def add_right_box(self, box):
        self.rb = box
        box.lb = self
    
    def add_up_box(self, box):
        self.ub = box
        box.db = self
    
    def add_down_box(self, box):
        self.db = box
        box.ub = self


    def reset(self):
        self.value = 0

    def set_o(self):
        self.value = 1 if (not self.get_value()) else self.get_value()

    def set_x(self):
        self.value = 2 if (not self.get_value()) else self.get_value()



    # CHECKS
    # def check(self):    # Does a row and col check, returning x wins if both x and o have won
    #     return self.check_col() if ( self.check_col() > self.check_row() ) else self.check_row()


    def check_row(self):    # Returns 0 for no consistent row values, 1 for a row of o's, 2 for a row of x's
        if not self.get_value():
            return 0
        else: 
            left_box = self.lb
            while (left_box != None):
                if (left_box.get_value() != self.get_value()):
                    return 0
                left_box = left_box.get_left_box()

            right_box = self.rb
            while (right_box != None):
                if (right_box.get_value() != self.get_value()):
                    return 0
                right_box = right_box.get_right_box()        
        return self.get_value()


    def check_col(self):    # Returns 0 for no consistent col values, 1 for a col of o's, 2 for a col of x's
        if not self.get_value():
            return 0
        else: 
            up_box = self.ub
            while (up_box != None):
                if (up_box.get_value() != self.get_value()):
                    return 0
                up_box = up_box.get_up_box()

            down_box = self.db
            while (down_box != None):
                if (down_box.get_value() != self.get_value()):
                    return 0
                down_box = down_box.get_down_box()        
        return self.get_value()
    

    def check_diagonal(self):   # Returns the same codes as col and row checks, CAN ONLY BE RUN WITH THE MIDDLE BOX
        if not self.get_value():
            return 0
        else:
            # Checking left up to right down diagonal for non wins
            if ( self.get_value() == self.get_left_box().get_up_box().get_value() or self.get_value() == self.get_right_box().get_down_box().get_value() ):
                return self.get_value()
            # Checking left down to right up diagonal for non wins
            if ( self.get_value() == self.get_left_box().get_down_box().get_value() or self.get_value() == self.get_right_box().get_up_box().get_value() ):
                return self.get_value()
            return 0
        


    def print_box(self):
        sys.stdout.write( "[ " + str(self.get_value()) + " ]")


# MAP Class
class Map:

    def __init__(self):
        # The root box is the middle box
        self.root_box = Box()
        self.create_map()
        self.win = 0
        self.check_win()



    # GETTERS
    def get_win(self):
        return self.win



    # GAME FUNCTIONS
    def create_map(self):   # Adds partner boxes to the root box to define a 3 x 3 map grid

        # Root box starts as top middle
        # add left and right boxes to root
        self.root_box.add_left_box(Box())
        self.root_box.add_right_box(Box())

        # add bottom box to root, and left and right boxes to that box. Also links those boxes to boxes above them
        self.root_box.add_down_box(Box())
        self.root_box.get_down_box().add_left_box(Box())
        # Links top left box to middle left box
        self.root_box.get_down_box().get_left_box().add_up_box(self.root_box.get_left_box())
        self.root_box.get_down_box().add_right_box(Box())
        # Links top right box to middle right box
        self.root_box.get_down_box().get_right_box().add_up_box(self.root_box.get_right_box())

        # Repeats previous pattern with the middle box by going down from the middle, left, right and then uplinking the left and right boxes
        middle_box = self.root_box.get_down_box()
        middle_box.add_down_box(Box())
        middle_box.get_down_box().add_left_box(Box())
        # Links top left box to middle left box
        middle_box.get_down_box().get_left_box().add_up_box(middle_box.get_left_box())
        middle_box.get_down_box().add_right_box(Box())
        # Links top right box to middle right box
        middle_box.get_down_box().get_right_box().add_up_box(middle_box.get_right_box())

        # Assigns root box to middle box
        self.root_box = self.root_box.get_down_box()

    
    def check_win(self):    # Uses the middle column to check all rows, the top. Assumes only one win can occur in the game
        
        up_box = self.root_box.get_up_box()
        down_box = self.root_box.get_down_box()
        left_box = self.root_box.get_left_box()
        right_box = self.root_box.get_right_box()

        if ( up_box.check_row() ):
            self.win = up_box.get_value()
        if ( down_box.check_row() ):
            self.win = down_box.get_value()
        if ( left_box.check_col() ):
            self.win = left_box.get_value()
        if ( right_box.check_col() ):
            self.win = right_box.get_value()

        if ( self.root_box.check_col() or self.root_box.check_row() ):
            self.win = self.root_box.get_value()
        if ( self.root_box.check_diagonal() ):
            self.win = self.root_box.get_value()
        
        return self.win


    def print_map(self):
        box = self.root_box.get_up_box().get_left_box()
        while (box != None):
            box.print_box()
            box = box.get_right_box()
        print ""
        box = self.root_box.get_left_box()
        while (box != None):
            box.print_box()
            box = box.get_right_box()
        print ""
        box = self.root_box.get_left_box().get_down_box()
        while (box != None):
            box.print_box()
            box = box.get_right_box()
        print ""


map = Map()

map.root_box.set_o()
map.root_box.get_up_box().set_o()
map.root_box.get_down_box().set_o()

map.print_map()
map.check_win()
print str( map.win )