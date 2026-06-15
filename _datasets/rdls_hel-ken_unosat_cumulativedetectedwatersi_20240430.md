---
attributions:
- entity:
    affiliation: null
    email: null
    name: NOAA-VIIRS
    url: https://data.humdata.org/dataset/cumulative-satellite-detected-waters-and-impact-in-kenya-between-24-to-28-april-2024
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/cumulative-satellite-detected-waters-and-impact-in-kenya-between-24-to-28-april-2024
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/cumulative-satellite-detected-waters-and-impact-in-kenya-between-24-to-28-april-2024
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/cumulative-satellite-detected-waters-and-impact-in-kenya-between-24-to-28-april-2024
dataset_id: rdls_hel-ken_unosat_cumulativedetectedwatersi_20240430
description: "UNOSAT code: FL20240426KEN This map illustrates cumulative satellite-detected\
  \ water using NOAA-VIIRS acquired between the 24th and the 28th of April 2024. about\
  \ 3,800 km\xB2 of land appear to be flooded. Based on Worldpop population data from\
  \ 2020 and the flood water extent, ~190,000 people are potentially exposed or living\
  \ close to flooded areas. This is a preliminary analysis and has not yet been validated\
  \ in the field. Please send ground feedback to the United Nations Satellite Centre\
  \ (UNOSAT). Important note: Population data used for this estimate is from 2020.\
  \ Current population count is not available.. [Source: This metadata record was\
  \ automatically extracted from the Humanitarian Data Exchange (HDX); Original dataset:\
  \ https://data.humdata.org/dataset/cumulative-satellite-detected-waters-and-impact-in-kenya-between-24-to-28-april-2024]"
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
      on WorldPop 2020 data
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
        intensity_measure: wd:m
        process: fluvial_flood
        trigger: null
        type: flood
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: "Satellite imagery from NOAA-VIIRS acquired between 24-28 April 2024\
    \ was analyzed by UNOSAT to detect cumulative water extent. The resulting flood\
    \ water polygon (3,800 km\xB2) was intersected with WorldPop 2020 population data\
    \ to estimate approximately 190,000 people potentially exposed to flooded areas.\
    \ This is a preliminary post-event impact assessment not yet validated in the\
    \ field."
  sources:
  - id: source_1
    license: null
    name: NOAA-VIIRS
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
- href: https://data.humdata.org/dataset/cumulative-satellite-detected-waters-and-impact-in-kenya-between-24-to-28-april-2024
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Approximately 190,000 people potentially exposed to flooded areas
      based on satellite-detected water extent and population data
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
  description: Cumulative Satellite Detected Waters and Impact in Kenya between 24
    to 28 April 2024 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3828/FL20240426KEN_gdb.zip
  format: Geodatabase
  id: resource_b5c6292b
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240426KEN_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Cumulative Satellite Detected Waters and Impact in Kenya between 24
    to 28 April 2024 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3828/FL20240426KEN_SHP.zip
  format: null
  id: resource_1e81b4ad
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240426KEN_SHP.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Cumulative Satellite Detected Waters and Impact in Kenya between 24
    to 28 April 2024 (Excel file)
  download_url: https://unosat.org/static/unosat_filesystem/3828/UNOSAT_PopulationExposure_FL20240426KEN_20240424_20240428.xlsx
  format: null
  id: resource_8588a278
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_PopulationExposure_FL20240426KEN_20240424_20240428.xlsx
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-ken_unosat_cumulativedetectedwatersi_20240430
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
  start: '2024-04-30'
temporal_resolution: null
title: Cumulative Satellite Detected Waters and Impact in Kenya between 24 to 28 April
  2024
version: null
vulnerability: null
---
