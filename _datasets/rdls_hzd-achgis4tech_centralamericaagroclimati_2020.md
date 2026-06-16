---
attributions:
- entity:
    affiliation: null
    email: null
    name: MODIS
    url: https://data.humdata.org/dataset/central-america-agroclimatics-hazards-data-by-ach-gis4tech
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: CHIRPS
    url: https://data.humdata.org/dataset/central-america-agroclimatics-hazards-data-by-ach-gis4tech
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: "Acci\xF3n contra el hambre - GIS4tech"
  url: https://data.humdata.org/dataset/central-america-agroclimatics-hazards-data-by-ach-gis4tech
creator:
  affiliation: null
  email: null
  name: "Acci\xF3n contra el hambre - GIS4tech"
  url: https://data.humdata.org/dataset/central-america-agroclimatics-hazards-data-by-ach-gis4tech
dataset_id: rdls_hzd-achgis4tech_centralamericaagroclimati_2020
description: 'A summary table is established at the municipal level with the list
  of agroclimatic hazards calculated from the agroclimatic indicators shown in the
  Vulnerability panel. For each column, the threat category in which the municipality
  would be found is defined (No risk, Mild threat, Moderate threat, Severe threat),
  and the final column represents the general summary of global threats, obtained
  using the 20% rule. The calculation made within each category is established through
  a matrix of crossed conditions. For more information contact GIS4Tech: info@gis4tech.com.
  You can also visit the PREDISAN platform https://predisan.gis4tech.com/ca4 for detailed,
  accurate information.. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/central-america-agroclimatics-hazards-data-by-ach-gis4tech]'
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
license: CC-BY-4.0
lineage:
  description: 'Agroclimatic hazard indicators were derived from satellite-based vegetation
    indices (MODIS: NDVI, EVI, ARVI, SIPI) and precipitation data (CHIRPS) aggregated
    at the municipal level as median values over specified periods. Hazard classifications
    were generated using a matrix of crossed conditions to assign threat categories
    (No risk, Mild, Moderate, Severe) for each municipality, with a final composite
    hazard score calculated using the 20% rule.'
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
- href: https://data.humdata.org/dataset/central-america-agroclimatics-hazards-data-by-ach-gis4tech
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
  description: Central America - Agroclimatics Hazards (Agroclimatic hazard data for
    Central America.)
  download_url: https://data.humdata.org/dataset/90a82caa-7694-48ae-99b0-79c170613876/resource/2bce7329-121a-46c4-9aab-e7853472aacb/download/agroclimatic_hazards.csv
  format: null
  id: resource_2bce7329
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Central America Agroclimatics Hazards
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-achgis4tech_centralamericaagroclimati_2020
spatial:
  bbox: null
  centroid: null
  countries:
  - SLV
  - GTM
  - HND
  - NIC
  - CRI
  - PAN
  - BLZ
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2025-12-31'
  start: '2020-01-01'
temporal_resolution: null
title: Central America - Agroclimatics Hazards
version: null
vulnerability: null
---
