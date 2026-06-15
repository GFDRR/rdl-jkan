---
attributions:
- entity:
    affiliation: null
    email: null
    name: Humanitarian OpenStreetMap
    url: https://data.humdata.org/dataset/damage-assessment-of-pantoloan-area-in-central-sulawesi-2846
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Worldview-2 satellite imagery
    url: https://data.humdata.org/dataset/damage-assessment-of-pantoloan-area-in-central-sulawesi-2846
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-of-pantoloan-area-in-central-sulawesi-2846
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/damage-assessment-of-pantoloan-area-in-central-sulawesi-2846
dataset_id: rdls_el-idn_unosat_damageassessmentpantoloan_20181003
description: 'This map illustrates satellite-detected building damage assessment as
  of 02 October 2018, over Pantoloan area northeastern Palu city in Central Sulawesi
  following the 7.5 magnitude earthquake and subsequent tsunami of the 28th of September
  2018. The analysis was conducted using a post-event Worldview-2 satellite image
  acquired 2 October 2018. UNITAR-UNOSAT identified in the analysed area 424 potentially
  damaged structures.Taking into account the pre-building footprints provided by Humanitarian
  OpenStreetMap, this represents about 10% of the total number of structures damaged
  within this analysed zone of Pantoloan. This is a preliminary analysis and has not
  yet been validated in the field. Please send ground feedback to UNITAR - UNOSAT..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/damage-assessment-of-pantoloan-area-in-central-sulawesi-2846]'
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
    description: Building footprints in Pantoloan area identified from pre-event OpenStreetMap
      data
    id: buildings
    scheme: null
    title: null
    uri: null
  category: buildings
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts compared pre-event building footprints from Humanitarian
    OpenStreetMap with post-event Worldview-2 satellite imagery acquired 2 October
    2018 to detect structural damage in Pantoloan area. Visual change detection identified
    424 potentially damaged structures, representing approximately 10% of total structures
    in the analysis area.
  sources:
  - id: source_1
    license: null
    name: Humanitarian OpenStreetMap
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_2
    license: null
    name: Worldview-2 satellite imagery
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/damage-assessment-of-pantoloan-area-in-central-sulawesi-2846
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from 7.5 magnitude earthquake detected via
      satellite imagery
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
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from subsequent tsunami detected via satellite
      imagery
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_tsunami
      intensity_measure: wd:m
      process: null
      trigger: null
      type: tsunami
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
  description: Indonesia - Damage assessment of Pantoloan area in Central Sulawesi
    (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/ID/EQ20181001IDN/EQ20181001IDN_shp.zip
  format: null
  id: resource_31af4582
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20181001IDN_shp.zip
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-idn_unosat_damageassessmentpantoloan_20181003
spatial:
  bbox: null
  centroid: null
  countries:
  - IDN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2018-10-03'
temporal_resolution: null
title: Indonesia - Damage assessment of Pantoloan area in Central Sulawesi
version: null
vulnerability: null
---
