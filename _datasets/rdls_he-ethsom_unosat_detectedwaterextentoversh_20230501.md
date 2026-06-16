---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sentinel-2 satellite imagery
    url: https://data.humdata.org/dataset/water-extent-over-shabelle-zone-somali-region-ethiopia-and-beledweyne-district-hiraan-regi
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop population data
    url: https://data.humdata.org/dataset/water-extent-over-shabelle-zone-somali-region-ethiopia-and-beledweyne-district-hiraan-regi
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-over-shabelle-zone-somali-region-ethiopia-and-beledweyne-district-hiraan-regi
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-over-shabelle-zone-somali-region-ethiopia-and-beledweyne-district-hiraan-regi
dataset_id: rdls_he-ethsom_unosat_detectedwaterextentoversh_20230501
description: "UNOSAT code FL20230327SOM This map illustrates satellite-detected surface\
  \ waters in Shabelle Zone, Somali Region of Ethiopia and Beledweyne District, Hiraan\
  \ Region of Somalia as observed from a Sentinel-2 image acquired on 29 April 2023\
  \ at 07:06 UTC. Within the analyzed area of about 5,300 km\xB2, about 180 km\xB2\
  \ of land appear to be flooded. Water extent appears to have increased by about\
  \ 60 km\xB2 since 19 April 2023. Based on Worldpop population data and the detected\
  \ surface waters in the analyzed area, 7,500 people are potentially exposed or living\
  \ close to flooded areas. This is a preliminary analysis and has not yet been validated\
  \ in the field. Please send ground feedback to United Nations Satellite Centre (UNOSAT)..\
  \ [Source: This metadata record was automatically extracted from the Humanitarian\
  \ Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/water-extent-over-shabelle-zone-somali-region-ethiopia-and-beledweyne-district-hiraan-regi]"
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
  description: UNOSAT analysts processed Sentinel-2 satellite imagery acquired on
    29 April 2023 to detect surface water extent through visual interpretation and
    comparison with a prior image from 19 April 2023. Detected water polygons were
    intersected with WorldPop gridded population data to estimate exposure. The resulting
    geodatabase and shapefile products contain water extent geometries with area calculations
    and population exposure estimates.
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
- href: https://data.humdata.org/dataset/water-extent-over-shabelle-zone-somali-region-ethiopia-and-beledweyne-district-hiraan-regi
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
  description: Satellite detected water extent over Shabelle Zone, Somali Region,
    Ethiopia and Beledweyne District, Hiraan Region of Somalia as of 29 April 2023
    (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3569/FL20230327SOM_gdb.zip
  format: Geodatabase
  id: resource_153accf9
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
  description: Satellite detected water extent over Shabelle Zone, Somali Region,
    Ethiopia and Beledweyne District, Hiraan Region of Somalia as of 29 April 2023
    (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3569/FL20230327SOM_SHP.zip
  format: null
  id: resource_05c7e354
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
slug: rdls_he-ethsom_unosat_detectedwaterextentoversh_20230501
spatial:
  bbox: null
  centroid: null
  countries:
  - ETH
  - SOM
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-05-01'
temporal_resolution: null
title: Satellite detected water extent over Shabelle Zone, Somali Region, Ethiopia
  and Beledweyne District, Hiraan Region of Somalia as of 29 April 2023
version: null
vulnerability: null
---
