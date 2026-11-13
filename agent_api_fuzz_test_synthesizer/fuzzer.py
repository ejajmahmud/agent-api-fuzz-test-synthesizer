"""Type-directed API fuzz payload synthesizer."""
from typing import Dict, List, Optional, Tuple, Any

class FuzzPayload:
    def __init__(self, field_name: str, value: Any, category: str):
        self.field_name = field_name
        self.value = value
        self.category = category

class APIFuzzSynthesizer:
    """Generates boundary and malformed payloads from simple schema specs."""

    @staticmethod
    def generate_fuzz_values_for_type(field_name: str, field_type: str) -> List[FuzzPayload]:
        t = field_type.lower().strip()
        payloads = []

        if t in ["int", "integer"]:
            payloads.append(FuzzPayload(field_name, 0, "ZERO"))
            payloads.append(FuzzPayload(field_name, -1, "NEGATIVE"))
            payloads.append(FuzzPayload(field_name, 2147483647, "INT_MAX_32"))
            payloads.append(FuzzPayload(field_name, 9223372036854775807, "INT_MAX_64"))
            payloads.append(FuzzPayload(field_name, "NaN", "TYPE_CONFUSION"))

        elif t in ["str", "string"]:
            payloads.append(FuzzPayload(field_name, "", "EMPTY_STRING"))
            payloads.append(FuzzPayload(field_name, chr(0) * 3, "NULL_BYTES"))
            payloads.append(FuzzPayload(field_name, "A" * 5000, "OVERFLOW_LENGTH"))
            payloads.append(FuzzPayload(field_name, "<script>alert(1)</script>", "XSS_PAYLOAD"))
            payloads.append(FuzzPayload(field_name, "' OR 1=1 --", "SQLI_PAYLOAD"))

        elif t in ["bool", "boolean"]:
            payloads.append(FuzzPayload(field_name, True, "TRUE"))
            payloads.append(FuzzPayload(field_name, False, "FALSE"))
            payloads.append(FuzzPayload(field_name, None, "NULL"))

        return payloads
