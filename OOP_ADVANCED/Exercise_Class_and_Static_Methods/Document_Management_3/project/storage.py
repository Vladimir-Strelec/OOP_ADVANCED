from project.category import Category
from project.document import Document
from project.topic import Topic





class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        if self.__chek_object(self.categories, category.id):
            return
        self.categories.append(category)

    def add_topic(self, topic: Topic):
        if self.__chek_object(self.topics, topic.id):
            return
        self.topics.append(topic)

    def add_document(self, document: Document):
        if self.__chek_object(self.documents, document.id):
            return
        self.documents.append(document)

    def edit_category(self, category_id: int, new_name:str):
        category = self.__chek_object(self.categories, category_id)
        if category:
            category.edit(new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic = self.__chek_object(self.topics, topic_id)
        if topic:
            topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str):
        document = self.__chek_object(self.documents, document_id)
        if document:
            document.edit(new_file_name)

    def delete_category(self, category_id):
        category = self.__chek_object(self.categories, category_id)
        if category:
            self.categories.remove(category)

    def delete_topic(self, topic_id):
        topic = self.__chek_object(self.topics, topic_id)
        if topic:
            self.categories.remove(topic)

    def delete_document(self, document_id):
        document = self.__chek_object(self.documents, document_id)
        if document:
            self.documents.remove(document)

    def get_document(self, document_id):
        current_object = self.__chek_object(self.documents, document_id)
        return current_object

    def __repr__(self):
        return '\n'.join([str(d) for d in self.documents])

    def __chek_object(self, obj, i):
        for obj_id in obj:
            if obj_id.id == i:
                return obj_id
        return
