---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sentinel-2 satellite imagery
    url: https://data.humdata.org/dataset/wildfires-in-tabarka-delegation-jendouba-governorate-and-el-krib-delegation-siliana-govern
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/wildfires-in-tabarka-delegation-jendouba-governorate-and-el-krib-delegation-siliana-govern
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/wildfires-in-tabarka-delegation-jendouba-governorate-and-el-krib-delegation-siliana-govern
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/wildfires-in-tabarka-delegation-jendouba-governorate-and-el-krib-delegation-siliana-govern
dataset_id: rdls_he-tun_unosat_wildfirestabarkadelegatio_20230728
description: "UNOSAT code FR20230725TUN, GDACS Id: 1015980 This map illustrates satellite-detected\
  \ burned areas in Tabarka delegation, Jendouba Governorate and El Krib delegation,\
  \ Siliana Governorate, Tunisia based on a Sentinel-2 image aquired on 27 July 2023\
  \ at 10:20 UTC. Within the analysed area of about 2,800 km\xB2, about 29 km\xB2\
  \ of lands appear to be potentially burned. Based on Worldpop population data and\
  \ the burned area extent about 7,700 people are potentially exposed or living close\
  \ to burned areas. This is a preliminary analysis and has not yet been validated\
  \ in the field. Please send ground feedback to the United Nations Satellite Centre\
  \ (UNOSAT).. [Source: This metadata record was automatically extracted from the\
  \ Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/wildfires-in-tabarka-delegation-jendouba-governorate-and-el-krib-delegation-siliana-govern]"
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
    description: Population potentially exposed or living close to burned areas based
      on WorldPop data
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
      intensity_measure: FWI:-
      process: wildfire
      trigger: null
      type: wildfire
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts performed change detection analysis on Sentinel-2 satellite
    imagery acquired on 27 July 2023 to identify burned areas in the study region.
    Burned area polygons were delineated and intersected with WorldPop gridded population
    data to estimate approximately 7,700 people potentially exposed to or living near
    the burned areas. This is a preliminary satellite-based assessment not yet validated
    in the field.
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
    name: WorldPop
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/wildfires-in-tabarka-delegation-jendouba-governorate-and-el-krib-delegation-siliana-govern
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
  description: Tunisia - Wildfires in Tabarka delegation, Jendouba Governorate and
    El Krib delegation, Siliana Governorate as of 27 July 2023 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3647/FR20230725TUN.gdb.zip
  format: Geodatabase
  id: resource_700d767f
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FR20230725TUN.gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Tunisia - Wildfires in Tabarka delegation, Jendouba Governorate and
    El Krib delegation, Siliana Governorate as of 27 July 2023 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3647/FR20230725TUN_SHP.zip
  format: null
  id: resource_b421e991
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FR20230725TUN_SHP.zip
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-tun_unosat_wildfirestabarkadelegatio_20230728
spatial:
  bbox: null
  centroid: null
  countries:
  - TUN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-07-28'
temporal_resolution: null
title: Tunisia - Wildfires in Tabarka delegation, Jendouba Governorate and El Krib
  delegation, Siliana Governorate as of 27 July 2023
version: null
vulnerability: null
---
