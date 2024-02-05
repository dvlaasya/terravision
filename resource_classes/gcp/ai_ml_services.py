from . import _GCP


class _AI_ML_Services(_GCP):
    _type = "ai_ml_services"
    _icon_dir = "resource_images/gcp/ai_ml_services"

class Vertexai(_AI_ML_Services):
    _icon = "vertexai.png"

class Dialogflow(_AI_ML_Services):
    _icon="dialogflow.png"

class Dialogflow_cx(_AI_ML_Services):
    _icon="dialogflow_cx.png"

class Document_AI(_AI_ML_Services):
    _icon="document_ai.png"


google_dialogflow_agent=Dialogflow
google_dialogflow_cx_agent=Dialogflow_cx
google_document_ai_processor=Document_AI
google_vertex_ai_endpoint=Vertexai



