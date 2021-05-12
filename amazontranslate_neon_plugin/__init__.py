from ovos_plugin_manager.templates.language import LanguageDetector,\
    LanguageTranslator
import boto3


class AmazonTranslator(LanguageTranslator):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.keys = self.config["keys"]["amazon"]
        self.client = boto3.Session(
            aws_access_key_id=self.keys["key_id"],
            aws_secret_access_key=self.keys["secret_key"],
            region_name=self.keys["region"]).client('translate')

    def translate(self, text, target=None, source="auto"):
        target = target or self.internal_language

        response = self.client.translate_text(
            Text=text,
            SourceLanguageCode="auto",
            TargetLanguageCode=target.split("-")[0]
        )
        return response["TranslatedText"]


class AmazonDetector(LanguageDetector):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.keys = self.config["keys"]["amazon"]
        self.client = boto3.Session(
            aws_access_key_id=self.keys["key_id"],
            aws_secret_access_key=self.keys["secret_key"],
            region_name=self.keys["region"]).client('comprehend')

    def detect(self, text):
        response = self.client.detect_dominant_language(
            Text=text
        )
        return response['Languages'][0]['LanguageCode']

    def detect_probs(self, text):
        response = self.client.detect_dominant_language(
            Text=text
        )
        langs = {}
        for lang in response["Languages"]:
            langs[lang["LanguageCode"]] = lang["Score"]
        return langs
