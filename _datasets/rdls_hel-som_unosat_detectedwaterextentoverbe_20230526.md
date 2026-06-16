---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/water-extent-over-between-19-to-23-may-2023-over-hiraan-midle-shabelle-and-lower-shabelle-
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/water-extent-over-between-19-to-23-may-2023-over-hiraan-midle-shabelle-and-lower-shabelle-
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-over-between-19-to-23-may-2023-over-hiraan-midle-shabelle-and-lower-shabelle-
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-over-between-19-to-23-may-2023-over-hiraan-midle-shabelle-and-lower-shabelle-
dataset_id: rdls_hel-som_unosat_detectedwaterextentoverbe_20230526
description: "UNOSAT code FL20230327SOM, GDACS Id: 1101908 This map illustrates cumulative\
  \ satellite-detected water using VIIRS along the Shabelle River in Somalia between\
  \ 19 to 23 May 2023. Within the analysed area of about 39,000 km\xB2, about 1,400\
  \ km\xB2 of land appear to be flooded. Based on Worldpop population data and the\
  \ maximum flood water coverage, at least 120,000 people are potentially exposed\
  \ or living close to flooded areas. This is a preliminary analysis and has not yet\
  \ been validated in the field. Please send ground feedback to United Nations Satellite\
  \ Centre (UNOSAT).. [Source: This metadata record was automatically extracted from\
  \ the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/water-extent-over-between-19-to-23-may-2023-over-hiraan-midle-shabelle-and-lower-shabelle-]"
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
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-SA-4.0
lineage:
  description: "UNOSAT analysts reviewed and compared VIIRS satellite imagery from\
    \ May 19-23, 2023 to detect cumulative water extent along the Shabelle River in\
    \ Somalia. Detected flood water coverage (1,400 km\xB2) was overlaid with WorldPop\
    \ population data to estimate approximately 120,000 people potentially exposed\
    \ to flooding in the 39,000 km\xB2 study area. This is a preliminary post-event\
    \ empirical assessment not yet validated in the field."
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
    name: WorldPop
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/water-extent-over-between-19-to-23-may-2023-over-hiraan-midle-shabelle-and-lower-shabelle-
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population exposed to fluvial flooding based on satellite-detected
      water extent and population distribution
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
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
  description: Satellite detected water extent over between 19 to 23 May 2023 over
    Hiraan, Midle Shabelle and Lower Shabelle Region, Somalia (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3600/FL20230327SOM_gdb.zip
  format: Geodatabase
  id: resource_4a862f0f
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
  description: Satellite detected water extent over between 19 to 23 May 2023 over
    Hiraan, Midle Shabelle and Lower Shabelle Region, Somalia (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3600/FL20230327SOM_SHP.zip
  format: null
  id: resource_49633372
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
- loss
schema: rdls-10
slug: rdls_hel-som_unosat_detectedwaterextentoverbe_20230526
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
  start: '2023-05-26'
temporal_resolution: null
title: Satellite detected water extent over between 19 to 23 May 2023 over Hiraan,
  Midle Shabelle and Lower Shabelle Region, Somalia
version: null
vulnerability: null
---
