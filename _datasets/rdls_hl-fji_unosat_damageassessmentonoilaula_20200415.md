---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/damage-assessment-in-ono-i-lau-lau-province-eastern-division-republic-of-fiji
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: OpenStreetMap
    url: https://data.humdata.org/dataset/damage-assessment-in-ono-i-lau-lau-province-eastern-division-republic-of-fiji
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-ono-i-lau-lau-province-eastern-division-republic-of-fiji
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-ono-i-lau-lau-province-eastern-division-republic-of-fiji
dataset_id: rdls_hl-fji_unosat_damageassessmentonoilaula_20200415
description: 'UNOSAT code: TC20200408FJI This map illustrates potentially damaged
  structures and buildings in Ono-i-Lau, Lau Province, Eastern Division, Republic
  of Fiji as detected by satellite image acquired after landfall of the Tropical Cyclone
  Harold-20 on 08 April 2020. UNITAR-UNOSAT analysis used a Pleiades image acquired
  on 10 April 2020. Within Ono District, UNITAR-UNOSAT identified 23 potentially damages
  structures. Taking into account the pre-building footprints provided by OpenStreetMap,
  this represents about 8% of the total number of structures within the analyzed cloud
  free areas. This is a preliminary analysis and has not yet been validated in the
  field. Please send ground feedback to UNITAR - UNOSAT.. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/damage-assessment-in-ono-i-lau-lau-province-eastern-division-republic-of-fiji]'
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
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts compared Pleiades satellite imagery acquired on 10
    April 2020 (post-landfall) with pre-event building footprints from OpenStreetMap
    to identify structural changes and damage in Ono-i-Lau. Visual interpretation
    of satellite imagery detected 23 potentially damaged structures, representing
    approximately 8% of total structures in the cloud-free analyzed area.
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
    name: OpenStreetMap
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/damage-assessment-in-ono-i-lau-lau-province-eastern-division-republic-of-fiji
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from Tropical Cyclone Harold detected via
      satellite imagery analysis
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
  description: Damage Assessment in Ono-i-Lau, Lau Province, Eastern Division, Republic
    of Fiji (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/FJ/TC20200408FJI/TC20200408FJI_gdb.zip
  format: Geodatabase
  id: resource_5dfb422e
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20200408FJI_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Damage Assessment in Ono-i-Lau, Lau Province, Eastern Division, Republic
    of Fiji (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/FJ/TC20200408FJI/TC20200408FJI_SHP.zip
  format: null
  id: resource_08ecf558
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20200408FJI_SHP.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-fji_unosat_damageassessmentonoilaula_20200415
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
  start: '2020-04-15'
temporal_resolution: null
title: Damage Assessment in Ono-i-Lau, Lau Province, Eastern Division, Republic of
  Fiji
version: null
vulnerability: null
---
