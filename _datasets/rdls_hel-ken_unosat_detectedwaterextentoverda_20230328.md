---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sentinel-2 satellite imagery
    url: https://data.humdata.org/dataset/water-extent-over-dagahaley-refugee-camp-garissa-county-kenya-as-of-26-march-2023
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop population data
    url: https://data.humdata.org/dataset/water-extent-over-dagahaley-refugee-camp-garissa-county-kenya-as-of-26-march-2023
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-over-dagahaley-refugee-camp-garissa-county-kenya-as-of-26-march-2023
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-over-dagahaley-refugee-camp-garissa-county-kenya-as-of-26-march-2023
dataset_id: rdls_hel-ken_unosat_detectedwaterextentoverda_20230328
description: 'UNOSAT code FL20230321KEN This map illustrates satellite detected surface
  waters in Dagahaley Refugee Camp, Dadaab sub-county, Garissa county, Kenya as observed
  from a Sentinel-2 image acquired on 26 March 2023 at 07:49 UTC. Within the analyzed
  area of about 45 km2, about 8 km2 of lands appear to be flooded. Based on Worldpop
  population data and the detected surface waters in the analyzed area, 8600 people
  are potentially exposed or living close to flooded areas. This is a preliminary
  analysis and has not yet been validated in the field. Please send ground feedback
  to United Nations Satellite Centre (UNOSAT).. [Source: This metadata record was
  automatically extracted from the Humanitarian Data Exchange (HDX); Original dataset:
  https://data.humdata.org/dataset/water-extent-over-dagahaley-refugee-camp-garissa-county-kenya-as-of-26-march-2023]'
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
    description: Population potentially exposed or living close to flooded areas in
      Dagahaley Refugee Camp
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
  event_sets_by_hazard_type:
    flood:
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
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: "Sentinel-2 satellite imagery from 26 March 2023 was analyzed by UNOSAT\
    \ analysts through visual interpretation and comparison to detect surface water\
    \ extent. The detected flooded area (8 km\xC2\xB2) was intersected with WorldPop\
    \ gridded population data to estimate 8,600 people potentially exposed to flooding\
    \ in Dagahaley Refugee Camp. This is a preliminary post-event assessment not yet\
    \ validated in the field."
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
- href: https://data.humdata.org/dataset/water-extent-over-dagahaley-refugee-camp-garissa-county-kenya-as-of-26-march-2023
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population exposed to flooded areas based on satellite-detected water
      extent and WorldPop data
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
  description: Satellite detected water extent over Dagahaley Refugee Camp, Garissa
    County, Kenya as of 26 March 2023 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3547/FL20230321KEN_gdb.zip
  format: Geodatabase
  id: resource_3d01b777
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20230321KEN_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extent over Dagahaley Refugee Camp, Garissa
    County, Kenya as of 26 March 2023 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3547/FL20230321KEN_SHP.zip
  format: null
  id: resource_7d257d70
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20230321KEN_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-ken_unosat_detectedwaterextentoverda_20230328
spatial:
  bbox: null
  centroid: null
  countries:
  - KEN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-03-28'
temporal_resolution: null
title: Satellite detected water extent over Dagahaley Refugee Camp, Garissa County,
  Kenya as of 26 March 2023
version: null
vulnerability: null
---
