from typing import List, Union

from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    @staticmethod
    def adding(the_list: List, the_element: Union[Category, Document, Topic]) -> None:
        if the_element not in the_list:
            the_list.append(the_element)

    @staticmethod
    def editing(the_list: List, the_id: int, *to_change) -> None:
        the_element = next((x for x in the_list if x.id == the_id))
        if isinstance(the_element, Category):
            the_element.name = to_change[0]
        elif isinstance(the_element, Topic):
            the_element.topic = to_change[0]
            the_element.storage_folder = to_change[1]
        else:
            the_element.file_name = to_change[0]

    @staticmethod
    def deleting(the_list: List, the_id) -> None:
        the_element = next((x for x in the_list if x.id == the_id), None)
        the_list.remove(the_element)

    def add_category(self, category: Category) -> None:
        self.adding(self.categories, category)

    def add_topic(self, topic: Topic) -> None:
        self.adding(self.topics, topic)

    def add_document(self, document: Document) -> None:
        self.adding(self.documents, document)

    def edit_category(self, category_id: int, new_name: str) -> None:
        self.editing(self.categories, category_id, new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str) -> None:
        self.editing(self.topics, topic_id, new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str) -> None:
        self.editing(self.documents, document_id, new_file_name)

    def delete_category(self, category_id: int) -> None:
        self.deleting(self.categories, category_id)

    def delete_topic(self, topic_id: int) -> None:
        self.deleting(self.topics, topic_id)

    def delete_document(self, document_id: int) -> None:
        self.deleting(self.documents, document_id)

    def get_document(self, document_id) -> "Document":
        the_document = next((x for x in self.documents if x.id == document_id), None)
        return the_document

    def __repr__(self):
        return "\n".join(f'{x}' for x in self.documents)
