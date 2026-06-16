---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sentinel-2
    url: https://data.humdata.org/dataset/water-extent-over-hiraan-lower-shabelle-and-middle-shabelle-regions-somalia-as-of-29-april
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/water-extent-over-hiraan-lower-shabelle-and-middle-shabelle-regions-somalia-as-of-29-april
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-over-hiraan-lower-shabelle-and-middle-shabelle-regions-somalia-as-of-29-april
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-over-hiraan-lower-shabelle-and-middle-shabelle-regions-somalia-as-of-29-april
dataset_id: rdls_he-som_unosat_detectedwaterextentoverhi_20230501
description: "UNOSAT code FL20230327SOM, GDACS Id: 1101908 This map illustrates satellite\
  \ detected surface waters Hiraan, Lower Shabelle, and Middle Shabelle Regions Somalia\
  \ as observed from Sentinel-2 image acquired on 29 April 2023 at 07:06 UTC. Within\
  \ the analyzed area about 12,000 km\xB2, about 600 km\xB2 of land appear to be flooded.\
  \ Water extent appears to have increased by about 480km\xB2 since 19 April 2023.\
  \ Based on Worldpop population data and the detected surface waters in the analyzed\
  \ area 59,000 people are potentially exposed or living close flooded areas. This\
  \ is a preliminary analysis and has not yet been validated in the field. Please\
  \ send ground feedback to United Nations Satellite Centre (UNOSAT).. [Source: This\
  \ metadata record was automatically extracted from the Humanitarian Data Exchange\
  \ (HDX); Original dataset: https://data.humdata.org/dataset/water-extent-over-hiraan-lower-shabelle-and-middle-shabelle-regions-somalia-as-of-29-april]"
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
    description: Population potentially exposed or living close to flooded areas based
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
      intensity_measure: AA:km2
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-SA-4.0
lineage:
  description: "Satellite imagery from Sentinel-2 acquired on 29 April 2023 was analyzed\
    \ by UNOSAT to detect surface water extent through comparison with prior imagery\
    \ from 19 April 2023. Detected water polygons were intersected with WorldPop population\
    \ data to estimate exposure. The dataset provides observed flood extent (600 km\xB2\
    \ flooded out of 12,000 km\xB2 analyzed area) and derived population exposure\
    \ estimates (59,000 people)."
  sources:
  - id: source_1
    license: null
    name: Sentinel-2
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
- href: https://data.humdata.org/dataset/water-extent-over-hiraan-lower-shabelle-and-middle-shabelle-regions-somalia-as-of-29-april
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
  description: Satellite detected water extent over Hiraan, Lower Shabelle, and Middle
    Shabelle Regions, Somalia as of 29 April 2023 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3571/FL20230327SOM_gdb.zip
  format: Geodatabase
  id: resource_f207ef82
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20230327SOM_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extent over Hiraan, Lower Shabelle, and Middle
    Shabelle Regions, Somalia as of 29 April 2023 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3571/FL20230327SOM_SHP.zip
  format: null
  id: resource_fdc68f93
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20230327SOM_SHP.zip
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-som_unosat_detectedwaterextentoverhi_20230501
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
  start: '2023-05-01'
temporal_resolution: null
title: Satellite detected water extent over Hiraan, Lower Shabelle, and Middle Shabelle
  Regions, Somalia as of 29 April 2023
version: null
vulnerability: null
---
