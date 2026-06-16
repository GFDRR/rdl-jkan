---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/water-extents-in-kombo-north-st-marie-district-brikama-region-gambia-as-of-5-august-2022
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extents-in-kombo-north-st-marie-district-brikama-region-gambia-as-of-5-august-2022
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extents-in-kombo-north-st-marie-district-brikama-region-gambia-as-of-5-august-2022
dataset_id: rdls_he-gmb_unosat_detectedwaterextentskombo_20220808
description: 'UNOSAT code: FL20220801GMB This map illustrates satellite-detected surface
  waters in Kombo North/St Marie District, Brikama Region, Gambia as observed from
  a Sentinel-2 image acquired on 5 Aug 2022 at 11:33 local time. Within the analyzed
  area of about 2,340 hectares, about 22 hectares of lands appear to be flooded and
  about 3 km of road appear to be likely affected by the flood waters. This is a preliminary
  analysis and has not yet been validated in the field. Please send ground feedback
  to United Nations Satellite Centre (UNOSAT).. [Source: This metadata record was
  automatically extracted from the Humanitarian Data Exchange (HDX); Original dataset:
  https://data.humdata.org/dataset/water-extents-in-kombo-north-st-marie-district-brikama-region-gambia-as-of-5-august-2022]'
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
    description: Road network segments affected by flood waters
    id: infrastructure
    scheme: null
    title: null
    uri: null
  category: infrastructure
  id: exposure_1
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
      intensity_measure: AA:km2
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: Sentinel-2 satellite imagery acquired on 5 August 2022 was analyzed
    by UNOSAT analysts through visual interpretation and multi-temporal comparison
    to detect surface water extents. The flooded area (22 hectares) and affected road
    length (3 km) were delineated and quantified within the 2,340 hectare study area
    in Kombo North/St Marie District, Gambia.
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
- href: https://data.humdata.org/dataset/water-extents-in-kombo-north-st-marie-district-brikama-region-gambia-as-of-5-august-2022
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
  description: Satellite detected water extents in Kombo North/St Marie District,
    Brikama Region, Gambia as of 5 August 2022 (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/GM/FL20220801GMB/FL20220801GMB_gdb.zip
  format: Geodatabase
  id: resource_df78dd51
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20220801GMB_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents in Kombo North/St Marie District,
    Brikama Region, Gambia as of 5 August 2022 (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/GM/FL20220801GMB/FL20220801GMB_SHP.zip
  format: null
  id: resource_0f1a6d7e
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20220801GMB_SHP.zip
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-gmb_unosat_detectedwaterextentskombo_20220808
spatial:
  bbox: null
  centroid: null
  countries:
  - GMB
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2022-08-08'
temporal_resolution: null
title: Satellite detected water extents in Kombo North/St Marie District, Brikama
  Region, Gambia as of 5 August 2022
version: null
vulnerability: null
---
