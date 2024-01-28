class ClothingItem:
    def __init__(self, name, image_path, category):
        self.name = name
        self.image_path = image_path
        self.category = category

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_image_path(self):
        return self.image_path

    def set_image_path(self, image_path):
        self.image_path = image_path

    def get_category(self):
        return self.category

    def set_category(self, category):
        self.category = category

    def get_image(self):
        with open(self.image_path, 'rb') as file:
            return file.read()
