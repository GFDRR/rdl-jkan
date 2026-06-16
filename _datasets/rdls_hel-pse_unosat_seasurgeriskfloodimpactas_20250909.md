---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/sea-surge-risk-flood-impact-assessment-in-the-coastal-area-of-gaza-city-occupied-palestini
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/sea-surge-risk-flood-impact-assessment-in-the-coastal-area-of-gaza-city-occupied-palestini
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/sea-surge-risk-flood-impact-assessment-in-the-coastal-area-of-gaza-city-occupied-palestini
dataset_id: rdls_hel-pse_unosat_seasurgeriskfloodimpactas_20250909
description: 'UNOSAT code: FL20250828PSE This map illustrates the current shoreline
  and the highest observed watermark in the Gaza Strip (Occupied Palestinian Territory),
  derived from Sentinel-2 and Pleiades imagery acquired on 28 July 2025 and 29 August
  2025, respectively. The analysis focuses on the area west of Al Rashid Road, where
  a very high density of tents has been observed within a small geographic area that
  is particularly prone to flooding in the event of high tides or storm surges. UNITAR-
  UNOSAT has identified 350 internally displaced persons (IDPs) in high-risk areas
  (within 20 meters of the highest observed watermark) and 1,252 IDPs in risk areas
  (within 50 meters of the highest observed watermark). This is a preliminary analysis
  and has not yet been validated in the field. Please send ground feedback to the
  United Nations Satellite Centre (UNOSAT).. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/sea-surge-risk-flood-impact-assessment-in-the-coastal-area-of-gaza-city-occupied-palestini]'
details: This is a preliminary assessment and has not yet been validated in the field.
  It is important to consider the characteristics of the source imagery used in the
  analyses when interpreting results. For damage assessments it should be noted that
  only significant damage to the structural integrity of the buildings analyzed can
  be seen in imagery, while minor damage such as cracks or holes may not be visible
  at all. For flood extractions using radar data it is important to note that urban
  areas and highly vegetated areas may mask the flood signature and result in underestimation
  of flood waters. Users with specific questions or concerns should contact unosat@unitar.org
  to seek clarification.
exposure:
- asset_type:
    description: Internally displaced persons in tent settlements within high-risk
      coastal flood zones
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
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: wd:m
      process: coastal_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: Satellite imagery from Sentinel-2 and Pleiades was acquired and analyzed
    to map the current shoreline and highest observed watermark in Gaza coastal areas.
    Multi-temporal image comparison identified areas prone to storm surge and high
    tide flooding. Field assessment and spatial analysis identified 350 internally
    displaced persons in tent settlements within high-risk coastal flood zones west
    of Al Rashid Road.
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/sea-surge-risk-flood-impact-assessment-in-the-coastal-area-of-gaza-city-occupied-palestini
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons identified in high-risk coastal flood
      areas
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: coastal_flood
      trigger: null
      type: flood
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
        modelling: simulated
        type: direct
      loss_approach: analytical
      loss_frequency_type: probabilistic
      loss_type: ground_up
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
  description: Palestine - Sea Surge risk & flood impact assessment in the Coastal
    Area of Gaza city (Occupied Palestinian Territory) as of 29 August 2025 (Zipped
    geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/4195/FL20250828PSE_gdb.zip
  format: Geodatabase
  id: resource_db2f2f18
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20250828PSE_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Palestine - Sea Surge risk & flood impact assessment in the Coastal
    Area of Gaza city (Occupied Palestinian Territory) as of 29 August 2025 (Zipped
    shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/4195/FL20250828PSE_SHP.zip
  format: null
  id: resource_ed7ba28d
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20250828PSE_SHP.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Palestine - Sea Surge risk & flood impact assessment in the Coastal
    Area of Gaza city (Occupied Palestinian Territory) as of 29 August 2025 (Excel
    file)
  download_url: https://unosat.org/static/unosat_filesystem/4195/UNOSAT_FL20250828PSE_Total_IDPs_Governorates.xlsx
  format: null
  id: resource_e7ece56a
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_FL20250828PSE_Total_IDPs_Governorates.xlsx
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-pse_unosat_seasurgeriskfloodimpactas_20250909
spatial:
  bbox: null
  centroid: null
  countries:
  - PSE
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2025-09-09'
temporal_resolution: null
title: Palestine - Sea Surge risk & flood impact assessment in the Coastal Area of
  Gaza city (Occupied Palestinian Territory) as of 29 August 2025
version: null
vulnerability: null
---
