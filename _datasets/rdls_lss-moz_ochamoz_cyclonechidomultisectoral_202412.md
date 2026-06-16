---
attributions:
- entity:
    affiliation: null
    email: null
    name: Humanitarian partners
    url: https://data.humdata.org/dataset/moz_dataanalysis_mira_chido
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Mozambique
  url: https://data.humdata.org/dataset/moz_dataanalysis_mira_chido
creator:
  affiliation: null
  email: null
  name: OCHA Mozambique
  url: https://data.humdata.org/dataset/moz_dataanalysis_mira_chido
dataset_id: rdls_lss-moz_ochamoz_cyclonechidomultisectoral_202412
description: 'Cyclone Chido Multip-Sectoral Initial Rapid Assessment(MIRA) analysis
  dataset of Cabo Delgado and Nampula, Mozambique. On December 15, 2024, Tropical
  Cyclone Chido made landfall in Mozambique, bringing torrential rainfall of up to
  250 mm in 24 hours and winds reaching speeds of 120 km/h. The provinces of Cabo
  Delgado and Nampula have been identified as the hardest hit, experiencing significant
  rainfall and strong winds, with Niassa, Tete, and northern Manica also affected
  to a lesser extent. As of December 20, the National Institute for Disaster Risk
  Management and Reduction (INGD) reported that 329,510 people had been affected by
  the cyclone, with numbers expected to rise as ongoing assessments provide more data.
  To assist INGD in estimating the extent and severity of needs, the humanitarian
  community in Cabo Delgado and Nampula is actively supporting the implementation
  of a Multi-Sectoral Initial Rapid Assessment (MIRA) in both provinces.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/moz_dataanalysis_mira_chido]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: Multi-Sectoral Initial Rapid Assessment (MIRA) data collected via sample
    survey methodology by humanitarian partners in Mozambique following Tropical Cyclone
    Chido landfall on December 15, 2024. The dataset aggregates needs assessment and
    impact information across affected sectors in Cabo Delgado and Nampula provinces,
    with gender and age disaggregation, to support humanitarian response planning.
  sources:
  - id: source_1
    license: null
    name: Humanitarian partners
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/moz_dataanalysis_mira_chido
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct impacts to buildings from tropical cyclone winds and associated
      rainfall
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Population affected by Tropical Cyclone Chido in Cabo Delgado and
      Nampula provinces
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: Sample Survey
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mozambique: Cyclone Chido Multi-Sectoral Initial Rapid Assessment
    (Excel)'
  download_url: https://data.humdata.org/dataset/bd2fe1f9-4d14-4d23-b46e-28d82d7f01f7/resource/390a153e-9d9a-44c5-97bb-480c4eec3ad0/download/moz_dataanalysis_mira_chido_v3_16012024.xlsx
  format: null
  id: resource_390a153e
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MOZ_DataAnalysis_MIRA_Chido_V3_16012024.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-moz_ochamoz_cyclonechidomultisectoral_202412
spatial:
  bbox: null
  centroid: null
  countries:
  - MOZ
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2024-12-28'
  start: '2024-12-18'
temporal_resolution: null
title: 'Mozambique: Cyclone Chido Multi-Sectoral Initial Rapid Assessment'
version: null
vulnerability: null
---
