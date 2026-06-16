---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-unosat-damage-assessment-activities-in-viti-levu-island-fiji-march-10-2016
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-unosat-damage-assessment-activities-in-viti-levu-island-fiji-march-10-2016
dataset_id: rdls_lss-fji_unosat_geodatadamageassessmentac_20160310
description: 'Tropical Cyclone Winston-UNOSAT Damage Assessment Activities in Viti
  Levu Island.. [Source: This metadata record was automatically extracted from the
  Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-unosat-damage-assessment-activities-in-viti-levu-island-fiji-march-10-2016]'
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
  description: UNOSAT analysts conducted post-event damage assessment by comparing
    satellite imagery acquired before and after Tropical Cyclone Winston (February
    2016) to identify and map damaged structures in Viti Levu Island, Fiji. Damage
    polygons were digitized with associated metadata including sensor date, sensor
    ID, and affected area in hectares and square meters.
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
- href: https://data.humdata.org/dataset/geodata-of-unosat-damage-assessment-activities-in-viti-levu-island-fiji-march-10-2016
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage assessment from Tropical Cyclone Winston
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
  description: Geodata of UNOSAT Damage Assessment Activities in Viti Levu Island,
    Fiji (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/FJ/TC20160219FJI/TC20160219FJI_shp.zip
  format: null
  id: resource_96bbd0b5
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20160219FJI_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of UNOSAT Damage Assessment Activities in Viti Levu Island,
    Fiji (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/FJ/TC20160219FJI/TC20160219FJI.gdb.zip
  format: null
  id: resource_46e55430
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20160219FJI.gdb.zip
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-fji_unosat_geodatadamageassessmentac_20160310
spatial:
  bbox: null
  centroid: null
  countries:
  - FJI
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2016-03-10'
temporal_resolution: null
title: Geodata of UNOSAT Damage Assessment Activities in Viti Levu Island, Fiji
version: null
vulnerability: null
---
