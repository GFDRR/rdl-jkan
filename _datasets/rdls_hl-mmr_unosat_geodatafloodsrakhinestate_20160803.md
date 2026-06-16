---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-floods-in-rakhine-state-myanmar-situation-analysis-preliminary-rep-august-03-2016
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-floods-in-rakhine-state-myanmar-situation-analysis-preliminary-rep-august-03-2016
dataset_id: rdls_hl-mmr_unosat_geodatafloodsrakhinestate_20160803
description: 'Floods in Rakhine State, Myanmar-Situation Analysis Preliminary Report.
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-floods-in-rakhine-state-myanmar-situation-analysis-preliminary-rep-august-03-2016]'
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
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: UNOSAT analysts reviewed and compared satellite imagery from the flood
    event (sensor date 2016-07-14) to identify notable changes in surface water extent.
    Flood-affected areas were delineated and vectorized as polygon geometries with
    area measurements in square meters and hectares, producing a post-event damage/impact
    assessment of flood inundation.
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
- href: https://data.humdata.org/dataset/geodata-of-floods-in-rakhine-state-myanmar-situation-analysis-preliminary-rep-august-03-2016
  rel: source
loss:
  losses:
  - asset_category: natural_environment
    asset_dimension: product
    description: Flood-affected area extent mapped from satellite imagery in Rakhine
      State
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
  description: Geodata of Floods in Rakhine State, Myanmar-Situation Analysis Preliminary
    Report (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/MM/FL20160714MMR/FL20160714MMR_shp.zip
  format: null
  id: resource_b2ee378b
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20160714MMR_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of Floods in Rakhine State, Myanmar-Situation Analysis Preliminary
    Report (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/MM/FL20160714MMR/FL20160714MMR.gdb.zip
  format: null
  id: resource_effb652a
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20160714MMR.gdb.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-mmr_unosat_geodatafloodsrakhinestate_20160803
spatial:
  bbox: null
  centroid: null
  countries:
  - MMR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2016-08-03'
temporal_resolution: null
title: Geodata of Floods in Rakhine State, Myanmar-Situation Analysis Preliminary
  Report
version: null
vulnerability: null
---
