---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/water-extents-and-damage-assessment-as-of-7-march-2020-over-the-eastern-part-of-ncheta-zam
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extents-and-damage-assessment-as-of-7-march-2020-over-the-eastern-part-of-ncheta-zam
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/water-extents-and-damage-assessment-as-of-7-march-2020-over-the-eastern-part-of-ncheta-zam
dataset_id: rdls_hel-zmb_unosat_detectedwaterextentsdamag_20200310
description: 'UNOSAT code: FL20200305ZMB This map illustrates satellite-detected water
  extents in the eastern part of Ncheta Island, Lunga District, Luapula Province,
  Republic of Zambia as observed form Pleiades imagery acquired on 7 March 2020. Within
  the analyzed area several hectares of land appear to be flooded and 29 structures
  out of 300 are likely flooded within this area. This is a preliminary analysis and
  has not yet been validated in the field. Please send ground feedback to UNITAR-UNOSAT..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/water-extents-and-damage-assessment-as-of-7-march-2020-over-the-eastern-part-of-ncheta-zam]'
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
    description: Building stock in the analyzed area of Ncheta Island (300 structures
      inventoried)
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
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: Pleiades satellite imagery acquired on 7 March 2020 over eastern Ncheta
    Island was analyzed by UNOSAT analysts through visual interpretation and multi-temporal
    comparison to detect water extents and identify flooded structures. Water extent
    polygons and affected building locations were extracted and validated against
    the 300-structure inventory to produce preliminary damage assessment maps.
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/water-extents-and-damage-assessment-as-of-7-march-2020-over-the-eastern-part-of-ncheta-zam
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from fluvial flooding (29 structures likely
      flooded out of 300)
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
  description: Satellite detected water extents and damage assessment over the eastern
    part of Ncheta, Zambia (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/ZM/FL20200305ZMB/FL20200305ZMB_gdb.zip
  format: Geodatabase
  id: resource_1168c3b0
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20200305ZMB_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extents and damage assessment over the eastern
    part of Ncheta, Zambia (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/ZM/FL20200305ZMB/FL20200305ZMB_SHP.zip
  format: null
  id: resource_8da440bd
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20200305ZMB_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-zmb_unosat_detectedwaterextentsdamag_20200310
spatial:
  bbox: null
  centroid: null
  countries:
  - ZMB
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2020-03-10'
temporal_resolution: null
title: Satellite detected water extents and damage assessment over the eastern part
  of Ncheta, Zambia
version: null
vulnerability: null
---
