import uuid

class Save_image(object):
    def save_image(instance, file_name):
        image_path = file_name.split(".")[-1]
        return f"{uuid.uuid4()}.{image_path}"
