---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/tropical-cyclones-judy-and-kevin-preliminary-satellite-derived-assessment-in-vanuatu-penam
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/tropical-cyclones-judy-and-kevin-preliminary-satellite-derived-assessment-in-vanuatu-penam
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/tropical-cyclones-judy-and-kevin-preliminary-satellite-derived-assessment-in-vanuatu-penam
dataset_id: rdls_hel-vut_unosat_tropicalcyclonesjudykevin_20230313
description: 'UNOSAT code TC20230227VUT, GDACS Id: 1000965 Status: Landslide, potentially
  affected road and damaged houses observed. Further action(s): Continue monitoring
  Summary of findings; Based on satellite images acquired on 04th, 09th and 11th of
  March 2023, the findings are the following: Tanna Island, Tafea Province; Widespread
  affected forest observed over Tanna Island; Potentially affected houses observed
  in West Tanna Council, Tafea Province; Widespread damaged houses observed in Lawir
  Village, Tanna Island, North Tanna Council, Tafea Province; Efate Island, Shefa
  Province; Widepsread affected forest observed over Efate Island; Tongoa Island,
  Shefa Province Widespread affected forest observed over Tongoa Island; South Pentecost
  Island, Penama Province No visible affected forest observed over cloud free areas
  in South Pentecost Island, South Pentecost Council, Penama Province; Ambae Island,
  West Ambae Council, Penama Province; Landslide observed in Ambae Island, West Ambae
  Council, Penama Province ; Affected shoreline observed in Ambae Island, West Ambae
  Council, Penama Province ; Potentially affected road and potentially affected houses
  observed in Ambae Island, West Ambae Council, Penama Province ; Malekula Island,
  Malampa Province; Affected shoreline observed in South Malekula Council, Malampa
  Province;. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/tropical-cyclones-judy-and-kevin-preliminary-satellite-derived-assessment-in-vanuatu-penam]'
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
    description: Residential and settlement building stock affected by tropical cyclones
      in Vanuatu provinces
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
    description: Forest areas affected by tropical cyclone damage on Tanna Island
    id: natural_environment
    scheme: null
    title: null
    uri: null
  category: natural_environment
  id: exposure_2
  metrics:
  - dimension: product
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
- asset_type:
    description: Road network potentially affected by landslides and cyclone impacts
    id: infrastructure
    scheme: null
    title: null
    uri: null
  category: infrastructure
  id: exposure_3
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: length
      unit: null
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
      intensity_measure: sws_10m:m/s
      process: tropical_cyclone
      trigger: null
      type: strong_wind
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: strong_wind
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts reviewed and compared satellite imagery acquired on
    4th, 9th, and 11th March 2023 to identify notable changes and damage patterns.
    Damage assessments were conducted through visual interpretation of satellite imagery,
    with results mapped and validated across four provinces (Penama, Malampa, Shefa,
    Tafea) in Vanuatu to produce a preliminary post-event impact assessment.
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/tropical-cyclones-judy-and-kevin-preliminary-satellite-derived-assessment-in-vanuatu-penam
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from tropical cyclones Judy and Kevin observed
      in settlements across Vanuatu
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: natural_environment
    asset_dimension: product
    description: Forest damage from tropical cyclone impacts on Tanna Island
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: area
          unit: null
        metric: loss
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
  description: Tropical Cyclones Judy And Kevin, Preliminary Satellite-derived Assessment
    in Vanuatu-Penama, Malampa, Shefa, and Tefea Provinces (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3526/TC20230227VUT_gdb.zip
  format: Geodatabase
  id: resource_519ffe30
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20230227VUT_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Tropical Cyclones Judy And Kevin, Preliminary Satellite-derived Assessment
    in Vanuatu-Penama, Malampa, Shefa, and Tefea Provinces (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3526/TC20230227VUT_SHP.zip
  format: null
  id: resource_fa96e8ef
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20230227VUT_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-vut_unosat_tropicalcyclonesjudykevin_20230313
spatial:
  bbox: null
  centroid: null
  countries:
  - VUT
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-03-13'
temporal_resolution: null
title: Tropical Cyclones Judy And Kevin, Preliminary Satellite-derived Assessment
  in Vanuatu-Penama, Malampa, Shefa, and Tefea Provinces
version: null
vulnerability: null
---
