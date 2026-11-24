import json
import unittest

import check_datasets
import mappers
import relations
import structured_data


def make_dataset(**overrides):
    return {
        "id": "rdls_hzd-test",
        "title": "Test dataset",
        "description": "A dataset",
        "risk_data_type": ["hazard"],
        "publisher": {"name": "Publisher"},
        "creator": {"name": "Creator"},
        "contact_point": {"name": "Contact", "email": "contact@example.org"},
        "license": "CC-BY-4.0",
        "links": [],
        "spatial": {"scale": "national", "countries": ["KEN"]},
        "resources": [
            {
                "id": "r1",
                "title": "File",
                "description": "A file",
                "download_url": "https://example.org/a b.csv",
                "media_type": "text/csv",
            }
        ],
        **overrides,
    }


def frontmatter(**overrides):
    return mappers.make_dataset_frontmatter(make_dataset(**overrides))


class MapperTest(unittest.TestCase):
    def test_socio_economic_without_functions(self):
        index = {
            "id": "se_1",
            "indicator_name": "Index",
            "indicator_code": "index",
            "description": "An index",
            "reference_year": 2015,
        }
        result = mappers.make_vulnerability({"socio_economic": [index]})
        self.assertEqual(result["socio_economic"][0]["indicator_name"], "Index")
        self.assertEqual(result["functions"]["fragility"], [])

    def test_catalog_from_download_url(self):
        url = "https://datacatalogfiles.worldbank.org/ddh-published/1/a.zip"
        catalog = mappers.make_catalog({"resources": [{"download_url": url}]})
        self.assertEqual(catalog["slug"], "world-bank-data-catalog")
        self.assertEqual(catalog["url"], "datacatalog.worldbank.org")


    def test_bbox_must_be_in_degrees(self):
        projected = [3778287.28, -515424.18, 4663287.28, 549575.82]
        self.assertIsNone(mappers.make_spatial({"bbox": projected})["bbox"])
        for bbox in ([-180.0, -90.0, 180.0, 90.0], [175, -20, 190, -10]):
            self.assertEqual(mappers.make_spatial({"bbox": bbox})["bbox"], bbox)


class StructuredDataTest(unittest.TestCase):
    def test_schema_org(self):
        fm = frontmatter(
            temporal={"start": "2000", "end": "2010"},
            spatial={"scale": "national", "countries": ["KEN"], "bbox": [34, -5, 42, 5]},
        )
        result = structured_data.make_schema_org(fm)
        self.assertEqual(result["@type"], "Dataset")
        self.assertEqual(result["temporalCoverage"], "2000/2010")
        self.assertEqual(result["spatialCoverage"][0]["name"], "Kenya")
        self.assertEqual(result["spatialCoverage"][1]["geo"]["box"], "-5 34 5 42")
        self.assertEqual(
            result["distribution"][0]["contentUrl"], "https://example.org/a%20b.csv"
        )
        self.assertNotIn("contact@example.org", json.dumps(result))

    def test_long_description_is_cut(self):
        result = structured_data.make_schema_org(frontmatter(description="x" * 6000))
        self.assertEqual(len(result["description"]), 5000)

    def test_dcat(self):
        catalog = structured_data.make_dcat_catalog([frontmatter()])
        dataset = catalog["dcat:dataset"][0]
        self.assertEqual(dataset["dct:identifier"], "rdls_hzd-test")
        self.assertEqual(
            dataset["dcat:distribution"][0]["dcat:accessURL"],
            {"@id": "https://example.org/a%20b.csv"},
        )

    def test_only_http_urls_become_references(self):
        self.assertIsNone(structured_data.clean_url("javascript:alert(1)"))
        self.assertIsNone(structured_data.clean_url("not a url"))
        self.assertEqual(structured_data.clean_url("www.brgm.fr"), "https://www.brgm.fr")


class RelationsTest(unittest.TestCase):
    def test_source_matched_by_title(self):
        source = frontmatter(id="a", title="Power Plants", resources=[])
        derived = frontmatter(
            id="b",
            resources=[],
            lineage={"sources": [{"id": "s", "name": "power plants"}]},
        )
        self.assertEqual(
            relations.make_relations([source, derived]),
            [("b", "a", "source", 0), ("a", "b", "derived", 0)],
        )

    def test_home_pages_are_not_matched(self):
        links = [{"rel": "source", "href": "https://example.org/"}]
        one = frontmatter(id="a", links=links, resources=[])
        two = frontmatter(
            id="b",
            resources=[],
            lineage={"sources": [{"id": "s", "url": "https://example.org"}]},
        )
        self.assertEqual(relations.make_relations([one, two]), [])


class CheckTest(unittest.TestCase):
    def errors(self, check, *args):
        report = check_datasets.Report()
        check(*args, report)
        return [message for _, message in report.errors]

    def load(self, raw):
        report = check_datasets.Report()
        return check_datasets.load_dataset("a.json", raw, report), report.errors

    def test_load(self):
        dataset, errors = self.load(b'{"datasets": [{"id": "a"}]}')
        self.assertEqual((dataset, errors), ({"id": "a"}, []))
        for raw in (
            b"{",
            b"\xff",
            b'\xef\xbb\xbf{"datasets": [{}]}',
            b'{"datasets": []}',
            b'{"datasets": [{}, {}]}',
            b'{"datasets": [{"id": "a", "id": "b"}]}',
            b"[]",
        ):
            dataset, errors = self.load(raw)
            self.assertIsNone(dataset, raw)
            self.assertEqual(len(errors), 1, raw)

    def test_text(self):
        check = check_datasets.check_text
        self.assertEqual(self.errors(check, "a", {"t": "Réunion, São Tomé, Ã"}), [])
        for text in ("a b", "a​b", "�", "SÃ£o"):
            self.assertEqual(len(self.errors(check, "a", {"t": text})), 1, text)

    def test_id(self):
        check = check_datasets.check_id
        self.assertEqual(self.errors(check, "a-b.json", {"id": "a-b"}, {}), [])
        self.assertTrue(self.errors(check, "x.json", {"id": "a"}, {}))
        self.assertTrue(self.errors(check, "a b.json", {"id": "a b"}, {}))
        self.assertTrue(self.errors(check, "A.json", {"id": "A"}, {"a": "a.json"}))


if __name__ == "__main__":
    unittest.main()
