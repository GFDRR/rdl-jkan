---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-san-vicente-manabi-province-ecuador-april-21-2016
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-san-vicente-manabi-province-ecuador-april-21-2016
dataset_id: rdls_lss-ecu_unosat_geodatadamageassessmentsa_20160421
description: "This map illustrates satellite-detected, potential damaged structures\
  \ in San Vicente, Manabi Province, Ecuador. The analyzed area is located approximately\
  \ 120 km south of the 16 April 2016 Muisne earthquake mainshock epicenter. This\
  \ analysis is done using Pl\xE9iades satellite image acquired 19 April 2016 and\
  \ a WorldView-2 image acquired 02 December 2013. UNITAR-UNOSAT identified 102 potentially\
  \ damaged structures of which 25 are destroyed, 46 severely damaged, and 31 moderately\
  \ damaged. This is a preliminary analysis and not yet been validated in the field.\
  \ Please send ground feedback to UNITAR-UNOSAT.. [Source: This metadata record was\
  \ automatically extracted from the Humanitarian Data Exchange (HDX); Original dataset:\
  \ https://data.humdata.org/dataset/geodata-of-damage-assessment-of-san-vicente-manabi-province-ecuador-april-21-2016]"
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
license: CC-BY-4.0
lineage:
  description: "UNOSAT analysts compared Pl\xE9iades satellite imagery acquired 19\
    \ April 2016 (post-earthquake) with WorldView-2 baseline imagery from 02 December\
    \ 2013 to detect structural damage in San Vicente, Manabi Province. Visual interpretation\
    \ identified 102 potentially damaged structures classified by severity (25 destroyed,\
    \ 46 severely damaged, 31 moderately damaged), representing direct earthquake\
    \ impacts in the study area approximately 120 km from the mainshock epicenter."
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
- href: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-san-vicente-manabi-province-ecuador-april-21-2016
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from the 16 April 2016 Ecuador earthquake
      assessed via satellite imagery
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
  description: Geodata of Damage Assessment of San Vicente, Manabi Province, Ecuador
    (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/EC/EQ20160417ECU/EQ20160417ECU_shp.zip
  format: null
  id: resource_c2ccafaa
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20160417ECU_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of Damage Assessment of San Vicente, Manabi Province, Ecuador
    (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/EC/EQ20160417ECU/EQ20160417ECU.gdb.zip
  format: null
  id: resource_8d3281ce
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20160417ECU.gdb.zip
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-ecu_unosat_geodatadamageassessmentsa_20160421
spatial:
  bbox: null
  centroid: null
  countries:
  - ECU
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2016-04-21'
temporal_resolution: null
title: Geodata of Damage Assessment of San Vicente, Manabi Province, Ecuador
version: null
vulnerability: null
---
