---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-saturated-soils-over-jowhar-middle-shabelle-region-somalia-november-03-2015
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-saturated-soils-over-jowhar-middle-shabelle-region-somalia-november-03-2015
dataset_id: rdls_hzd-som_unosat_geodatasaturatedsoilsover_20151103
description: 'This map illustrates satellite-detected areas of potentially saturated
  soils and probable flood waters in the Jowhar, Middle Shabelle region of Somalia.
  Using satellite imagery acquired 30 October 2015 and 02 January 2015, UNITAR-UNOSAT
  identified a total affected area of roughly 54,000 hectares in the Shabelle Dhexe
  and Hoose provinces. As of 30 October 2015, approximately 41,500 hectares of possibly
  saturated wet soils, as well as about 12,200 hectares of probable standing flood
  waters were detected over the districts of Jowhar, Balcad and, Afgooye. Due to the
  low spatial resolution of satellite data used for this analysis, the exact limit
  of flood water is uncertain. Detected water bodies likely reflect an underestimation
  of all flood-affected areas within the map extent. This analysis has not yet been
  validated in the field. Please send ground feedback to UNITAR-UNOSAT.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-saturated-soils-over-jowhar-middle-shabelle-region-somalia-november-03-2015]'
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
license: CC-BY-4.0
lineage:
  description: UNOSAT analysts compared satellite imagery from two dates (30 October
    2015 and 02 January 2015) to identify notable changes in soil saturation and surface
    water extent. Satellite-detected areas of potentially saturated soils and probable
    standing flood waters were mapped and quantified by area (hectares) across Jowhar,
    Balcad, and Afgooye districts in Middle Shabelle region.
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
- href: https://data.humdata.org/dataset/geodata-of-saturated-soils-over-jowhar-middle-shabelle-region-somalia-november-03-2015
  rel: source
loss: null
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
  description: Geodata of Saturated Soils Over Jowhar Middle Shabelle Region, Somalia
    (Shapefile)
  download_url: https://cern.ch/unosat-maps/SO/FL20151015SOM/FL20151015SOM_shp.zip
  format: null
  id: resource_2658ea6f
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20151015SOM_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of Saturated Soils Over Jowhar Middle Shabelle Region, Somalia
    (Shapefile)
  download_url: https://cern.ch/unosat-maps/SO/FL20151015SOM/FL20151015SOM_gdb.zip
  format: null
  id: resource_0d7a9c77
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20151015SOM_gdb.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-som_unosat_geodatasaturatedsoilsover_20151103
spatial:
  bbox: null
  centroid: null
  countries:
  - SOM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2015-11-03'
temporal_resolution: null
title: Geodata of Saturated Soils Over Jowhar Middle Shabelle Region, Somalia
version: null
vulnerability: null
---
