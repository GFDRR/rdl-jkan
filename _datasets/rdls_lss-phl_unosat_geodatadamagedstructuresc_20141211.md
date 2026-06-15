---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damaged-structures-in-calbayog-city-samar-island-philippines-december-11-2014
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damaged-structures-in-calbayog-city-samar-island-philippines-december-11-2014
dataset_id: rdls_lss-phl_unosat_geodatadamagedstructuresc_20141211
description: 'This map illustrates damaged structures in Calbayog City, Samar Island,
  Philippines. Using a satellite image acquired 09 December 2014 and compared to an
  image collected 27 May 2014, UNOSAT reviewed the City of Calbayog and identified
  a total of 526 damaged structures in the area. 88 structures were identified as
  destroyed, 180 as severely damaged and 258 as moderately damaged. This is a preliminary
  analysis & has not yet been validated in the field. Please send ground feedback
  to UNITAR / UNOSAT.. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-damaged-structures-in-calbayog-city-samar-island-philippines-december-11-2014]'
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
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: UNOSAT analysts compared satellite imagery acquired on 27 May 2014
    (pre-event) with imagery from 09 December 2014 (post-event) to identify structural
    damage in Calbayog City caused by a tropical cyclone. Damage was classified into
    three severity categories (destroyed, severely damaged, moderately damaged) based
    on visual interpretation of satellite-detected changes. The resulting vector dataset
    contains 526 damaged structure locations with damage classification attributes.
  sources:
  - id: source_1
    license: null
    name: United Nations Satellite Centre (UNOSAT)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/geodata-of-damaged-structures-in-calbayog-city-samar-island-philippines-december-11-2014
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from tropical cyclone assessed via satellite
      imagery comparison
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
  description: Geodata of Damaged Structures in Calbayog City, Samar Island, Philippines
    (Shapefile)
  download_url: https://cern.ch/unosat-maps/PH/TC20141204PHL/TC20141204PHL_shp.zip
  format: null
  id: resource_f5119749
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20141204PHL_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of Damaged Structures in Calbayog City, Samar Island, Philippines
    (Shapefile)
  download_url: https://cern.ch/unosat-maps/PH/TC20141204PHL/TC20141204PHL.gdb.zip
  format: null
  id: resource_e89c6fff
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20141204PHL.gdb.zip
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-phl_unosat_geodatadamagedstructuresc_20141211
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
  start: '2014-12-11'
temporal_resolution: null
title: Geodata of Damaged Structures in Calbayog City, Samar Island, Philippines
version: null
vulnerability: null
---
