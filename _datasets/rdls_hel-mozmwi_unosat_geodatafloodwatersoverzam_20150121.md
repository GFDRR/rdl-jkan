---
attributions:
- entity:
    affiliation: null
    email: null
    name: World Population database
    url: https://data.humdata.org/dataset/geodata-of-flood-waters-over-zambezia-tete-and-sofala-provinces-mozambique-january-21-2015
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-flood-waters-over-zambezia-tete-and-sofala-provinces-mozambique-january-21-2015
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-flood-waters-over-zambezia-tete-and-sofala-provinces-mozambique-january-21-2015
dataset_id: rdls_hel-mozmwi_unosat_geodatafloodwatersoverzam_20150121
description: 'This map illustrates satellite-detected flood waters in the Caia, Chemba,
  Mopeia and Mutarara and Morrumbala Districts of Mozambique and southern Malawi along
  the Chire River as detected by Radarsat-2 imagery acquired 21 January 2015. Between
  11 December 2014 and 21 January 2015 flood waters affected roughly 55,000 hectares
  of lands in the five listed districts. About 31 villages are located within the
  flooded zone and according to the World Population database around 33,500 people
  are located within these potentially affected areas. This is a preliminary analysis
  and has not yet been validated in the field. Please send ground feedback to UNITAR
  / UNOSAT.. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-flood-waters-over-zambezia-tete-and-sofala-provinces-mozambique-january-21-2015]'
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
    description: Population located within potentially flood-affected areas estimated
      at 33,500 people across 31 villages
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
- asset_type:
    description: Agricultural land affected by flood waters covering approximately
      55,000 hectares
    id: agriculture
    scheme: null
    title: null
    uri: null
  category: agriculture
  id: exposure_2
  metrics:
  - dimension: product
    id: metric_1
    measurement:
      quantity_kind: area
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
      intensity_measure: AA:km2
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: flood
license: CC-BY-4.0
lineage:
  description: Radarsat-2 satellite imagery acquired on 21 January 2015 was analyzed
    by UNOSAT to detect flood water extent through comparison with baseline imagery.
    Detected inundation polygons were intersected with World Population database to
    estimate affected population (33,500 people) and agricultural land area (55,000
    hectares) across five districts in Mozambique and southern Malawi.
  sources:
  - id: source_1
    license: null
    name: United Nations Satellite Centre (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: World Population database
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/geodata-of-flood-waters-over-zambezia-tete-and-sofala-provinces-mozambique-january-21-2015
  rel: source
loss:
  losses:
  - asset_category: agriculture
    asset_dimension: product
    description: Direct agricultural land loss from fluvial flooding affecting 55,000
      hectares
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
  - asset_category: population
    asset_dimension: population
    description: Population affected by fluvial flooding estimated at 33,500 people
      in potentially inundated areas
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
  description: Geodata of Flood Waters Over Zambezia, Tete and Sofala Provinces, Mozambique
    (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/MZ/FL20150112MOZ/FL20150112MOZ_shp.zip
  format: null
  id: resource_012c146c
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20150112MOZ_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of Flood Waters Over Zambezia, Tete and Sofala Provinces, Mozambique
    (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/MZ/FL20150112MOZ/FL20150112MOZ.gdb.zip
  format: null
  id: resource_f27a9043
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20150112MOZ.gdb.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-mozmwi_unosat_geodatafloodwatersoverzam_20150121
spatial:
  bbox: null
  centroid: null
  countries:
  - MOZ
  - MWI
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2015-01-21'
temporal_resolution: null
title: Geodata of Flood Waters Over Zambezia, Tete and Sofala Provinces, Mozambique
version: null
vulnerability: null
---
