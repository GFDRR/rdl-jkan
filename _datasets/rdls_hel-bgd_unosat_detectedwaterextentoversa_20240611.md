---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/water-extent-over-satkhira-and-khulna-districts-khulna-divisions-bangladesh-as-of-1-june-2
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/water-extent-over-satkhira-and-khulna-districts-khulna-divisions-bangladesh-as-of-1-june-2
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-over-satkhira-and-khulna-districts-khulna-divisions-bangladesh-as-of-1-june-2
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extent-over-satkhira-and-khulna-districts-khulna-divisions-bangladesh-as-of-1-june-2
dataset_id: rdls_hel-bgd_unosat_detectedwaterextentoversa_20240611
description: 'UNOSAT code: FL20240502BGD, GDACS ID: 1001064 This map illustrates satellite-detected
  surface waters in Satkhira and Khulna Districts, Khulna Divisions, Bangladesh as
  observed from TANDEM_X images acquired on 1 June 2024 at 18:01 local time. Within
  the analyzed area of about 1,100 km2, about 200 km2 of land appears to be flooded.
  Based on Worldpop population data and the detected surface waters in the analyzed
  area, 124,000 people are potentially exposed or living close to the affected areas.
  UNITAR-UNOSAT identified 76,000 structures potentially exposed to floods in the
  analyzed area. This is a preliminary analysis and has not yet been validated in
  the field. Please send ground feedback to the United Nations Satellite Centre (UNOSAT).
  Important note: Flood analysis from radar images may underestimate the presence
  of standing waters in built-up areas and densely vegetated areas due to the backscattering
  properties of the radar signal.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/water-extent-over-satkhira-and-khulna-districts-khulna-divisions-bangladesh-as-of-1-june-2]'
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
    description: Structures potentially exposed to flood waters as identified by UNOSAT
      within the analyzed area of Satkhira and Khulna Districts
    id: buildings
    scheme: null
    title: null
    uri: null
  category: buildings
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
- asset_type:
    description: Population potentially exposed or living close to flooded areas,
      estimated using WorldPop population data intersected with detected surface waters
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_2
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard:
  event_sets_by_hazard_type:
    flood:
    - analysis_type: deterministic
      calculation_method: observed
      event_count: 0
      events: []
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_1
        intensity_measure: AA:km2
        process: coastal_flood
        trigger: null
        type: flood
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: 'TANDEM_X satellite imagery acquired on 1 June 2024 was analyzed by
    UNOSAT analysts to detect surface water extent through change detection and image
    comparison techniques, delineating approximately 200 km2 of flooded land within
    a 1,100 km2 study area. The detected flood extent was intersected with WorldPop
    population data to estimate exposed populations and with structural datasets to
    identify potentially affected buildings. The dataset supports rapid emergency
    response and situational awareness for the flood event (GDACS ID: 1001064) affecting
    Satkhira and Khulna Districts, Bangladesh.'
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
- href: https://data.humdata.org/dataset/water-extent-over-satkhira-and-khulna-districts-khulna-divisions-bangladesh-as-of-1-june-2
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Count of structures potentially exposed to flood inundation in Satkhira
      and Khulna Districts as of 1 June 2024
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
        modelling: inferred
        type: direct
      loss_approach: analytical
      loss_frequency_type: deterministic
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Estimated number of people potentially exposed or living close to
      flooded areas based on WorldPop data and satellite-detected water extent
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: AA:km2
      process: null
      trigger: null
      type: flood
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
        modelling: inferred
        type: direct
      loss_approach: analytical
      loss_frequency_type: deterministic
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
  description: Satellite detected water extent over Satkhira and Khulna Districts,
    Khulna Divisions, Bangladesh as of 1 June 2024 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3878/TC20240502BGD_GDB.zip
  format: Geodatabase
  id: resource_acd604a9
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20240502BGD_GDB.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extent over Satkhira and Khulna Districts,
    Khulna Divisions, Bangladesh as of 1 June 2024 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3878/TC20240502BGD_SHP.zip
  format: null
  id: resource_4fd05c08
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20240502BGD_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-bgd_unosat_detectedwaterextentoversa_20240611
spatial:
  bbox: null
  centroid: null
  countries:
  - BGD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2024-06-11'
temporal_resolution: null
title: Satellite detected water extent over Satkhira and Khulna Districts, Khulna
  Divisions, Bangladesh as of 1 June 2024
version: null
vulnerability: null
---
