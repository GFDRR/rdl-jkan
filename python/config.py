root_dir = ".."
# output directory
datasets_dir = f"{root_dir}/_datasets"
# input directory
country_geojson_dir = f"{root_dir}/country_geojson"
json_dir = f"{datasets_dir}/json"
python_path = f"{root_dir}/python"
vectors_path = f"{python_path}/vectors.json"
# for use when run with --ci flag
remote_target_branch = "rdl-0.3"

# Search configuration constants (matching front-end hybrid search logic)
KEYWORD_SCORE_MIN = 0.75
KEYWORD_SCORE_MAX = 1.0
SCORED_FIELDS = ['catalog', 'category', 'creator.name', 'dataset_id', 'description', 'details', 'geo_coverage', 'license', 'notes', 'project', 'resources', 'title']
SEMANTIC_MAX_RESULTS = 50
SEMANTIC_MIN_SCORE = 0.25

schema_url_v2 = "https://docs.riskdatalibrary.org/en/0__2__0/rdls_schema.json"
schema_url_v3 = "https://docs.riskdatalibrary.org/en/0__3__0/rdls_schema.json"

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