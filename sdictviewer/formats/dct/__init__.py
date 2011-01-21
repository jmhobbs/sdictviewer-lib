from __future__ import with_statement
import sdictviewer
from . import sdict

def can_open(file_name):
    with __builtins__['open'](file_name, "rb") as file:
        sig = file.read(4)
        return sig == 'sdct'

def open(file_name):
    return sdict.SDictionary(file_name)

def create_article_formatter(text_buffer_factory, internal_link_callback, external_link_callback):
    return sdictviewer.articleformat.ArticleFormat(text_buffer_factory, internal_link_callback, external_link_callback)
