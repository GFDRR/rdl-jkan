---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-health-facilities-damage-assessment-in-gaza-strip-occupied-palesti-september-26-2014
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-health-facilities-damage-assessment-in-gaza-strip-occupied-palesti-september-26-2014
dataset_id: rdls_el-pse_unosat_geodatadamageassessmentst_20140926
description: 'This map illustrates satellite-detected damage and destruction of health
  facilities in Gaza Strip, resulting from recent conflicts in the area. Using satellite
  imagery collected 14 August 2014 and 27-28 August 2014 by the Pleiades satellite,
  and compared with a pre-crisis Pleiades image collected 6 July 2014, UNOSAT analysis
  has identified 4 destroyed structures, 1 severely damaged structures, 13 moderately
  damaged structures and 5 possibly damaged structures from a total of 101 hospitals
  in the Gaza Strip. The Governorate of Gaza represents 74% of the total damaged hosptial
  structures. This is a preliminary analysis & has not yet been validated in the field.
  Please send ground feedback to UNITAR / UNOSAT.. [Source: This metadata record was
  automatically extracted from the Humanitarian Data Exchange (HDX); Original dataset:
  https://data.humdata.org/dataset/geodata-of-health-facilities-damage-assessment-in-gaza-strip-occupied-palesti-september-26-2014]'
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
    description: Health facility infrastructure (hospitals) in Gaza Strip with structural
      inventory
    id: infrastructure
    scheme: null
    title: null
    uri: null
  category: infrastructure
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
  description: UNOSAT analysts compared multi-temporal Pleiades satellite imagery
    (pre-crisis baseline from 6 July 2014 versus post-crisis imagery from 14 and 27-28
    August 2014) to identify and classify damage to 101 health facilities across Gaza
    Strip. Damage was categorized into four severity classes (destroyed, severely
    damaged, moderately damaged, possibly damaged) with spatial coordinates and confidence
    levels recorded for each facility.
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
- href: https://data.humdata.org/dataset/geodata-of-health-facilities-damage-assessment-in-gaza-strip-occupied-palesti-september-26-2014
  rel: source
loss:
  losses:
  - asset_category: infrastructure
    asset_dimension: structure
    description: Direct damage to health facilities from conflict-related destruction
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
  description: Palestine - Geodata of Damage Assessment in Gaza Strip, Occupied Palestinian
    Territory (Shapefile)
  download_url: https://cern.ch/unosat-maps/PS/CE20140715PSE/CE20140715PSE.shp.zip
  format: null
  id: resource_d7bb7fca
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
  description: Palestine - Geodata of Damage Assessment in Gaza Strip, Occupied Palestinian
    Territory (Shapefile)
  download_url: https://cern.ch/unosat-maps/PS/CE20140715PSE/CE20140715PSE.gdb.zip
  format: null
  id: resource_68c82f5b
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
slug: rdls_el-pse_unosat_geodatadamageassessmentst_20140926
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
  start: '2014-09-26'
temporal_resolution: null
title: Palestine - Geodata of Damage Assessment in Gaza Strip, Occupied Palestinian
  Territory
version: null
vulnerability: null
---
