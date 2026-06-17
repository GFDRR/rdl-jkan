---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sentinel-2 satellite imagery
    url: https://data.humdata.org/dataset/water-extent-over-shabelle-zone-somali-region-ethiopia-and-beledweyne-and-northern-bulo-bu
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop population data
    url: https://data.humdata.org/dataset/water-extent-over-shabelle-zone-somali-region-ethiopia-and-beledweyne-and-northern-bulo-bu
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-over-shabelle-zone-somali-region-ethiopia-and-beledweyne-and-northern-bulo-bu
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-over-shabelle-zone-somali-region-ethiopia-and-beledweyne-and-northern-bulo-bu
dataset_id: rdls_hel-ethsom_unosat_detectedwaterextentoversh_20230517
description: "UNOSAT code FL20230327SOM, GDACS Id: 1101908 This map illustrates satellite-detected\
  \ surface waters in Shabelle Zone, Somali Region of Ethiopia and Beledweyne and\
  \ Northern Bulo Burto District, Hiraan Region of Somalia as observed from a Sentinel-2\
  \ image acquired on 14 May 2023 at 07:28 UTC. Within the analyzed area of about\
  \ 8,000 km\xB2, about 500 km\xB2 of land appear to be flooded. Water extent appears\
  \ to have increased by about 300 km\xB2 since 29 April 2023. Based on Worldpop population\
  \ data and the detected surface waters in the analyzed area, about 29,700 people\
  \ are potentially exposed or living close to flooded areas. This is a preliminary\
  \ analysis and has not yet been validated in the field. Please send ground feedback\
  \ to United Nations Satellite Centre (UNOSAT).. [Source: This metadata record was\
  \ automatically extracted from the Humanitarian Data Exchange (HDX); Original dataset:\
  \ https://data.humdata.org/dataset/water-extent-over-shabelle-zone-somali-region-ethiopia-and-beledweyne-and-northern-bulo-bu]"
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
    description: Residential population potentially exposed to detected flood waters
      based on WorldPop data
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
  description: "UNOSAT analysts manually reviewed and compared Sentinel-2 satellite\
    \ imagery acquired on 14 May 2023 against prior imagery from 29 April 2023 to\
    \ detect changes in surface water extent. Detected water polygons (approximately\
    \ 500 km\xB2) were intersected with WorldPop gridded population data to estimate\
    \ approximately 29,700 potentially affected people in the study area covering\
    \ Shabelle Zone (Ethiopia) and Beledweyne/Northern Bulo Burto District (Somalia)."
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
- href: https://data.humdata.org/dataset/water-extent-over-shabelle-zone-somali-region-ethiopia-and-beledweyne-and-northern-bulo-bu
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population potentially affected by satellite-detected surface water
      extent
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: AA:km2
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
  description: Satellite detected water extent over Shabelle Zone, Somali Region,
    Ethiopia and Beledweyne and Northern Bulo Burto District, Hiraan Region of Somalia
    as of 14 May 2023 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3595/FL20230327SOM_gdb.zip
  format: Geodatabase
  id: resource_1daec5eb
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
    Ethiopia and Beledweyne and Northern Bulo Burto District, Hiraan Region of Somalia
    as of 14 May 2023 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3595/FL20230327SOM_SHP.zip
  format: null
  id: resource_45cfea6d
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
slug: rdls_hel-ethsom_unosat_detectedwaterextentoversh_20230517
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
  start: '2023-05-17'
temporal_resolution: null
title: Satellite detected water extent over Shabelle Zone, Somali Region, Ethiopia
  and Beledweyne and Northern Bulo Burto District, Hiraan Region of Somalia as of
  14 May 2023
version: null
vulnerability: null
---
