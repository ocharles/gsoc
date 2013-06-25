import uuid
import re

from werkzeug.routing import BaseConverter, ValidationError

UUID_RE = re.compile(
    r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$')

class UUIDConverter(BaseConverter):
    
    def __init__(self, url_map, strict=True):
        super(UUIDConverter, url_map, self).__init__(url_map)
        self.strict = strict
    
    def to_python(self, value):
        if self.strict and not UUID_RE.match(value):
            raise ValidationError()

        try:
            return uuid.UUID(value)
        except ValueError:
            raise ValidationError()

    def to_url(self, value):
        return str(value)

class FlaskUUID(object):

    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.url_map.converters['uuid'] = UUIDConverter
