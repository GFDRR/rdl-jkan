---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-idps-in-unmiss-bor-base-jonglei-state-south-sudan-october-30-2015
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-idps-in-unmiss-bor-base-jonglei-state-south-sudan-october-30-2015
dataset_id: rdls_el-ssd_unosat_geodataidpsunmissborbasej_20151030
description: 'This map illustrates satellite-detected areas of IDPs in Bor UNMISS
  Base and Protection of Civilian (PoC) areas, in Jonglei state, as seen by the WorldView-3
  satellite on 8 October 2015. The IDP structures were moved from the old PoC area
  in the northeast of the base to the new PoC area found in the south, and currently
  all the IDP shelters are now entirely in the southern extension of the UNMISS base.
  There are currently 1,077 structures in the IDP settlement with 101 consisting of
  infrastructure buildings and 976 of shelter structures. A large part of the camp
  still remains unoccupied and this can be seen as the Contingency area. This is a
  preliminary analysis and has not yet been validated in the field. Please send ground
  feedback to UNITAR -UNOSAT. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-idps-in-unmiss-bor-base-jonglei-state-south-sudan-october-30-2015]'
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
    description: IDP shelter structures and infrastructure buildings in UNMISS Bor
      Base PoC area
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
- asset_type:
    description: Internally displaced persons residing in satellite-detected structures
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_2
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: UNOSAT analysts reviewed WorldView-3 satellite imagery from 8 October
    2015 and compared multi-temporal images to identify and map IDP settlement structures
    in the UNMISS Bor Base. Structures were classified as shelter (976) or infrastructure
    (101) and georeferenced to document the relocation of IDPs from the northeast
    to the southern extension of the base.
  sources:
  - id: source_1
    license: null
    name: United Nations Satellite Centre (UNOSAT)
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/geodata-of-idps-in-unmiss-bor-base-jonglei-state-south-sudan-october-30-2015
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: IDP shelter structures affected by displacement and relocation within
      UNMISS base
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_1
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
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons in UNMISS Bor Base PoC area
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: displaced
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
  description: Geodata of IDPs in UNMISS Bor Base, Jonglei State, South Sudan (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SS/CE20131218SSD/CE20131218SSD_shp.zip
  format: null
  id: resource_b2558678
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20131218SSD_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of IDPs in UNMISS Bor Base, Jonglei State, South Sudan (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SS/CE20131218SSD/CE20131218SSD.gdb.zip
  format: null
  id: resource_14abe029
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20131218SSD.gdb.zip
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-ssd_unosat_geodataidpsunmissborbasej_20151030
spatial:
  bbox: null
  centroid: null
  countries:
  - SSD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2015-10-30'
temporal_resolution: null
title: Geodata of IDPs in UNMISS Bor Base, Jonglei State, South Sudan
version: null
vulnerability: null
---
