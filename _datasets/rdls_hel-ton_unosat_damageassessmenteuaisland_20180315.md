---
attributions:
- entity:
    affiliation: null
    email: null
    name: Humanitarian Open Street Map
    url: https://data.humdata.org/dataset/damage-assessment-of-eua-island-tonga
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldView-2 satellite imagery
    url: https://data.humdata.org/dataset/damage-assessment-of-eua-island-tonga
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: GeoEye-1 satellite imagery
    url: https://data.humdata.org/dataset/damage-assessment-of-eua-island-tonga
  id: attribution_3
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-of-eua-island-tonga
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-of-eua-island-tonga
dataset_id: rdls_hel-ton_unosat_damageassessmenteuaisland_20180315
description: 'This map illustrates satellite-detected building damage assessment as
  of 13 February 2018, over the Island of Eua, Tonga, following the passage of the
  tropical cyclone GITA-18. The analysis was conducted using post-event WorldView-2
  images and pre-event GeoEye-1 images as of 28 June 2017. A total of 542 buildings
  were detected as damaged over the towns of Houma, Ohnoua, Pangai and Tufuvai. According
  to the pre-building footprints provided by Humanitarian Open Street Map, this represents
  47% of the total number of structures in Eua Island. The analysis could have been
  underestimated due to cloud cover. This is a preliminary analysis and has not yet
  been validated in the field. Please send ground feedback to UNITAR - UNOSAT.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/damage-assessment-of-eua-island-tonga]'
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
    description: Building footprints across Eua Island detected from pre-event satellite
      imagery
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
hazard:
  event_sets_by_hazard_type:
    strong_wind:
    - analysis_type: probabilistic
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
  event_sets_count: 1
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: 'Post-event damage assessment conducted by UNOSAT using multi-temporal
    satellite imagery comparison: pre-event GeoEye-1 imagery (28 June 2017) and post-event
    WorldView-2 imagery (13 February 2018) were analyzed to detect building damage
    from tropical cyclone GITA-18. Building footprints from Humanitarian Open Street
    Map provided the baseline inventory. Satellite analysts visually identified structural
    changes and damage signatures, resulting in detection of 542 damaged buildings
    representing 47% of total structures on Eua Island.'
  sources:
  - id: source_1
    license: null
    name: Humanitarian Open Street Map
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_2
    license: null
    name: WorldView-2 satellite imagery
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_3
    license: null
    name: GeoEye-1 satellite imagery
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/damage-assessment-of-eua-island-tonga
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from tropical cyclone GITA-18 assessed via
      satellite imagery comparison
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
        modelling: simulated
        type: direct
      loss_approach: analytical
      loss_frequency_type: probabilistic
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
  description: Damage Assessment of Eua Island, Tonga (zipped shapefile)
  download_url: https://cern.ch/unosat-maps/TO/TC20180209TON/TC20180209TON_shp.zip
  format: null
  id: resource_ad41ad37
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20180209TON_shp.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-ton_unosat_damageassessmenteuaisland_20180315
spatial:
  bbox: null
  centroid: null
  countries:
  - TON
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2018-03-15'
temporal_resolution: null
title: Damage Assessment of Eua Island, Tonga
version: null
vulnerability: null
---
