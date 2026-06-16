---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/preliminary-satellite-derived-flood-assessment-bardere-city-baardheere-district-gedo-regio
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/preliminary-satellite-derived-flood-assessment-bardere-city-baardheere-district-gedo-regio
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/preliminary-satellite-derived-flood-assessment-bardere-city-baardheere-district-gedo-regio
dataset_id: rdls_he-som_unosat_preliminaryderivedfloodas_20231113
description: 'UNOSAT code FL20231105SOM Status: Increased water extent along the Jubba
  River Further action(s): continue monitoring Summary of findings: - Increase of
  water extent along the Jubba River observed as of 12 November 2023; - Affected structures
  and agricultural areas. We also observe inundated roads in Bardere City, in the
  Gedo Region as of 12 November 2023;. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/preliminary-satellite-derived-flood-assessment-bardere-city-baardheere-district-gedo-regio]'
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
    description: Affected structures in Bardere City identified through satellite
      imagery
    id: buildings
    scheme: null
    title: null
    uri: null
  category: buildings
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
- asset_type:
    description: Agricultural areas inundated by fluvial flooding along the Jubba
      River
    id: agriculture
    scheme: null
    title: null
    uri: null
  category: agriculture
  id: exposure_2
  metrics:
  - dimension: product
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
- asset_type:
    description: Inundated roads in Bardere City affected by flood waters
    id: infrastructure
    scheme: null
    title: null
    uri: null
  category: infrastructure
  id: exposure_3
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: length
      unit: null
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
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts reviewed and compared satellite imagery from 12 November
    2023 to identify changes in water extent along the Jubba River and delineate affected
    structures, agricultural areas, and inundated roads in Bardere City. The resulting
    geodatabase and shapefile contain mapped flood extent polygons with area measurements
    in square meters and hectares.
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
- href: https://data.humdata.org/dataset/preliminary-satellite-derived-flood-assessment-bardere-city-baardheere-district-gedo-regio
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
  description: Preliminary satellite-derived flood assessment -Bardere City, Baardheere
    District, Gedo Region, Somalia (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3733/FL20231105SOM_gdb.zip
  format: Geodatabase
  id: resource_2a4b7b35
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20231105SOM_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Preliminary satellite-derived flood assessment -Bardere City, Baardheere
    District, Gedo Region, Somalia (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3733/FL20231105SOM_SHP.zip
  format: null
  id: resource_11eb977b
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20231105SOM_SHP.zip
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-som_unosat_preliminaryderivedfloodas_20231113
spatial:
  bbox: null
  centroid: null
  countries:
  - SOM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-11-13'
temporal_resolution: null
title: Preliminary satellite-derived flood assessment -Bardere City, Baardheere District,
  Gedo Region, Somalia
version: null
vulnerability: null
---
