import importlib.util
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "utils" / "knowledge_base.py"
SPEC = importlib.util.spec_from_file_location("knowledge_base", MODULE_PATH)
knowledge_base = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(knowledge_base)


def test_get_answer_handles_none_input():
    assert knowledge_base.get_answer(None) is None


def test_get_answer_handles_empty_string():
    assert knowledge_base.get_answer("") is None
