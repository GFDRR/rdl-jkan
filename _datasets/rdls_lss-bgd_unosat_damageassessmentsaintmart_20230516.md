---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/damage-assessment-in-saint-martins-island-coxbazar-district-chittagong-division-as-of-15-m
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Humanitarian OpenStreetMap
    url: https://data.humdata.org/dataset/damage-assessment-in-saint-martins-island-coxbazar-district-chittagong-division-as-of-15-m
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-saint-martins-island-coxbazar-district-chittagong-division-as-of-15-m
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-in-saint-martins-island-coxbazar-district-chittagong-division-as-of-15-m
dataset_id: rdls_lss-bgd_unosat_damageassessmentsaintmart_20230516
description: 'UNOSAT code TC20230510BGD, GDACS Id: 1000970 This map illustrates satellite-based
  damage assessment in Saint Martin''s Island Cox''Bazar District, Chattogram Division
  detected by using a Pleiades very high-resolution satellite image acquired on 15
  May 2023. Within the analyzed area, UNOSAT identified 211 affected and potentially
  affected structures. Taking into account the pre-building footprints provided by
  Humanitarian OpenStreetMap, this represents about 17% of the total number of structures
  affected in Saint Martin''s Island. This is a preliminary analysis and has not yet
  been validated in the field. Please send ground feedback to United Nations Satellite
  Centre (UNOSAT).. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/damage-assessment-in-saint-martins-island-coxbazar-district-chittagong-division-as-of-15-m]'
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
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: 'Post-event satellite imagery (Pleiades, 15 May 2023) was compared
    against pre-event imagery and Humanitarian OpenStreetMap building footprints to
    detect structural damage caused by Cyclone Mocha (GDACS Id: 1000970) on Saint
    Martin''s Island, Cox''s Bazar District. UNOSAT analysts visually interpreted
    change detection results to classify structures as affected or potentially affected,
    producing a preliminary damage assessment geodataset.'
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
    name: Humanitarian OpenStreetMap
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/damage-assessment-in-saint-martins-island-coxbazar-district-chittagong-division-as-of-15-m
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Satellite-based damage assessment identifying 211 affected and potentially
      affected structures on Saint Martin's Island following Cyclone Mocha (TC20230510BGD),
      representing ~17% of total structures
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: convective_storm
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
  description: Bangladesh - Damage assessment in Saint Martin's Island Cox'Bazar District,
    Chittagong Division as of 15 May 2023 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3593/TC20230510BGD_gdb.zip
  format: Geodatabase
  id: resource_0be88b18
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20230510BGD_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bangladesh - Damage assessment in Saint Martin's Island Cox'Bazar District,
    Chittagong Division as of 15 May 2023 (Zipped shapefile)
  download_url: https://unosat.org/static/unosat_filesystem/3593/TC20230510BGD_shp.zip
  format: null
  id: resource_09e6f39c
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20230510BGD_shp.zip
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-bgd_unosat_damageassessmentsaintmart_20230516
spatial:
  bbox: null
  centroid: null
  countries:
  - BGD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-05-16'
temporal_resolution: null
title: Bangladesh - Damage assessment in Saint Martin's Island Cox'Bazar District,
  Chittagong Division as of 15 May 2023
version: null
vulnerability: null
---
