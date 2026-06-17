---
attributions:
- entity:
    affiliation: null
    email: null
    name: Global Volcano Model (GVM)
    url: https://data.humdata.org/dataset/volcano-population-exposure-index-gvm
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: The International Association of Volcanology and Chemistry of the Earth's
      Interior (IAVCEI)
    url: https://data.humdata.org/dataset/volcano-population-exposure-index-gvm
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Office for Disaster Risk Reduction (UNDRR)
  url: https://data.humdata.org/dataset/volcano-population-exposure-index-gvm
creator:
  affiliation: null
  email: null
  name: United Nations Office for Disaster Risk Reduction (UNDRR)
  url: https://data.humdata.org/dataset/volcano-population-exposure-index-gvm
dataset_id: rdls_he-undrr_volcanopopulationexposure_20150101
description: 'A comprehensive set of information on global volcanic hazard, historical
  events, population exposure, vulnerability, and impact has been provided to GAR15
  by Global Volcano Model (GVM) and The International Association of Volcanology and
  Chemistry of the Earth''s Interior (IAVCEI). This work is the first of its kind
  in global coverage and level of contribution from a wide network of experts and
  institutions around the world.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/volcano-population-exposure-index-gvm]'
details: This dataset was generated using other global datasets; it should not be
  used for local applications (such as land use planning). The main purpose of GAR
  2015 datasets is to broadly identify high risk areas at global level and for identification
  of areas where more detailed data should be collected. Some areas may be underestimated
  or overestimated. Given this analysis was conducted using global datasets, the resolution
  of which is not sufficient for in-situ planning, it should not be used for critical
  (like life saving) decisions. UNISDR and collaborators should in no case be liable
  for misuse or misinterpretation of the presented results. The designations employed
  and the presentation of material on the maps do not imply the expression of any
  opinion whatsoever on the part of UNISDR or the Secretariat of the United Nations
  concerning the legal status of any country, territory, city or area or of its authorities,
  or concerning the delimitation of its frontiers or boundaries. The designations
  employed and the presentation of material on the maps do not imply the expression
  of any opinion whatsoever on the part of UNISDR or the Secretariat of the United
  Nations concerning the legal status of any country, territory, city or area or of
  its authorities, or concerning the delimitation of its frontiers or boundaries.
  This analysis was conducted using global datasets, the resolution of which is not
  relevant for in-situ planning and should not be used for life and death decisions.
  UNISDR and collaborators should in no case be liable for misuse of the presented
  results.
exposure:
- asset_type:
    description: Population exposure to volcanic hazards in regions and countries
      with active volcanoes
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_1
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard:
  event_sets:
  - analysis_type: probabilistic
    calculation_method: simulated
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: h_vaf:mm
      process: ashfall
      trigger: null
      type: volcanic
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: volcanic
license: CC-BY-4.0
lineage:
  description: Global volcanic hazard, exposure, and vulnerability data compiled by
    GVM and IAVCEI experts from a worldwide network of institutions. The dataset integrates
    comprehensive technical information on volcanic hazards, historical events, and
    population exposure to produce the first global-coverage volcanic risk assessment
    for GAR15.
  sources:
  - id: source_1
    license: null
    name: Global Volcano Model (GVM)
    risk_data_type:
    - hazard
    type: model
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: The International Association of Volcanology and Chemistry of the Earth's
      Interior (IAVCEI)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/volcano-population-exposure-index-gvm
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Volcano - Population Exposure Index(GVM) (Zipped shapefiles of volcano
    PEI (98 kb).)
  download_url: https://data.humdata.org/dataset/a60ac839-920d-435a-bf7d-25855602699d/resource/9a7872e5-9617-4c1a-a70b-589e47ac72f0/download/volcano.zip
  format: null
  id: resource_9a7872e5
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: volcano.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Volcano - Population Exposure Index(GVM) (Geojson of volcano PEI (573
    kb).)
  download_url: https://data.humdata.org/dataset/a60ac839-920d-435a-bf7d-25855602699d/resource/7234d067-2d74-449a-9c61-22ae6d98d928/download/volcano.json
  format: null
  id: resource_7234d067
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: volcano.json
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Volcano - Population Exposure Index(GVM) (Csv files of volcano population
    exposure index (209 kb).)
  download_url: https://data.humdata.org/dataset/a60ac839-920d-435a-bf7d-25855602699d/resource/e3b1ecf0-ec47-49f7-9011-6bbb7403ef6d/download/volcano.csv
  format: null
  id: resource_e3b1ecf0
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: volcano.csv
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-undrr_volcanopopulationexposure_20150101
spatial:
  bbox: null
  centroid: null
  countries:
  - GLO
  gazetteer_entries: []
  scale: global
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2015-01-01'
temporal_resolution: null
title: Volcano - Population Exposure Index(GVM)
version: null
vulnerability: null
---
