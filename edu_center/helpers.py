import uuid

class Save_image(object):
    def save_image_book(instance, file_name):
        image_path = file_name.split(".")[-1]
        return f"book/{uuid.uuid4()}.{image_path}"

    def save_image_author(instance, file_name):
        image_path = file_name.split(".")[-1]
        return f"author/{uuid.uuid4()}.{image_path}"