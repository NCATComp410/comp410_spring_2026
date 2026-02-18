"""PII Scan"""
import re
import logging
import spacy
from presidio_analyzer import (AnalyzerEngine, RecognizerRegistry, RecognizerResult,
                               PatternRecognizer, Pattern,)
from presidio_analyzer.predefined_recognizers import (ItDriverLicenseRecognizer,
                                                      ItVatCodeRecognizer,
                                                      ItFiscalCodeRecognizer,
                                                      ItIdentityCardRecognizer,
                                                      ItPassportRecognizer,
                                                      EsNieRecognizer,
                                                      EsNifRecognizer,
                                                      PlPeselRecognizer,
                                                      FiPersonalIdentityCodeRecognizer,
                                                      AbaRoutingRecognizer,
                                                      AuAbnRecognizer,
                                                      AuAcnRecognizer,
                                                      AuMedicareRecognizer,
                                                      AuTfnRecognizer,
                                                      InAadhaarRecognizer,
                                                      InPanRecognizer,
                                                      InPassportRecognizer,
                                                      InVehicleRegistrationRecognizer,
                                                      InVoterRecognizer,
                                                      InGstinRecognizer,
                                                      UkNinoRecognizer,
                                                      ThTninRecognizer,
                                                      KrRrnRecognizer,
                                                      SgFinRecognizer,
                                                      SgUenRecognizer,
                                                      )

from presidio_anonymizer import AnonymizerEngine
import requests

# make sure en_core_web_lg is loaded correctly
# this can also be achieved with
# python -m spacy download en_core_web_lg
try:
    nlp = spacy.load("en_core_web_lg")
except OSError:
    from spacy.cli import download
    download("en_core_web_lg")
    nlp = spacy.load("en_core_web_lg")

# Configure logging to DEBUG level when needed
# logging.basicConfig(level=logging.DEBUG)
# Configure logging to INFO level when needed
# logging.basicConfig(level=logging.INFO)
# By default only critical logs will be printed
logging.basicConfig(level=logging.CRITICAL)

# Create an analyzer object
registry = RecognizerRegistry()
registry.load_predefined_recognizers()
# Add some language specific recognizers as english instead of default language
registry.add_recognizer(ItDriverLicenseRecognizer(supported_language='en'))
registry.add_recognizer(ItVatCodeRecognizer(supported_language='en'))
registry.add_recognizer(ItFiscalCodeRecognizer(supported_language='en'))
registry.add_recognizer(ItIdentityCardRecognizer(supported_language='en'))
registry.add_recognizer(ItPassportRecognizer(supported_language='en'))
registry.add_recognizer(EsNieRecognizer(supported_language='en'))
registry.add_recognizer(EsNifRecognizer(supported_language='en'))
registry.add_recognizer(PlPeselRecognizer(supported_language='en'))
registry.add_recognizer(FiPersonalIdentityCodeRecognizer(supported_language='en'))
registry.add_recognizer(AbaRoutingRecognizer(supported_language='en'))
registry.add_recognizer(AuAbnRecognizer(supported_language='en'))
registry.add_recognizer(AuAcnRecognizer(supported_language='en'))
registry.add_recognizer(AuMedicareRecognizer(supported_language='en'))
registry.add_recognizer(AuTfnRecognizer(supported_language='en'))
registry.add_recognizer(InAadhaarRecognizer(supported_language='en'))
registry.add_recognizer(InPanRecognizer(supported_language='en'))
registry.add_recognizer(InPassportRecognizer(supported_language='en'))
registry.add_recognizer(InVehicleRegistrationRecognizer(supported_language='en'))
registry.add_recognizer(InVoterRecognizer(supported_language='en'))
registry.add_recognizer(InGstinRecognizer(supported_language='en'))
registry.add_recognizer(UkNinoRecognizer(supported_language='en'))
registry.add_recognizer(ThTninRecognizer(supported_language='en'))
registry.add_recognizer(KrRrnRecognizer(supported_language='en'))
registry.add_recognizer(SgFinRecognizer(supported_language='en'))
registry.add_recognizer(SgUenRecognizer(supported_language='en'))


