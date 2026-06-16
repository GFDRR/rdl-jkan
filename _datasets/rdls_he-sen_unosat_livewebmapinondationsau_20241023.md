---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/unosat-live-web-map-inondations-au-senegal
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/unosat-live-web-map-inondations-au-senegal
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/unosat-live-web-map-inondations-au-senegal
dataset_id: rdls_he-sen_unosat_livewebmapinondationsau_20241023
description: 'UNOSAT code: FL20241022SEN This application provides geospatial information
  regarding the floods in Senegal Important note: The boundaries and names shown,
  and the designations used on this map do not imply official endorsement or acceptance
  by the United Nations. The United Nations Satellite Centre. UNOSAT is not responsible
  for the misuse or misrepresentation of the map.. [Source: This metadata record was
  automatically extracted from the Humanitarian Data Exchange (HDX); Original dataset:
  https://data.humdata.org/dataset/unosat-live-web-map-inondations-au-senegal]'
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
    description: Population exposed to observed flood extent in Senegal
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
  - analysis_type: empirical
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts reviewed and compared multi-temporal satellite imagery
    to identify and delineate flood water extent, classifying water bodies by confidence
    level and validation status. Population exposure was calculated by intersecting
    observed flood polygons with gridded population data. The resulting geodatabase
    and shapefiles contain water classification features with area measurements and
    metadata for the October 2024 Senegal flooding event.
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/unosat-live-web-map-inondations-au-senegal
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
  description: "Senegal - UNOSAT Live Web Map - Inondations au S\xE9n\xE9gal (Zipped\
    \ geodatabase)"
  download_url: https://unosat.org/static/unosat_filesystem/4007/FL20241022SEN_gdb.zip
  format: Geodatabase
  id: resource_0774614b
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20241022SEN_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Senegal - UNOSAT Live Web Map - Inondations au S\xE9n\xE9gal (Zipped\
    \ shapefile)"
  download_url: https://unosat.org/static/unosat_filesystem/4007/FL20241022SEN_SHP.zip
  format: null
  id: resource_018cffcf
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20241022SEN_SHP.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Senegal - UNOSAT Live Web Map - Inondations au S\xE9n\xE9gal (Excel\
    \ file)"
  download_url: https://unosat.org/static/unosat_filesystem/4007/UNOSAT_Population_Exposure_FL20241022SEN_17Oct_21Oct2024_Senegal.xlsx
  format: null
  id: resource_eaf4db00
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_Population_Exposure_FL20241022SEN_17Oct_21Oct2024_Senegal.xlsx
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-sen_unosat_livewebmapinondationsau_20241023
spatial:
  bbox: null
  centroid: null
  countries:
  - SEN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2024-10-23'
temporal_resolution: null
title: "Senegal - UNOSAT Live Web Map - Inondations au S\xE9n\xE9gal"
version: null
vulnerability: null
---
