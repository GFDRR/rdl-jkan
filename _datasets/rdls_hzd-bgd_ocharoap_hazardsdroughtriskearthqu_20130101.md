---
attributions:
- entity:
    affiliation: null
    email: null
    name: Bangladesh Agricultural Research Council (BARC)
    url: https://data.humdata.org/dataset/bangladesh-hazards
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Regional Office for Asia and the Pacific (ROAP)
  url: https://data.humdata.org/dataset/bangladesh-hazards
creator:
  affiliation: null
  email: null
  name: OCHA Regional Office for Asia and the Pacific (ROAP)
  url: https://data.humdata.org/dataset/bangladesh-hazards
dataset_id: rdls_hzd-bgd_ocharoap_hazardsdroughtriskearthqu_20130101
description: 'This spatial dataset provides Hazard data of Bangladesh. Drought risk,
  Earthquake risk, Flood risk and River erosion risk are included as separated datasets
  with different attributes. The source of the data is Bangladesh Agricultural Research
  Council (BARC). Dataset records are updated by WFP, Map Action and OCHA.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/bangladesh-hazards]'
details: Date of the dataset is unclear.
exposure: []
hazard:
  event_sets:
  - analysis_type: empirical
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: es_flood_hzd
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: es_flood
    occurrence_range: null
    seasonality: null
  - analysis_type: deterministic
    calculation_method: inferred
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: es_earthquake_hzd
      intensity_measure: PGA:g
      process: ground_motion
      trigger: null
      type: earthquake
    id: es_earthquake
    occurrence_range: null
    seasonality: null
  - analysis_type: empirical
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: es_drought_hzd
      intensity_measure: NDVI:-
      process: agricultural_drought
      trigger: null
      type: drought
    id: es_drought
    occurrence_range: null
    seasonality: null
license: CC-BY-4.0
lineage:
  description: Spatial hazard datasets were compiled by Bangladesh Agricultural Research
    Council (BARC) and subsequently updated and maintained by WFP, Map Action, and
    OCHA. The datasets classify Bangladesh into hazard zones for four distinct hazard
    types (drought, earthquake, flood, river erosion) based on historical occurrence
    patterns and geographic/climatic characteristics, with results stored as polygon
    shapefiles at thana (sub-district) and zone administrative levels.
  sources:
  - id: source_1
    license: null
    name: Bangladesh Agricultural Research Council (BARC)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/bangladesh-hazards
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
  description: Bangladesh - Hazards (Drought risk, Earthquake risk, Flood risk and
    River erosion risk) (Drought risk by BARC - Drought class 1 to 10)
  download_url: https://data.humdata.org/dataset/7362ef2d-7282-459f-bc1b-0347076fcc12/resource/8f974cee-89d9-4818-a05a-f0263f939923/download/bgd_nhr_drought_barc.zip
  format: null
  id: resource_8f974cee
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bgd_nhr_drought_barc.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bangladesh - Hazards (Drought risk, Earthquake risk, Flood risk and
    River erosion risk) (Earthquake risk by BARC - Zone I, II, III)
  download_url: https://data.humdata.org/dataset/7362ef2d-7282-459f-bc1b-0347076fcc12/resource/994c0647-dc44-400f-b969-4f41dc3df812/download/bgd_nhr_earthquake_barc.zip
  format: null
  id: resource_994c0647
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bgd_nhr_earthquake_barc.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Flood risk by BARC- Flood cat 0 - Not flood proned, 1 - Severe River
    Flooding, 8 - Moderate Tidal Surge
  download_url: https://data.humdata.org/dataset/7362ef2d-7282-459f-bc1b-0347076fcc12/resource/ca979980-e533-43f8-83c9-2a6b5ac570c6/download/bgd_nhr_floods_barc.zip
  format: null
  id: resource_ca979980
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bgd_nhr_floods_barc.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bangladesh - Hazards (Drought risk, Earthquake risk, Flood risk and
    River erosion risk) (River erosion risk by BARC)
  download_url: https://data.humdata.org/dataset/7362ef2d-7282-459f-bc1b-0347076fcc12/resource/b9845724-c2d2-4fd5-9513-98b1f0cc0d25/download/bgd_nhr_rivererosion_barc.zip
  format: null
  id: resource_b9845724
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bgd_nhr_rivererosion_barc.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-bgd_ocharoap_hazardsdroughtriskearthqu_20130101
spatial:
  bbox: null
  centroid: null
  countries:
  - BGD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2013-01-01'
temporal_resolution: null
title: Bangladesh - Hazards (Drought risk, Earthquake risk, Flood risk and River erosion
  risk)
version: null
vulnerability: null
---
