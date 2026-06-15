---
attributions:
- entity:
    affiliation: null
    email: null
    name: Bar-Ilan University
    url: https://www.biu.ac.il/en
  id: attr_biu
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: University of California Davis
    url: https://www.ucdavis.edu/
  id: attr_ucd
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: University of Alabama
    url: https://www.ua.edu/
  id: attr_ua
  role: collaborator
catalog: Zenodo
contact_point:
  affiliation: null
  email: null
  name: Rotem Mayo
  url: https://zenodo.org/records/18647054
creator:
  affiliation: null
  email: null
  name: Google Research
  url: https://research.google/
dataset_id: rdls_hzd-google_groundsource
description: An open global dataset of 2.6 million historical flood events extracted
  from automated processing of over 5 million news articles spanning 150+ countries.
  Google Gemini large language models extract structured spatial and temporal data
  from journalistic text. Each record includes a unique identifier, event start and
  end dates, location polygon or buffered point geometry (WGS 84), and area in square
  kilometres. Temporal coverage spans 2000 to 2026, with approximately 64% of records
  from 2020 onwards reflecting digital news availability rather than increased flood
  frequency. Entity-based structure means multiple records may exist for a single
  meteorological event.
details: 'Methodology: news articles where flooding is the primary subject are processed
  through a four-stage pipeline: (1) Google Read Aloud isolates primary article text;
  (2) Cloud Translation API standardises content to English across 80 languages; (3)
  Gemini LLM classifies whether flooding is actual/ongoing/past (not a warning), anchors
  relative time references to publication dates, and identifies granular event locations;
  (4) Google Maps Platform geocodes locations to standardised polygons. Average event
  footprint 142 km2; 82% of events span less than 50 km2. Validation: 85-100% recall
  of severe flood events recorded by GDACS (2020-2026); 82% of all extracted events
  are practically useful for real-world analysis. Known biases: temporal underrepresentation
  of pre-2020 events due to digitisation gaps; geographic density correlates with
  regional news infrastructure coverage; language coverage limited to 80 languages.
  Also available as Google Earth Engine FeatureCollection at projects/sat-io/open-datasets/groundsource_2026.'
exposure: []
hazard:
  event_sets_by_hazard_type:
    flood:
    - analysis_type: empirical
      calculation_method: observed
      event_count: 2600000
      events: []
      frequency_distribution: null
      hazards:
      - classification:
          description: Flood events observed from global news media. Coverage spans
            multiple sub-types (fluvial, pluvial, coastal); process is set to fluvial_flood
            as the dominant type in globally reported major flood events. Dataset
            does not record physical intensity values; wd:m is the conventional flood
            intensity measure placeholder required by schema.
          id: cls_flood_undrr
          scheme: UNDRR-ISC
          title: Flood
          uri: https://www.undrr.org/understanding-disaster-risk/terminology/hips/fl0050
        id: hzd_flood
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: es_flood_empirical
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Flood event records extracted from global news media (2000-2026) using
    a four-stage LLM pipeline. News articles are retrieved from global sources across
    150+ countries and 80 languages, then processed through Google Read Aloud (text
    isolation), Cloud Translation API (English standardisation), Gemini LLM (flood
    classification, temporal reasoning, and spatial extraction), and Google Maps Platform
    (geocoding to standardised polygons). Each record represents a distinct reported
    flood occurrence with a spatial polygon and temporal extent.
  sources:
  - id: src_news
    license: null
    name: Global news articles
    risk_data_type: null
    type: dataset
    url: null
    used_in: hazard
  - id: src_read_aloud
    license: null
    name: Google Read Aloud
    risk_data_type: null
    type: model
    url: null
    used_in: hazard
  - id: src_translation
    license: null
    name: Google Cloud Translation API
    risk_data_type: null
    type: model
    url: https://cloud.google.com/translate
    used_in: hazard
  - id: src_gemini
    license: null
    name: Gemini LLM
    risk_data_type: null
    type: model
    url: https://deepmind.google/technologies/gemini/
    used_in: hazard
  - id: src_maps
    license: null
    name: Google Maps Platform
    risk_data_type: null
    type: model
    url: https://mapsplatform.google.com/
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss:
  losses: []
project:
  name: Groundsource
  url: https://research.google/blog/introducing-groundsource-turning-news-reports-into-data-with-gemini/
publisher:
  affiliation: null
  email: null
  name: Google Research
  url: https://research.google/
purpose: To provide a comprehensive global observational flood event catalogue derived
  from news media, addressing gaps in systematic flood observation particularly in
  data-scarce regions.
referenced_by:
- author_names:
  - Rotem Mayo
  - Oleg Zlydenko
  - Moral Bootbool
  - Shmuel Fronman
  - Oren Gilon
  - Avinatan Hassidim
  - Frederik Kratzert
  - Gila Loike
  - Yossi Matias
  - Yonatan Nakar
  - Grey Nearing
  - Reuven Sayag
  - Amitay Sicherman
  - Ido Zemach
  - Deborah Cohen
  date_published: '2026-03-10'
  doi: 10.31223/X5RR2K
  id: ref_preprint
  name: 'Groundsource: A Dataset of Flood Events from News'
  url: https://doi.org/10.31223/X5RR2K
resources:
- access_url: https://zenodo.org/records/18647054
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Complete global flood event catalogue in Apache Parquet format (667
    MB). Columns: uuid (event identifier), start_date (YYYY-MM-DD), end_date (YYYY-MM-DD),
    area_km2 (event polygon area in square kilometres), geometry (polygon or buffered
    point, WGS 84 EPSG:4326).'
  download_url: https://zenodo.org/records/18647054/files/groundsource_2026.parquet
  format: null
  id: resource_parquet
  media_type: application/vnd.apache.parquet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Groundsource flood events (Parquet)
- access_url: https://gee-community-catalog.org/projects/groundsource/
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Groundsource flood event catalogue available as a Google Earth Engine
    FeatureCollection at projects/sat-io/open-datasets/groundsource_2026. Queryable
    via Earth Engine JavaScript and Python APIs.
  download_url: null
  format: Google Earth Engine FeatureCollection
  id: resource_gee
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Groundsource on Google Earth Engine
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-google_groundsource
spatial:
  bbox:
  - -180.0
  - -90.0
  - 180.0
  - 90.0
  centroid: null
  countries:
  - GLO
  gazetteer_entries: []
  scale: global
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-12-31'
  start: '2000-01-01'
temporal_resolution: null
title: 'Groundsource: A Global Dataset of Flood Events from News'
version: '1'
vulnerability: null
---
