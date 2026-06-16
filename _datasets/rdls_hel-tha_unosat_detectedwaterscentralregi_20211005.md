---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sentinel-1 SAR imagery
    url: https://data.humdata.org/dataset/satellite-detected-waters-in-the-central-region-of-thailand-as-of-3-october-2021
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop population data
    url: https://data.humdata.org/dataset/satellite-detected-waters-in-the-central-region-of-thailand-as-of-3-october-2021
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-waters-in-the-central-region-of-thailand-as-of-3-october-2021
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-waters-in-the-central-region-of-thailand-as-of-3-october-2021
dataset_id: rdls_hel-tha_unosat_detectedwaterscentralregi_20211005
description: 'UNOSAT code: FL20210928THA This map illustrates satellite-detected surface
  waters in Central part of Thailand as observed from a Sentinel-1 image acquired
  on 3 October 2021 at 06:08 local time. Within the analyzed area of about 91,000
  km2 , about 3,300 km2 of lands appear to be flooded. The water extent appears to
  have decreased of about 180 km2 since 27 September 2021. Based on Worldpop population
  data and the detected surface waters in the analyzed area, the potentially exposed
  population is 350,000 people mainly located in the Ayutthaya Province with ~ 76,000
  People. This is a preliminary analysis and has not yet been validated in the field.
  Please send ground feedback to United Nations Satellite Centre (UNOSAT). Important
  note: Flood analysis from radar images may underestimate the presence of standing
  waters in built-up areas and densely vegetated areas due to backscattering properties
  of the radar signal.. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-waters-in-the-central-region-of-thailand-as-of-3-october-2021]'
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
    description: Potentially exposed population in Central Thailand based on WorldPop
      data intersected with detected flood extent
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
  description: "UNOSAT analysts processed Sentinel-1 SAR imagery acquired on 3 October\
    \ 2021 to detect surface water extent through comparison with baseline imagery,\
    \ identifying approximately 3,300 km\xC2\xB2 of flooded area in Central Thailand.\
    \ Detected water polygons were intersected with WorldPop gridded population data\
    \ to estimate 350,000 potentially exposed people, primarily in Ayutthaya Province."
  sources:
  - id: source_1
    license: null
    name: Sentinel-1 SAR imagery
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
- href: https://data.humdata.org/dataset/satellite-detected-waters-in-the-central-region-of-thailand-as-of-3-october-2021
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population potentially exposed to detected surface waters from fluvial
      flooding
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
  description: Satellite detected waters in the Central region of Thailand as of 3
    October 2021 (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/TH/FL20210928THA/FL20210928THA_gdb.zip
  format: Geodatabase
  id: resource_378ab84c
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20210928THA_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected waters in the Central region of Thailand as of 3
    October 2021 (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/TH/FL20210928THA/FL20210928THA_SHP.zip
  format: null
  id: resource_9f2898b9
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20210928THA_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-tha_unosat_detectedwaterscentralregi_20211005
spatial:
  bbox: null
  centroid: null
  countries:
  - THA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2021-10-05'
temporal_resolution: null
title: Satellite detected waters in the Central region of Thailand as of 3 October
  2021
version: null
vulnerability: null
---
