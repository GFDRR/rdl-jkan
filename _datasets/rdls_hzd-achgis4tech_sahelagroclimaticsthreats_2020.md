---
attributions:
- entity:
    affiliation: null
    email: null
    name: MODIS
    url: https://data.humdata.org/dataset/sahel-agroclimatics-threats-data
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: CHIRPS
    url: https://data.humdata.org/dataset/sahel-agroclimatics-threats-data
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: "Acci\xF3n contra el hambre - GIS4tech"
  url: https://data.humdata.org/dataset/sahel-agroclimatics-threats-data
creator:
  affiliation: null
  email: null
  name: "Acci\xF3n contra el hambre - GIS4tech"
  url: https://data.humdata.org/dataset/sahel-agroclimatics-threats-data
dataset_id: rdls_hzd-achgis4tech_sahelagroclimaticsthreats_2020
description: "A summary table is established at the municipal level with the list\
  \ of agroclimatic hazards calculated from the agroclimatic indicators shown in the\
  \ Vulnerability panel. For each column, the threat category in which the municipality\
  \ would be found is defined (No risk, Mild threat, Moderate threat, Severe threat),\
  \ and the final column represents the general summary of global threats, obtained\
  \ using the 20% rule. The calculation made within each category is established through\
  \ a matrix of crossed conditions. This information belongs to the Food and Nutrition\
  \ Security Monitoring and Prediction System in the Sahel (PREDISAN) Project, funded\
  \ by the Agencia Andaluza de Cooperaci\xF3n Internacional para el Desarrollo (AACID)\
  \ and the University of Granada (UGR). The PREDISAN AI-SAHEL Project focuses on\
  \ the Monitoring and Prediction System for Humanitarian Vulnerability of Pastoral\
  \ and Agro-pastoral Populations in the Western Sahel, based on GIS Analysis and\
  \ Artificial Intelligence. For more information, contact GIS4Tech at info@gis4tech.com\
  \ or visit the PREDISAN platform at https://predisan.gis4tech.com/sahel.. [Source:\
  \ This metadata record was automatically extracted from the Humanitarian Data Exchange\
  \ (HDX); Original dataset: https://data.humdata.org/dataset/sahel-agroclimatics-threats-data]"
details: null
exposure: []
hazard:
  event_sets:
  - analysis_type: empirical
    calculation_method: inferred
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: SPI:-
      process: agricultural_drought
      trigger: null
      type: drought
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Agroclimatic threat data derived from MODIS vegetation indices and
    CHIRPS precipitation data collected at pixel level and aggregated to municipal
    medians. Satellite-derived indicators (NDVI, EVI, ARVI, SIPI, SPI at multiple
    timescales) are processed through a crossed-condition matrix to classify municipalities
    into threat categories (No risk, Mild, Moderate, Severe), with a final global
    threat summary computed using the 20% rule.
  sources:
  - id: source_1
    license: null
    name: MODIS
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: CHIRPS
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/sahel-agroclimatics-threats-data
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
  description: Sahel Agroclimatics Threats Data (Agroclimatic threats data for Senegal
    and Mauritania.)
  download_url: https://data.humdata.org/dataset/9fe80552-9d7f-4d40-baa2-6b269ed95a24/resource/362f0dbc-5933-4e4c-95db-c382e159b2fd/download/sahel-agroclimatics-threats-by-ach-gis4tech.csv
  format: null
  id: resource_362f0dbc
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Sahel-agroclimatics-threats-by-ACH-GIS4Tech.csv
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-achgis4tech_sahelagroclimaticsthreats_2020
spatial:
  bbox: null
  centroid: null
  countries:
  - MLI
  - BFA
  - NER
  - TCD
  - SEN
  - MRT
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-01-01'
  start: '2020-01-01'
temporal_resolution: null
title: Sahel Agroclimatics Threats Data
version: null
vulnerability: null
---
