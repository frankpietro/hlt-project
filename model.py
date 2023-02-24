# define a class for the model with fields "model" and "folder_path"
class Model:
    def __init__(self, model, folder_path):
        self.model = model
        self.folder_path = folder_path


    # define set and get functions for folder path
    def set_folder_path(self, folder_path):
        self.folder_path = folder_path


    def get_folder_path(self):
        return self.folder_path
