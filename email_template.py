import os, email, smtplib

path = os.path.dirname(__file__)
#modify this to change the Template Directory
TEMPLATE_DIR = '/email_templates/'


class EmailTemplate():
    def __init__(self, template_name='', values={}, html=True):
        self.template_name = template_name
        self.values = values
        self.html = html

    def render(self):
        content = open(path + TEMPLATE_DIR + self.template_name).read()

        for k,v in self.values.iteritems():
            content = content.replace('[%s]' % k,v)

        return content
