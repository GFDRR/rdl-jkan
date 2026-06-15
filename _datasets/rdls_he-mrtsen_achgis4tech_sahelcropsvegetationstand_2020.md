---
attributions:
- entity:
    affiliation: null
    email: null
    name: MODIS
    url: https://data.humdata.org/dataset/senegal-and-mauritania-crops-vegetation-and-standardized-precipitation-index
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: CHIRPS
    url: https://data.humdata.org/dataset/senegal-and-mauritania-crops-vegetation-and-standardized-precipitation-index
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: "Acci\xF3n contra el hambre - GIS4tech"
  url: https://data.humdata.org/dataset/senegal-and-mauritania-crops-vegetation-and-standardized-precipitation-index
creator:
  affiliation: null
  email: null
  name: "Acci\xF3n contra el hambre - GIS4tech"
  url: https://data.humdata.org/dataset/senegal-and-mauritania-crops-vegetation-and-standardized-precipitation-index
dataset_id: rdls_he-mrtsen_achgis4tech_sahelcropsvegetationstand_2020
description: "Dataset containing information related to precipitation indices useful\
  \ for analyzing and comparing variations in precipitation over time and across different\
  \ geographical regions, alongside indices used in the analysis of vegetation and\
  \ crops to monitor their activity and detect their presence in the territory. Key\
  \ variables include the Atmospherically Resistant Vegetation Index (ARVI), Normalized\
  \ Difference Vegetation Index (NDVI), Enhanced Vegetation Index (EVI), and Structure\
  \ Insensitive Pigment Index (SIPI) for monitoring vegetation. For rainfall information,\
  \ the Standardized Precipitation Index (SPI1, SPI3, SPI6, SPI9, and SPI12) is used,\
  \ where SPI1 to SPI3 are indicators for immediate impacts and SPI6 to SPI12 measure\
  \ medium-term impacts. Each index is based on data that can be collected through\
  \ remote sensing, such as satellite imagery, and is designed to measure different\
  \ characteristics of vegetation and crops. The data are categorized by country,\
  \ department, and municipality and by year and month, referring to the monthly average.\
  \ This information belongs to the Food and Nutrition Security Monitoring and Prediction\
  \ System in the Sahel (PREDISAN) Project, funded by the Agencia Andaluza de Cooperaci\xF3\
  n Internacional para el Desarrollo (AACID) and the University of Granada (UGR).\
  \ The PREDISAN AI-SAHEL Project focuses on the Monitoring and Prediction System\
  \ for Humanitarian Vulnerability of Pastoral and Agro-pastoral Populations in the\
  \ Western Sahel, based on GIS Analysis and Artificial Intelligence. For more information,\
  \ contact GIS4Tech at info@gis4tech.com or visit the PREDISAN platform at https://predisan.gis4tech.com/sahel..\
  \ [Source: This metadata record was automatically extracted from the Humanitarian\
  \ Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/senegal-and-mauritania-crops-vegetation-and-standardized-precipitation-index]"
details: null
exposure:
- asset_type:
    description: Vegetation and crop activity monitoring through NDVI, EVI, ARVI,
      and SIPI indices derived from MODIS satellite data
    id: agriculture
    scheme: null
    title: null
    uri: null
  category: agriculture
  id: exposure_1
  metrics:
  - dimension: product
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
hazard:
  event_sets_by_hazard_type:
    drought:
    - analysis_type: empirical
      calculation_method: observed
      event_count: 0
      events: []
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_1
        intensity_measure: SPI:-
        process: meteorological_drought
        trigger: null
        type: drought
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: MODIS satellite data and CHIRPS precipitation records were processed
    to derive vegetation indices (NDVI, EVI, ARVI, SIPI) and Standardized Precipitation
    Index (SPI) at 1, 3, 6, 9, and 12-month timescales. Data were aggregated to municipality
    level by calculating median values across each administrative unit in Senegal
    and Mauritania, enabling temporal and spatial monitoring of drought conditions
    and crop/vegetation activity.
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
- href: https://data.humdata.org/dataset/senegal-and-mauritania-crops-vegetation-and-standardized-precipitation-index
  rel: source
loss:
  losses: []
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
  description: Senegal and Mauritania Monthly Crops Vegetation and Precipitation Index
    since 2020 by ACH-GIS4Tech.csv
  download_url: https://data.humdata.org/dataset/96564b62-dede-44a5-9a50-84c14f652c18/resource/254e4601-d19d-46bd-989a-2ea0e5a77e55/download/senegal-and-mauritania-crops-vegetation-and-standardized-precipitation-index.csv
  format: null
  id: resource_254e4601
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Senegal-and-Mauritania-Crops-Vegetation-and-Standardized-Precipitation-Index.csv
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-mrtsen_achgis4tech_sahelcropsvegetationstand_2020
spatial:
  bbox: null
  centroid: null
  countries:
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
title: Sahel Crops Vegetation and Standardized Precipitation Index
version: null
vulnerability: null
---
