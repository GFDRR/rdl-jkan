---
attributions:
- entity:
    affiliation: null
    email: null
    name: Worldpop
    url: https://data.humdata.org/dataset/mudflow-impact-in-eshkmesh-district-takhar-province-and-burka-district-baghlan-province-af
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Sentinel-2
    url: https://data.humdata.org/dataset/mudflow-impact-in-eshkmesh-district-takhar-province-and-burka-district-baghlan-province-af
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/mudflow-impact-in-eshkmesh-district-takhar-province-and-burka-district-baghlan-province-af
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/mudflow-impact-in-eshkmesh-district-takhar-province-and-burka-district-baghlan-province-af
dataset_id: rdls_hel-afg_unosat_mudflowimpacteshkmeshdist_20240520
description: "UNOSAT code: FL20240512AFG, GDACS ID: 1102616 This map illustrates satellite-detected\
  \ mudflow extent Eshkmesh District, Takhar Province and Burka District, Baghlan\
  \ Province, Afghanistan as observed from a Sentinel-2 image acquired on 15 May 2024\
  \ at 14:04 local time (09:34 UTC). Within the analysed area of about 1,000 km\xB2\
  , a total of about 65 km\xB2 of lands appear to be affected by mudflow. Based on\
  \ Worldpop population data and the extent of the mudflows, about 12,000 people are\
  \ potentially affected by mudflows. This is a preliminary analysis and has not yet\
  \ been validated in the field. Please send ground feedback to the United Nations\
  \ Satellite Centre (UNOSAT).. [Source: This metadata record was automatically extracted\
  \ from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/mudflow-impact-in-eshkmesh-district-takhar-province-and-burka-district-baghlan-province-af]"
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
    description: Residential population potentially affected by mudflow based on WorldPop
      data
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
    landslide:
    - analysis_type: empirical
      calculation_method: observed
      event_count: 0
      events: []
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_1
        intensity_measure: LSI:-
        process: landslide_mudflow
        trigger: null
        type: landslide
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: "UNOSAT analysts performed satellite-based change detection by comparing\
    \ Sentinel-2 imagery acquired on 15 May 2024 with reference imagery to delineate\
    \ mudflow extent across approximately 1,000 km\xB2 in Takhar and Baghlan provinces.\
    \ Population exposure was estimated by overlaying the mudflow extent polygon with\
    \ WorldPop gridded population data. The resulting geodatabase contains the observed\
    \ hazard footprint and derived population impact estimates."
  sources:
  - id: source_1
    license: null
    name: Worldpop
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_2
    license: null
    name: Sentinel-2
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/mudflow-impact-in-eshkmesh-district-takhar-province-and-burka-district-baghlan-province-af
  rel: source
loss:
  losses:
  - asset_category: natural_environment
    asset_dimension: product
    description: "Direct land area affected by mudflow extent (approximately 65 km\xB2\
      )"
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: AA:km2
      process: null
      trigger: null
      type: landslide
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: area
          unit: null
        metric: exposure
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Population potentially affected by mudflow (approximately 12,000
      people)
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_landslide
      intensity_measure: LSI:-
      process: null
      trigger: null
      type: landslide
    id: loss_2
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
  description: Mudflow impact in Eshkmesh District, Takhar Province and Burka District,
    Baghlan Province, Afghanistan as of 15 May 2024 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3848/FL20240512AFG_gdb.zip
  format: Geodatabase
  id: resource_e30f8db5
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20240512AFG_gdb.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-afg_unosat_mudflowimpacteshkmeshdist_20240520
spatial:
  bbox: null
  centroid: null
  countries:
  - AFG
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2024-05-20'
temporal_resolution: null
title: Mudflow impact in Eshkmesh District, Takhar Province and Burka District, Baghlan
  Province, Afghanistan as of 15 May 2024
version: null
vulnerability: null
---
