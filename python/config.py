root_dir = ".."
# output directory
datasets_dir = f"{root_dir}/_datasets"
# input directory
country_geojson_dir = f"{root_dir}/country_geojson"
json_dir = f"{datasets_dir}/json"
python_path = f"{root_dir}/python"
vectors_path = f"{python_path}/vectors.json"
# for use when run with --ci flag
remote_target_branch = "rdl-1.0"

# Search configuration constants (matching front-end hybrid search logic)
KEYWORD_SCORE_MIN = 0.75
KEYWORD_SCORE_MAX = 1.0
SCORED_FIELDS = [
    "catalog",
    "category",
    "creator.name",
    "dataset_id",
    "description",
    "details",
    "geo_coverage",
    "license",
    "notes",
    "project",
    "resources",
    "title",
]
SEMANTIC_MAX_RESULTS = 50
SEMANTIC_MIN_SCORE = 0.25

schema_url = "https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json"

dataset_catalogs = {
    "oasishub.co": "OASIS HUB",
    "drmkc.jrc.ec.europa.eu/risk-data-hub#": "JRC DRMKC risk hub",
    "data.humdata.org": "Humanitarian Data Exchange",
    "emdat.be": "EM-DAT (Emergency Events Database)",
    "gdacs.org": "GDACS (Global Disaster Alert and Coordination System)",
    "risk.preventionweb.net": "GAR PreventionWeb",
    "ncei.noaa.gov": "NOAA",
    "cds.climate.copernicus.eu": "Copernicus Climate Data Store",
    "earthdata.nasa.gov": "NASA Earth Data",
    "datacatalog.worldbank.org": "World Bank Data Catalog",
    "geohub.data.undp.org": "UNDP GeoHub",
    "unosat.org": "UNOSAT",
    "fao.org": "FAO Data",
    "data.adb.org": "Asian Development Bank Data Library",
    "dataportal.opendataforafrica.org": "African Development Bank Data Portal",
    "openstreetmap.org": "OpenStreetMap",
    "scihub.copernicus.eu": "Copernicus Open Access Hub",
    "sedac.ciesin.columbia.edu": "NASA SEDAC",
    "zenodo.org": "Zenodo",
    "figshare.com": "figshare",
    "datadryad.org": "Dryad",
    "data.europa.eu": "European Data Portal",
}

dataset_licenses = {
    "CC0-1.0": {
        "url": "https://creativecommons.org/publicdomain/zero/1.0/",
        "title": "Creative Commons CCZero",
    },
    "CC-BY-4.0": {
        "url": "https://creativecommons.org/licenses/by/4.0/",
        "title": "Creative Commons Attribution 4.0",
    },
    "CC-BY-SA-4.0": {
        "url": "https://creativecommons.org/licenses/by-sa/4.0/",
        "title": "Creative Commons Attribution Share-Alike 4.0",
    },
    "CC-BY-NC-SA-4.0": {
        "url": "https://creativecommons.org/licenses/by-nc-sa/4.0/",
        "title": "Creative Commons Attribution-NonCommercial-Share-Alike 4.0",
    },
    "CC-BY-ND 4.0": {
        "url": "https://creativecommons.org/licenses/by-nd/4.0/",
        "title": "Creative Commons Attribution-NoDerivatives 4.0 International",
    },
    "CC-BY-NC-ND 4.0": {
        "url": "https://creativecommons.org/licenses/by-nc-nd/4.0/",
        "title": "Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International",
    },
    "CC-BY-IGO-3.0": {
        "url": "https://creativecommons.org/licenses/by-sa/3.0/igo/",
        "title": "Creative Commons Attribution for Intergovernmental Organisations",
    },
    "GPL": {
        "url": "https://www.gnu.org/licenses/gpl-3.0-standalone.html",
        "title": "GNU General Public License",
    },
    "MIT": {"url": "https://opensource.org/license/MIT", "title": "The MIT License"},
    "PDDL-1.0": {
        "url": "http://opendatacommons.org/licenses/pddl/1.0/",
        "title": "Open Data Commons Public Domain Dedication and License",
    },
    "ODbL-1.0": {
        "url": "https://opendatacommons.org/licenses/odbl/1-0",
        "title": "Open Data Commons Open Database License",
    },
}
