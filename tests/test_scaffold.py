"""Скаффолд-проверки: репозиторий собран и конфиг эксперимента не заполнен молча.

Настоящие тесты появляются вместе с кодом — см. LEARNING.md. Первым из них должен быть
тест контроля ошибки под нулём: без него любая скорость обнаружения ничего не значит.
"""

from pathlib import Path

import yaml

CONFIG = Path(__file__).resolve().parents[1] / "configs" / "monitoring_probe.yaml"

REQUIRED_SECTIONS = {
    "table",
    "alternative",
    "horizon",
    "methods",
    "streams",
    "uncertainty",
}


def test_probe_config_has_all_sections():
    config = yaml.safe_load(CONFIG.read_text())
    assert REQUIRED_SECTIONS <= set(config)


def test_seeds_are_separated():
    """Сид потока и сид метода разделены: иначе смена метода меняет и сам поток."""
    streams = yaml.safe_load(CONFIG.read_text())["streams"]
    assert {"seed_stream", "seed_method"} <= set(streams)


def test_naive_peeking_is_present_as_calibration():
    """Наивная ветка обязана быть в сетке: на ней проверяется, что харнесс ловит инфляцию α."""
    methods = yaml.safe_load(CONFIG.read_text())["methods"]
    assert any(m["name"] == "naive_peeking" for m in methods)
