---
attributions:
- entity:
    affiliation: null
    email: null
    name: National Digital Strategy Unit at the Office of the President of Mexico
    url: https://data.humdata.org/dataset/laderas
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: National Digital Strategy Unit at the Office of the President of Mexico (inactive)
  url: https://data.humdata.org/dataset/laderas
creator:
  affiliation: null
  email: null
  name: National Digital Strategy Unit at the Office of the President of Mexico (inactive)
  url: https://data.humdata.org/dataset/laderas
dataset_id: rdls_hzd-mex_ndsmex_laderas_20151024
description: "\xC1reas susceptibles a deslizamiento de laderas El mapa nacional de\
  \ susceptibilidad a deslizamientos de laderas contempla una clasificaci\xF3n por\
  \ pixel de cinco posible valores de acuerdo a la tabla siguiente: Valores de pixel\
  \ Clasificaci\xF3n 1- Muy bajo 2- Bajo 3- Medio 4-Alto 5-Muy Alto. [Source: This\
  \ metadata record was automatically extracted from the Humanitarian Data Exchange\
  \ (HDX); Original dataset: https://data.humdata.org/dataset/laderas]"
details: null
exposure: []
hazard:
  event_sets:
  - analysis_type: deterministic
    calculation_method: inferred
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: LSI:-
      process: landslide_general
      trigger: null
      type: landslide
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: landslide
license: CC-BY-4.0
lineage:
  description: The dataset represents a national-scale landslide susceptibility assessment
    derived from topographic and observational data. Pixel-based classification methodology
    assigns each location one of five susceptibility levels (very low to very high)
    based on terrain characteristics and slope stability indicators. The output is
    a raster map suitable for hazard zoning and risk assessment applications.
  sources:
  - id: source_1
    license: null
    name: National Digital Strategy Unit at the Office of the President of Mexico
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/laderas
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: Direct Observational Data/Anecdotal Data
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Mexico - Laderas (Laderas de la Nayarit, Colina y Jalisco)
  download_url: https://data.humdata.org/dataset/14b85598-2aab-4f4b-8702-bf549284e9fd/resource/e502ad21-42bb-4c2e-8b76-bc76d8730eae/download/laderas.zip
  format: null
  id: resource_e502ad21
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: laderas.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-mex_ndsmex_laderas_20151024
spatial:
  bbox: null
  centroid: null
  countries:
  - MEX
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2015-10-24'
temporal_resolution: null
title: Mexico - Laderas
version: null
vulnerability: null
---