# Create an analyzer object

crypto_pattern = Pattern(
    "Crypto wallet pattern",
    r"\b(?:0x[a-fA-F0-9]{40}|[13LM][a-km-zA-HJ-NP-Z1-9]{25,34}|ltc1[a-z0-9]{39,59})\b",
    0.6,
)

crypto_recognizer = PatternRecognizer(
    supported_entity="CRYPTO",
    patterns=[crypto_pattern],
    name="crypto_recognizer"
)

registry.add_recognizer(crypto_recognizer)

# log_decision_process=True will log the decision process for debugging
analyzer = AnalyzerEngine(registry=registry, log_decision_process=False)
#change made
from presidio_analyzer import PatternRecognizer, Pattern

_identity_card_pattern = Pattern(
    name="t_identity_card_with_exp",
    regex=(
        r"(?i)\b(?:id|identity\s*card|id\s*card|document)\s*"
        r"(?:#|number|no\.|:)?\s*"
        r"[A-Z0-9]{6,12}\b"
        r"(?:.*?\b(?:exp|expires|expiration|expiry)\b\s*[:\-]?\s*"
        r"(?:0[1-9]|1[0-2])\/(?:\d{2}|\d{4})\b)"
    ),
    score=0.85,
)

t_identity_card_recognizer = PatternRecognizer(
    supported_entity="T_IDENTITY_CARD",
    patterns=[_identity_card_pattern],
    context=["identity", "card", "document", "expires", "expiration", "expiry"],
)

registry.add_recognizer(t_identity_card_recognizer)
# chang made
anonymizer = AnonymizerEngine()


def show_aggie_pride():
    """Show Aggie Pride"""
    return "Aggie Pride - Worldwide"


def anonymize_text(text: str, entity_list: list) -> str:
    """
    Anonymize the text using the entity list
    :param text: the text to be anonymized
    :param entity_list: the list of entities to be anonymized
           https://microsoft.github.io/presidio/supported_entities/
    """
    # Call analyzer to get results
    results = analyze_text(text=text, entity_list=entity_list)

    # Analyzer results are passed to the AnonymizerEngine for anonymization
    anonymized_text = anonymizer.anonymize(text=text, analyzer_results=results)

    return anonymized_text.text


def anonymize_data(data: list) -> None:
    """
    Anonymize the text using the entity list
    :param data: the data to be anonymized
    """
    for i, item in enumerate(data):
        if item:
            if item.startswith('#'):
                print(item)
            else:
                print(f'ID:{i}:Original  : {item}')
                print(f'ID:{i}:Anonymized: {anonymize_text(item, [])}')


def analyze_text(text: str, entity_list: list,
                 show_supported=False) -> list[str] | list[RecognizerResult]:
    """
    Analyze the text using the entity list
    :param text: the text to be analyzed
    :param entity_list: the list of entities to be analyzed
           https://microsoft.github.io/presidio/supported_entities/
    :param show_supported: show the supported entities
    """
    # Show all entities that can be detected for debugging
    if show_supported:
        return analyzer.get_supported_entities()
    # Call analyzer to get results
    results = analyzer.analyze(text=text,
                               entities=entity_list,
                               language='en',
                               return_decision_process=True)  # return decision process details

    return results


def read_data() -> list:
    """
    Reads data from a secure file using a secret key stored in .env
    :return: list of lines from the file
    """
    # Load SECRET from .env file
    with open('.env', encoding='utf-8') as f:
        for line in f.readlines():
            m = re.search(r'SECRET="(\w+)"', line)
            if m:
                secret = m.group(1)
                break
            else:
                raise RuntimeError("SECRET not found in .env file")

    # Construct the URL from the API key
    header = 'https://drive.google.com/uc?export=download&id=1Madj8otKjwwOO353nL_'
    url = requests.get(header + secret, timeout=10)

    # Return the data as a list of lines
    return url.text.split('\n')


if __name__ == '__main__':
    print(show_aggie_pride())
    # anonymize_data(read_data())
