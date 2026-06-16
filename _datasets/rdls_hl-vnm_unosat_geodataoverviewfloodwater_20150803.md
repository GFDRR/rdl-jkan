---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-overview-of-flood-waters-near-hai-phong-city-vietnam-august-03-2015
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-overview-of-flood-waters-near-hai-phong-city-vietnam-august-03-2015
dataset_id: rdls_hl-vnm_unosat_geodataoverviewfloodwater_20150803
description: 'This map gives an overview of satellite detected waters in Song Lach
  Tray delta near Hai Phong City in northern Vietnam. Due to continuous rain, there
  is a notable increase in inundated fields along the coast in Hai Phong and Quang
  Ninh Provinces. In the analyzed area, approximately 30,000 hectares of land has
  been classified as flood affected. Many identified flooded regions are in close
  proximity to Ha Long Bay in Gulf of Tonkin, a UNESCO World Heritage Site. This is
  a preliminary analysis and has not yet been validated in the field. Please send
  ground feedback to UNITAR-UNOSAT.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-overview-of-flood-waters-near-hai-phong-city-vietnam-august-03-2015]'
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
      intensity_measure: AA:km2
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-4.0
lineage:
  description: UNOSAT analysts reviewed and compared satellite imagery from the event
    date (2015-07-30) to detect notable changes in water extent. Flooded regions were
    delineated as polygons with area calculations in hectares and square meters. The
    dataset represents observed flood extent rather than modeled hazard, with preliminary
    validation status noted.
  sources:
  - id: source_1
    license: null
    name: United Nations Satellite Centre (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/geodata-of-overview-of-flood-waters-near-hai-phong-city-vietnam-august-03-2015
  rel: source
loss:
  losses:
  - asset_category: agriculture
    asset_dimension: product
    description: Direct agricultural land inundation from fluvial flooding detected
      via satellite imagery
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
  description: Geodata of Overview of Flood Waters Near Hai Phong City, Vietnam (Shapefile)
  download_url: https://cern.ch/unosat-maps/VN/FL20150730VNM/FL20150730VNM_shp.zip
  format: null
  id: resource_017ff2e7
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20150730VNM_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of Overview of Flood Waters Near Hai Phong City, Vietnam (Shapefile)
  download_url: https://cern.ch/unosat-maps/VN/FL20150730VNM/FL20150730VNM_gdb.zip
  format: null
  id: resource_61672d8c
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20150730VNM_gdb.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-vnm_unosat_geodataoverviewfloodwater_20150803
spatial:
  bbox: null
  centroid: null
  countries:
  - VNM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2015-08-03'
temporal_resolution: null
title: Geodata of Overview of Flood Waters Near Hai Phong City, Vietnam
version: null
vulnerability: null
---
