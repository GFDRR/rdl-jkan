---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damage-to-agricultural-areas-and-greenhouses-gaza-strip-occupied-p-september-23-2014
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damage-to-agricultural-areas-and-greenhouses-gaza-strip-occupied-p-september-23-2014
dataset_id: rdls_el-pse_unosat_geodatadamageagricultural_20140923
description: 'This map illustrates satellite-detected changes in agricultural areas
  of the Gaza Strip resulting from the July ? August 2014 conflict in the area. Using
  a satellite image collected 14 August 2014 by the Pleiades satellite, and compared
  with a pre-crisis Pleiades image collected 6 July 2014, UNOSAT performed Normalized
  Difference Vegetation Index analysis, multitemporal classification, and manual review
  in order to detect significant changes occurring in agricultural areas between those
  dates. This methodology assessed damage occurring as a result of razing, heavy vehicle
  tracking, bombing, shelling, and related conflict dynamics. The analysis includes
  damage occurring to both active crop fields and fallow lands, as well as in many
  household gardens. Note that due to the special characteristics of the area analysed,
  razing might have been overestimated in sandy areas, and some ambiguity often exists
  between unused lands, pasture lands, agricultural fields, and other land cover types.
  UNOSAT analysis indicates that ~1,800 hectares of agricultural fields have likely
  been razed or heavily damaged by these factors in the intervening period. In addition,
  using imagery acquired on 27 and 28 August 2014 UNOSAT assessed damage to greenhouses
  and identified a total 657 destroyed, 214 severely damaged and 392 moderately damaged
  greenhouse structures. This is a preliminary analysis and has not yet been validated
  in the field. Please send ground feedback to UNITAR/UNOSAT.. [Source: This metadata
  record was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/geodata-of-damage-to-agricultural-areas-and-greenhouses-gaza-strip-occupied-p-september-23-2014]'
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
    description: Agricultural areas and greenhouses in Gaza Strip mapped by satellite
      imagery
    id: agriculture
    scheme: null
    title: null
    uri: null
  category: agriculture
  id: exposure_1
  metrics:
  - dimension: product
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
hazard: null
license: CC-BY-4.0
lineage:
  description: UNOSAT analysts compared pre-crisis Pleiades satellite imagery (6 July
    2014) with post-crisis imagery (14 August 2014) of Gaza Strip agricultural areas.
    Normalized Difference Vegetation Index analysis, multitemporal classification,
    and manual review were applied to detect significant changes in vegetation and
    identify damage from razing, vehicle tracking, and bombing. Damage polygons were
    delineated with confidence levels and area measurements in hectares.
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
- href: https://data.humdata.org/dataset/geodata-of-damage-to-agricultural-areas-and-greenhouses-gaza-strip-occupied-p-september-23-2014
  rel: source
loss:
  losses:
  - asset_category: agriculture
    asset_dimension: product
    description: Direct damage to agricultural areas and greenhouses from conflict-related
      activities including bombing and vehicle tracking
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
  description: Palestine - Geodata of Damage to Agricultural Areas and Greenhouses,
    Gaza Strip - Occupied Palestinian Territory (Shapefile)
  download_url: https://cern.ch/unosat-maps/PS/CE20140715PSE/CE20140715PSE.shp.zip
  format: null
  id: resource_9f5940ce
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20140715PSE.shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Palestine - Geodata of Damage to Agricultural Areas and Greenhouses,
    Gaza Strip - Occupied Palestinian Territory (Shapefile)
  download_url: https://cern.ch/unosat-maps/PS/CE20140715PSE/CE20140715PSE.gdb.zip
  format: null
  id: resource_11d0e6bb
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20140715PSE.gdb.zip
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-pse_unosat_geodatadamageagricultural_20140923
spatial:
  bbox: null
  centroid: null
  countries:
  - PSE
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2014-09-23'
temporal_resolution: null
title: Palestine - Geodata of Damage to Agricultural Areas and Greenhouses, Gaza Strip
  - Occupied Palestinian Territory
version: null
vulnerability: null
---
