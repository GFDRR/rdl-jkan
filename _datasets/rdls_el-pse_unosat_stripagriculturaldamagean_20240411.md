---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/unosat-gaza-strip-agricultural-damage-analysis-1km-stretch-of-land-from-the-armistice-dema
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/unosat-gaza-strip-agricultural-damage-analysis-1km-stretch-of-land-from-the-armistice-dema
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/unosat-gaza-strip-agricultural-damage-analysis-1km-stretch-of-land-from-the-armistice-dema
dataset_id: rdls_el-pse_unosat_stripagriculturaldamagean_20240411
description: 'UNOSAT code: CE20231007PSE This map illustrates satellite-detected changes
  in agricultural areas in a stretch of land 1 km from the Armistice Demarcation Line
  in the Gaza Strip, Occupied Palestinian Territory. UNOSAT conducted an analysis
  utilising Sentinel-2 satellite imagery captured between January 2018 and 2024, performing
  a Normalised Difference Vegetation Index (NDVI) analysis as well as a multi-temporal
  classification to identify notable changes in agricultural areas during that time
  frame. The decline in the health and density of the crops can be observed due to
  the impact of activities such as razing, heavy vehicle activity, bombing, shelling,
  and other conflict-related dynamics. The analysis includes damage assessment for
  permanent crop fields, arable land, and fallow lands. UNOSAT analysis and statistics
  presented show the damaged agricultural area in sq km, percentage and percentage
  change for only the area contained within the zone. Statistical analysis shows an
  increase on the percentage of damaged agricultural land in October 2023 from 5.36%
  to 33.13% of damaged land in February 2024.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/unosat-gaza-strip-agricultural-damage-analysis-1km-stretch-of-land-from-the-armistice-dema]'
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
    description: Agricultural land areas in a 1 km stretch from the Armistice Demarcation
      Line, classified by vegetation health and crop density changes
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
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts performed Normalised Difference Vegetation Index (NDVI)
    analysis and multi-temporal classification on Sentinel-2 satellite imagery acquired
    between January 2018 and April 2024 to detect satellite-observed changes in agricultural
    vegetation health and crop density in a 1 km buffer zone from the Armistice Demarcation
    Line in Gaza, inferring agricultural damage from observed vegetation decline.
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/unosat-gaza-strip-agricultural-damage-analysis-1km-stretch-of-land-from-the-armistice-dema
  rel: source
loss:
  losses:
  - asset_category: agriculture
    asset_dimension: product
    description: Agricultural damage inferred from satellite-detected decline in crop
      health and vegetation density between January 2018 and April 2024
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
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
  description: Palestine - UNOSAT Gaza Strip Agricultural Damage Analysis 1km Stretch
    of Land from the Armistice Demarcation Line - April 2024 (Zipped geodatabase)
  download_url: https://unosat.org/static/unosat_filesystem/3821/CE20231007PSE_UNOSAT_1kmArmisticeDemarcationLine_09042024_GDB.zip
  format: Geodatabase
  id: resource_e8f45121
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20231007PSE_UNOSAT_1kmArmisticeDemarcationLine_09042024_GDB.zip
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-pse_unosat_stripagriculturaldamagean_20240411
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
  start: '2024-04-11'
temporal_resolution: null
title: Palestine - UNOSAT Gaza Strip Agricultural Damage Analysis 1km Stretch of Land
  from the Armistice Demarcation Line - April 2024
version: null
vulnerability: null
---
