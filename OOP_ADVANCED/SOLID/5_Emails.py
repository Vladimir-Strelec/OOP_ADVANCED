from abc import ABCMeta, abstractmethod


class IEmail(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def set_sender(self, sender):
        pass

    @abstractmethod
    def set_receiver(self, receiver):
        pass

    @abstractmethod
    def set_content(self, text):
        pass


class MyContent:
    def __init__(self, text):
        self.text = self.format_text(text)

    @staticmethod
    def format_text(text):
        return ' '.join(['<myML>', text, '</myML>'])


class MyHtml(MyContent):
    def __init__(self, text):
        super().__init__(text)

    @staticmethod
    def format_text(text):
        return ' '.join(['<myHTML>', text, '</myHTML>'])


class Email(IEmail):

    def __init__(self, protocol):
        self.protocol = protocol
        self.content_type = None
        self.__sender = None
        self.__receiver = None
        self.__content = None

    @property
    def protocol(self):
        return self.__protocol

    @protocol.setter
    def protocol(self, value):
        if value == 'IM':
            value = "I'm"
        self.__protocol = value

    def set_sender(self, sender):
        self.__sender = " ".join([self.protocol, sender])
        return self.__sender

    def set_receiver(self, receiver):
        self.__receiver = " ".join([self.protocol, receiver])
        return self.__receiver

    def set_content(self, text):
        self.__content = text.text
        return self.__content

    def __repr__(self):
        return f"Sender: {self.__sender}\nReceiver: {self.__receiver}\nContent:\n{self.__content}"




# email = Email('IM', 'MyML')
# email.set_sender('qmal')
# email.set_receiver('james')
# email.set_content('Hello, there!')
# print(email)

email = Email("IM")
email.set_sender("qmal")
email.set_receiver("james")


content = MyContent("Hello, there!")
html = MyHtml("Hello, there!")
email.set_content(content)
print(email)
email.set_content(html)
print(email)
