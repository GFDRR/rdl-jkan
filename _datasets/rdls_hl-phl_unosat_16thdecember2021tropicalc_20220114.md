---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/16th-of-december-2021-tropical-cyclone-rai-21-philippines-preliminary-satellite-based-comp
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Philippines National Disaster Risk Reduction and Management Council (NDRRMC)
    url: https://data.humdata.org/dataset/16th-of-december-2021-tropical-cyclone-rai-21-philippines-preliminary-satellite-based-comp
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/16th-of-december-2021-tropical-cyclone-rai-21-philippines-preliminary-satellite-based-comp
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/16th-of-december-2021-tropical-cyclone-rai-21-philippines-preliminary-satellite-based-comp
dataset_id: rdls_hl-phl_unosat_16thdecember2021tropicalc_20220114
description: 'UNOSAT code: TC20211216PHL A category 5 Tropical Cyclone RAI-21 struck
  the Philippines on the 16th of December 2021, causing damage, devastation, and destruction.
  The Tropical Cyclone RAI-21 made landfall north of General Luna city on Siargao
  Island, the easternmost island of the Philippines, and continued westward through
  the central part of the country. The Philippines National Disaster Risk Reduction
  and Management Council (NDRRMC) has stated that 2,182,791 families have been affected
  in 11 out of 17 regions of the Philippines. About 3M people, ~ 30% of the affected
  area population - need emergency humanitarian assistance. According to OCHA, the
  death toll has reached 177 persons, with more than 275 persons injured and 630,000
  displaced. More than 159,000 houses have been damaged, 61,900 have been destroyed.
  These figures are likely to rise as the after-effects of the Tropical Cyclone are
  fully realized. Preliminary assessment has shown devastating damage to houses, roads,
  and bridges disrupting aid movement into the affected areas. This report summarizes
  satellite-derived building damage analysis covering the most affected areas within
  Region IV-B (Mimaropa), Region VII (Central Visayas), Region VIII (Eastern Visayas),
  and Region XIII (Caraga) of the Philippines.. [Source: This metadata record was
  automatically extracted from the Humanitarian Data Exchange (HDX); Original dataset:
  https://data.humdata.org/dataset/16th-of-december-2021-tropical-cyclone-rai-21-philippines-preliminary-satellite-based-comp]'
details: This is a preliminary assessment and has not yet been validated in the field.
  It is important to consider the characteristics of the source imagery used in the
  analyses when interpreting results. For damage assessments it should be noted that
  only significant damage to the structural integrity of the buildings analyzed can
  be seen in imagery, while minor damage such as cracks or holes may not be visible
  at all. For flood extractions using radar data it is important to note that urban
  areas and highly vegetated areas may mask the flood signature and result in underestimation
  of flood waters. Users with specific questions or concerns should contact unosat@unitar.org
  to seek clarification.
exposure: []
hazard:
  event_sets:
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
  type: strong_wind
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts conducted post-event satellite image analysis by comparing
    pre- and post-cyclone imagery to identify structural damage to buildings and affected
    areas. Impact figures were compiled from NDRRMC official reports documenting 2.18M
    affected families across 11 regions. Damage polygons were digitized and compiled
    into geodatabase and shapefile formats for spatial analysis.
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: Philippines National Disaster Risk Reduction and Management Council (NDRRMC)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/16th-of-december-2021-tropical-cyclone-rai-21-philippines-preliminary-satellite-based-comp
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from tropical cyclone RAI-21 assessed via
      satellite imagery
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
  - asset_category: population
    asset_dimension: population
    description: Population affected by tropical cyclone RAI-21 across 11 regions
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
          quantity_kind: count
          unit: null
        metric: exposure
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
  description: 16th of December 2021 Tropical Cyclone RAI-21, Philippines. Preliminary
    Satellite-Based Comprehensive Damage Assessment (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/PH/TC20211216PHL/TC20211216PHL_gdb.zip
  format: Geodatabase
  id: resource_f2738620
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20211216PHL_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 16th of December 2021 Tropical Cyclone RAI-21, Philippines. Preliminary
    Satellite-Based Comprehensive Damage Assessment (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/PH/TC20211216PHL/TC20211216PHL_SHP.zip
  format: null
  id: resource_b4ecbd08
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20211216PHL_SHP.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-phl_unosat_16thdecember2021tropicalc_20220114
spatial:
  bbox: null
  centroid: null
  countries:
  - PHL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2022-01-14'
temporal_resolution: null
title: 16th of December 2021 Tropical Cyclone RAI-21, Philippines. Preliminary Satellite-Based
  Comprehensive Damage Assessment
version: null
vulnerability: null
---
