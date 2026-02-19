import json
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import config
import i18n as i18n_module

TRANSLATIONS_DIR = ROOT / "translations"
LOCALES = ["en", "es", "de"]
PLACEHOLDER_RE = re.compile(r"\{([^{}]+)\}")


def _load_locale(locale: str):
    file_path = TRANSLATIONS_DIR / f"{locale}.json"
    with file_path.open("r", encoding="utf-8") as f:
        return json.load(f)


def _to_map(entries):
    mapping = {}
    duplicates = set()

    for entry in entries:
        if not isinstance(entry, dict) or len(entry) != 1:
            continue
        key = next(iter(entry.keys()))
        if key in mapping:
            duplicates.add(key)
        mapping[key] = entry[key]

    return mapping, duplicates


class TestTranslations(unittest.TestCase):
    def test_json_has_expected_structure(self):
        for locale in LOCALES:
            entries = _load_locale(locale)
            self.assertIsInstance(entries, list, f"{locale}.json debe contener una lista")
            self.assertGreater(len(entries), 0, f"{locale}.json no debe estar vacio")

            for idx, entry in enumerate(entries):
                self.assertIsInstance(entry, dict, f"{locale}.json[{idx}] debe ser objeto")
                self.assertEqual(len(entry), 1, f"{locale}.json[{idx}] debe tener una sola clave")
                k, v = next(iter(entry.items()))
                self.assertIsInstance(k, str, f"{locale}.json[{idx}] clave debe ser string")
                self.assertIsInstance(v, str, f"{locale}.json[{idx}] valor debe ser string")

    def test_no_duplicate_keys_per_locale(self):
        for locale in LOCALES:
            entries = _load_locale(locale)
            _, duplicates = _to_map(entries)
            self.assertFalse(duplicates, f"{locale}.json tiene claves duplicadas: {sorted(duplicates)}")

    def test_all_locales_have_same_keys(self):
        reference_map, _ = _to_map(_load_locale("en"))
        reference_keys = set(reference_map.keys())

        for locale in ["es", "de"]:
            mapping, _ = _to_map(_load_locale(locale))
            locale_keys = set(mapping.keys())

            missing = sorted(reference_keys - locale_keys)
            extra = sorted(locale_keys - reference_keys)

            self.assertFalse(missing, f"{locale}.json sin claves respecto a en.json: {missing}")
            self.assertFalse(extra, f"{locale}.json con claves extra respecto a en.json: {extra}")

    def test_placeholders_are_consistent_across_locales(self):
        base_map, _ = _to_map(_load_locale("en"))

        for locale in ["es", "de"]:
            locale_map, _ = _to_map(_load_locale(locale))
            shared_keys = set(base_map.keys()) & set(locale_map.keys())

            for key in sorted(shared_keys):
                base_placeholders = set(PLACEHOLDER_RE.findall(base_map[key]))
                locale_placeholders = set(PLACEHOLDER_RE.findall(locale_map[key]))
                self.assertEqual(
                    base_placeholders,
                    locale_placeholders,
                    f"Placeholders inconsistentes para '{key}' entre en y {locale}",
                )


class TestI18nFunction(unittest.TestCase):
    def test_i18n_returns_translated_value(self):
        es_entries = _load_locale("es")
        result = i18n_module.i18n("wrong_password", es_entries)
        self.assertEqual(result, "Password incorrecta")

    def test_i18n_returns_fallback_for_missing_key(self):
        result = i18n_module.i18n("clave_inexistente", [])
        expected = f"clave_inexistente {config.LANG} :: <Not found>"
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
