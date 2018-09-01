import logging
from .DB import Database, English_Db, ASL_Structure_DB
from NLP import nlp_nlp
from pyramid.view import (
    view_config
)

log = logging.getLogger(__name__)



class Back_end_views(object):
    def __init__(self, request):
        self.request = request
        self.view_name = 'Back_end_views'

    def working(self,sentence):
        val = nlp_nlp.thesis(sentence)['value']
        gloss = nlp_nlp.thesis(sentence)['gloss']
        step = nlp_nlp.thesis(sentence)['step']
        return {'value' :val, 'gloss':gloss, 'step':step}

    @view_config(route_name='home1', renderer='templates/original.html')
    def home(self):
        if 'transcript_value' in self.request.params:
            sentence = self.request.params['transcript_value']
        else:
            sentence = "What is your name"
        sen = Back_end_views.working(self, sentence)['value']
        length = 1
        if sen is not None:
            if len(sen.split(" ")) is not None:
                length = len(sen.split(" "))
        elif sen is None:
            sen = "None"
        gloss = Back_end_views.working(self, sentence)['gloss']
        step = Back_end_views.working(self, sentence)['step']
        print(sentence)
        sentence = sentence.split(" ")
        print(sentence)
        for i,y in enumerate(sentence):
            print(y[:-2])
            if y[:-2] == "'s":
                sentence[i] = sentence[i] + " is"
        sentence = " ".join(sentence)
        print(sentence)
        return {'title': "Testing", 'sentence':sen, 'gloss':gloss, 'length':length, 'original_sentence':sentence
                , 'step':step}

    @view_config(request_method='POST', route_name='create', renderer='json')
    def create(self):
        word = self.request.params['word']
        POS = self.request.params['pos']
        url = self.request.params['url']
        body = Database.create_table(word,POS, url)
        return {'Response': 'Table created','data':body}

    @view_config(request_method='GET', route_name='get_all_words', renderer='json')
    def get_all(self):
        body2 = Database.getAll()
        return {'Status': 200, 'data':body2 }

    @view_config(request_method='GET', route_name='get_all_videos', renderer='json')
    def get_all_videos(self):
        body2 = English_Db.getAll()
        return {'Status': 200, 'data': body2}

    @view_config(request_method='GET', route_name='get_all_universaltags', renderer='json')
    def get_all_universaltags(self):
        body2 = ASL_Structure_DB.getAll()
        return {'Status': 200, 'data': body2}

    @view_config(request_method='GET', route_name='get_one_where', renderer='json')
    def get_one_where(self,word,pos):
        body2 = Database.get_one_where(word,pos)
        if body2 is None:
            body2 = "MO.jpg"
        else:
            body2 = body2
        return {'Status': 200, 'data': body2}

    @view_config(request_method='PUT', route_name='update_where', renderer='json')
    def update_where(self):
        where_to_update = self.request.params['where_to_update']
        what_to_update = self.request.params['what_to_update']
        body2 = Database.update_one_where(where_to_update, what_to_update)
        return {'Hello': body2}

    @view_config(request_method='DELETE', route_name='delete_where', renderer='json')
    def delete_where(self):
        table_name = self.request.matchdict['table_name']
        location = self.request.matchdict['location']
        uid = self.request.matchdict['id']
        body2 = Database.delete_one_where(table_name, location, uid)
        return {'Status': 200, 'data': body2, 'message':'deleted successfully'}
