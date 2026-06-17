---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sentinel-2 satellite imagery
    url: https://data.humdata.org/dataset/water-extents-in-banjul-kanifing-and-brikama-regions-gambia-as-of-10-august-2022
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop population data
    url: https://data.humdata.org/dataset/water-extents-in-banjul-kanifing-and-brikama-regions-gambia-as-of-10-august-2022
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extents-in-banjul-kanifing-and-brikama-regions-gambia-as-of-10-august-2022
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extents-in-banjul-kanifing-and-brikama-regions-gambia-as-of-10-august-2022
dataset_id: rdls_he-gmb_unosat_detectedwaterextentsbanju_20220811
description: 'UNOSAT code: FL20220801GMB This map illustrates satellite-detected surface
  waters in Satellite detected water in Banjul, Kanifing, and Brikama Regions, Gambia
  as observed from a Sentinel-2 image acquired on 10 Aug 2021 at 18:18 local time.
  Within the analyzed cloud free zones of about 960 km2, about 26 km2 of lands appear
  to be flooded. Based on Worldpop population data and the detected surface waters
  in the analyzed area, the potentially exposed population is mainly located in the
  districts of Kanifing with ~ 7,300 people, Kombo North/St Marie with ~ 7,000 and
  Kombo South with ~ 4,100 people This is a preliminary analysis and has not yet been
  validated in the field. Please send ground feedback to United Nations Satellite
  Centre (UNOSAT).. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/water-extents-in-banjul-kanifing-and-brikama-regions-gambia-as-of-10-august-2022]'
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
    description: Potentially exposed population in Kanifing, Kombo North/St Marie,
      and Kombo South districts derived from WorldPop data
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
      intensity_measure: AA:km2
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: flood
license: CC-BY-SA-4.0
lineage:
  description: "UNOSAT analysts processed Sentinel-2 satellite imagery acquired on\
    \ 10 August 2022 to detect surface water extents through visual interpretation\
    \ and comparison of cloud-free zones. Detected flooded areas (26 km\xB2 within\
    \ 960 km\xB2 analyzed) were intersected with WorldPop population data to estimate\
    \ potentially exposed populations by district."
  sources:
  - id: source_1
    license: null
    name: Sentinel-2 satellite imagery
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: WorldPop population data
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/water-extents-in-banjul-kanifing-and-brikama-regions-gambia-as-of-10-august-2022
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
  description: Satellite detected water extents in Banjul, Kanifing, and Brikama Regions,
    Gambia as of 10 August 2022 (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/GM/FL20220801GMB/FL20220801GMB_gdb.zip
  format: Geodatabase
  id: resource_7db8cf09
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
  description: Satellite detected water extents in Banjul, Kanifing, and Brikama Regions,
    Gambia as of 10 August 2022 (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/GM/FL20220801GMB/FL20220801GMB_SHP.zip
  format: null
  id: resource_7a3cb1dc
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
slug: rdls_he-gmb_unosat_detectedwaterextentsbanju_20220811
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
  start: '2022-08-11'
temporal_resolution: null
title: Satellite detected water extents in Banjul, Kanifing, and Brikama Regions,
  Gambia as of 10 August 2022
version: null
vulnerability: null
---
