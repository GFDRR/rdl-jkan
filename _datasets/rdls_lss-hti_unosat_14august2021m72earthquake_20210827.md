---
attributions:
- entity:
    affiliation: null
    email: null
    name: International Charter Space and Major Disasters
    url: https://data.humdata.org/dataset/14-august-2021-m7-2-haiti-earthquake-preliminary-satellite-based-comprehensive-damage-asse
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/14-august-2021-m7-2-haiti-earthquake-preliminary-satellite-based-comprehensive-damage-asse
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/14-august-2021-m7-2-haiti-earthquake-preliminary-satellite-based-comprehensive-damage-asse
dataset_id: rdls_lss-hti_unosat_14august2021m72earthquake_20210827
description: 'UNOSAT code: EQ20210814HTI This report describes preliminary building
  damage analysis covering the departments of South, Grande Anse, and Nippes of Haiti,
  for a total area of approximately 550 Km2. A building damage analysis and a rapid
  assessment of transportation network conditions was conducted by comparing a series
  of satellite imageries acquired from the International Charter Space and Major Disasters,
  before and after the earthquake. The preliminary analysis extent within South, Grande
  Anse, and Nippes departments identify a total of 1,842 buildings/structures with
  visible damages and approximately 130 locations with visible road obstacles and/or
  access constraints.. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/14-august-2021-m7-2-haiti-earthquake-preliminary-satellite-based-comprehensive-damage-asse]'
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
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts conducted post-event damage assessment by comparing
    multi-temporal satellite imagery from the International Charter Space and Major
    Disasters acquired before and after the 14 August 2021 M7.2 Haiti earthquake.
    Building damage and transportation network conditions were visually interpreted
    and classified across South, Grande Anse, and Nippes departments, with results
    delivered as vector geodatabase and shapefile formats.
  sources:
  - id: source_1
    license: null
    name: International Charter Space and Major Disasters
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/14-august-2021-m7-2-haiti-earthquake-preliminary-satellite-based-comprehensive-damage-asse
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage assessment from the 14 August 2021 M7.2 earthquake
      in Haiti
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
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
  - asset_category: infrastructure
    asset_dimension: structure
    description: Direct damage to transportation network infrastructure from the earthquake
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
    id: loss_2
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
  description: 14 August 2021 M7.2 Haiti Earthquake. Preliminary Satellite-Based Comprehensive
    Damage Assessment Report (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/HT/EQ20210814HTI/EQ20210814HTI_gdb.zip
  format: Geodatabase
  id: resource_a24d9f64
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20210814HTI_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 14 August 2021 M7.2 Haiti Earthquake. Preliminary Satellite-Based Comprehensive
    Damage Assessment Report (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/HT/EQ20210814HTI/EQ20210814HTI_shp.zip
  format: null
  id: resource_12273d20
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20210814HTI_shp.zip
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-hti_unosat_14august2021m72earthquake_20210827
spatial:
  bbox: null
  centroid: null
  countries:
  - HTI
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2021-08-27'
temporal_resolution: null
title: 14 August 2021 M7.2 Haiti Earthquake. Preliminary Satellite-Based Comprehensive
  Damage Assessment Report
version: null
vulnerability: null
---
