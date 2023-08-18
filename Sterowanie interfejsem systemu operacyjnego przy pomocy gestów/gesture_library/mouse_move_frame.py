

class MouseMoveFrame:

    def __init__(self):
        self.width = 0
        self.height = 0

    def calculate_mouse_move_frame(self, image):
        width = len(image[0])
        height = len(image)
        if width == self.width and height == self.height:
            return
        if height < 360 or width < 360:
            self.left_bound = 0
            self.right_bound = width - 1
            self.upper_bound = 0
            self.bottom_bound = height - 1
            self.frame_width = width
            self.frame_width_float = float(width)
            self.frame_height = height
            self.frame_height_float = float(height)
        else:
            if width >= height:
                distance_from_edge = int(height / 3.15)
            else:
                distance_from_edge = int(width / 3.15)
            self.left_bound = distance_from_edge
            self.right_bound = width - distance_from_edge - 1
            self.upper_bound = distance_from_edge
            self.bottom_bound = height - distance_from_edge - 1
            self.frame_width = width - 2 * distance_from_edge
            self.frame_width_float = float(self.frame_width)
            self.frame_height = height - 2 * distance_from_edge
            self.frame_height_float = float(self.frame_height)
        self.width = width
        self.height = height
    
    def check_if_in_frame(self, x, y):
        if x >= self.left_bound and x <= self.right_bound and y >= self.upper_bound \
            and y <= self.bottom_bound:
            return True
        return False

    def get_left_bound(self):
        return self.left_bound

    def get_upper_bound(self):
        return self.upper_bound

    def get_frame_width_float(self):
        return self.frame_width_float

    def get_frame_height_float(self):
        return self.frame_height_float