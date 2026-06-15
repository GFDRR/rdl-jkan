---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-crucita-area-manabi-province-ecuador-april-20-2016
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-crucita-area-manabi-province-ecuador-april-20-2016
dataset_id: rdls_el-ecu_unosat_geodatadamageassessmentcr_20160420
description: "This map illustrates satellite-detected potential damaged structures\
  \ in Crucita area in Manabi Province, Ecuador. Located at approximately 150 km south\
  \ of the 16 April 2016 Muisne earthquake mainshock epicenter and using a Pl\xE9\
  iades satellite image acquired the 19 April 2016 and a WorldView-2 image acquired\
  \ the 23 April 2015, UNITAR - UNOSAT identified 67 potentially damaged structures\
  \ within the map extent of which 7 are destroyed, 25 severely damaged, and 23 moderately\
  \ damaged. This is a preliminary analysis and not yet been validated in the field.\
  \ Please send ground feedback to UNITAR - UNOSAT.. [Source: This metadata record\
  \ was automatically extracted from the Humanitarian Data Exchange (HDX); Original\
  \ dataset: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-crucita-area-manabi-province-ecuador-april-20-2016]"
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
    description: Building structures in Crucita area classified by damage severity
      from satellite imagery
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
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: "UNOSAT analysts compared pre-event (23 April 2015 WorldView-2) and\
    \ post-event (19 April 2016 Pl\xE9iades) satellite imagery of the Crucita area\
    \ to detect structural damage from the 16 April 2016 Muisne earthquake. Visual\
    \ interpretation identified 67 potentially damaged structures classified into\
    \ three damage categories (destroyed, severely damaged, moderately damaged) as\
    \ preliminary field-unvalidated assessments."
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
- href: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-crucita-area-manabi-province-ecuador-april-20-2016
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage assessment from 16 April 2016 Ecuador earthquake
      detected via satellite imagery
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
  description: Geodata of Damage Assessment of Crucita Area, Manabi Province, Ecuador
    (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/EC/EQ20160417ECU/EQ20160417ECU_shp.zip
  format: null
  id: resource_055d66a6
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
  description: Geodata of Damage Assessment of Crucita Area, Manabi Province, Ecuador
    (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/EC/EQ20160417ECU/EQ20160417ECU.gdb.zip
  format: null
  id: resource_08f8fabe
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20160417ECU.gdb.zip
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-ecu_unosat_geodatadamageassessmentcr_20160420
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
  start: '2016-04-20'
temporal_resolution: null
title: Geodata of Damage Assessment of Crucita Area, Manabi Province, Ecuador
version: null
vulnerability: null
---
