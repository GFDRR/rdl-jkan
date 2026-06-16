---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-taiz-city-at-taziah-district-yemen-july-03-2015
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-taiz-city-at-taziah-district-yemen-july-03-2015
dataset_id: rdls_el-yem_unosat_geodatadamageassessmentta_20150703
description: 'This map illustrates satellite-detected areas of destruction in the
  majority of Taiz, Yemen, as seen by the WorldView-3 satellite on 26 June 2015. UNOSAT
  identified a total of 328 damaged buildings (54 destroyed, 66 severely damaged,
  156 moderately damaged, 52 possibly damaged) as well as 410 areas with significant
  amounts of debris. A total of 11 health centers are possibly damaged as they are
  within 100 meters of other destroyed or damaged buildings. This is a preliminary
  analysis and has not yet been validated in the field. Note that satellite imagery
  analysis will not capture all damage to buildings and instead only detects significant
  or catastrophic amounts of structural damage. Please send ground feedback to UNITAR
  - UNOSAT.. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-taiz-city-at-taziah-district-yemen-july-03-2015]'
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
    description: Building stock in Taiz City classified by damage severity (destroyed,
      severely damaged, moderately damaged, possibly damaged)
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
    description: Health centers potentially damaged by proximity to destroyed or damaged
      buildings
    id: infrastructure
    scheme: null
    title: null
    uri: null
  category: infrastructure
  id: exposure_2
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: CC-BY-4.0
lineage:
  description: UNOSAT analysts conducted multi-temporal satellite imagery analysis
    comparing WorldView-3 images to detect structural damage in Taiz City. Damaged
    buildings were classified into four severity categories (destroyed, severely damaged,
    moderately damaged, possibly damaged) and debris areas were mapped. Health facility
    vulnerability was assessed through spatial proximity analysis to damaged structures.
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
- href: https://data.humdata.org/dataset/geodata-of-damage-assessment-of-taiz-city-at-taziah-district-yemen-july-03-2015
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage assessed from satellite imagery including
      destroyed, severely damaged, moderately damaged, and possibly damaged structures
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
  - asset_category: infrastructure
    asset_dimension: structure
    description: Direct damage to health centers identified within 100 meters of destroyed
      or damaged buildings
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: convective_storm
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
  description: Geodata of Damage Assessment of Taiz City, At Ta'Ziah District, Yemen
    (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/YE/CE20150402YEM/CE20150402YEM_Taiz_20150626_shp.zip
  format: null
  id: resource_5704389a
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20150402YEM_Taiz_20150626_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of Damage Assessment of Taiz City, At Ta'Ziah District, Yemen
    (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/YE/CE20150402YEM/CE20150402YEM_Taiz_20150626_gdb.zip
  format: null
  id: resource_f7acce9c
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20150402YEM_Taiz_20150626_gdb.zip
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-yem_unosat_geodatadamageassessmentta_20150703
spatial:
  bbox: null
  centroid: null
  countries:
  - YEM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2015-07-03'
temporal_resolution: null
title: Geodata of Damage Assessment of Taiz City, At Ta'Ziah District, Yemen
version: null
vulnerability: null
---
