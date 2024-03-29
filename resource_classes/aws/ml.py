from . import _AWS


class _ML(_AWS):
    _type = "ml"
    _icon_dir = "resource_images/aws/ml"


class ApacheMxnetOnAWS(_ML):
    _icon = "apache-mxnet-on-aws.png"


class Comprehend(_ML):
    _icon = "comprehend.png"


class DeepLearningAmis(_ML):
    _icon = "deep-learning-amis.png"


class DeepLearningContainers(_ML):
    _icon = "deep-learning-containers.png"


class Deeplens(_ML):
    _icon = "deeplens.png"


class Deepracer(_ML):
    _icon = "deepracer.png"


class ElasticInference(_ML):
    _icon = "elastic-inference.png"


class Forecast(_ML):
    _icon = "forecast.png"


class Lex(_ML):
    _icon = "lex.png"


class MachineLearning(_ML):
    _icon = "machine-learning.png"


class Personalize(_ML):
    _icon = "personalize.png"


class Polly(_ML):
    _icon = "polly.png"


class Rekognition(_ML):
    _icon = "rekognition.png"


class SagemakerGroundTruth(_ML):
    _icon = "sagemaker-ground-truth.png"


class SagemakerModel(_ML):
    _icon = "sagemaker-model.png"


class SagemakerNotebook(_ML):
    _icon = "sagemaker-notebook.png"


class SagemakerTrainingJob(_ML):
    _icon = "sagemaker-training-job.png"


class Sagemaker(_ML):
    _icon = "sagemaker.png"


class TensorflowOnAWS(_ML):
    _icon = "tensorflow-on-aws.png"


class Textract(_ML):
    _icon = "textract.png"


class Transcribe(_ML):
    _icon = "transcribe.png"


class Translate(_ML):
    _icon = "translate.png"


# Aliases

DLC = DeepLearningContainers


aws_lex_bot = Lex
aws_sagemaker_app = Sagemaker
aws_sagemaker_notebook_instance = SagemakerNotebook
aws_sagemaker_model = SagemakerModel
