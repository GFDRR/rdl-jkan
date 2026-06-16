---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damage-assessment-in-marcounda-sub-prefecture-central-african-repu-july-08-2014
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-damage-assessment-in-marcounda-sub-prefecture-central-african-repu-july-08-2014
dataset_id: rdls_lss-caf_unosat_geodatadamageassessmentma_20140708
description: 'This map illustrates locations of destroyed structures in the area of
  Marcounda Sub-Prefecture in the Central African Republic. Using satellite images
  acquired 21 June, 23 June & 7 July 2014, UNOSAT reviewed almost 4,500 square kilometers
  of Marcounda to locate signs of destroyed structures. An estimated 3,840 damaged
  structures are visible across 50 distinct locations in the sub-prefecture. Destruction
  in many cases was likely due to arson based on appearance of structural remains.
  In addition, it appears violence and destruction continued between 21 June and 7
  July, and heavy rains apparently caused significant damage to structures as well.
  Overall, UNOSAT estimates that approximately 40% of structures in Marcounda Sub-Prefecture
  have been completely destroyed and many others are likely damaged to some degree.
  This is a preliminary analysis and has not yet been validated in the field. Please
  send ground feedback to UNITAR / UNOSAT.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-damage-assessment-in-marcounda-sub-prefecture-central-african-repu-july-08-2014]'
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
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: "UNOSAT analysts reviewed multi-temporal satellite imagery of Marcounda\
    \ Sub-Prefecture acquired across three dates in June-July 2014, comparing images\
    \ to detect structural damage through visual interpretation. Approximately 4,500\
    \ km\xC2\xB2 was analyzed, identifying 3,840 damaged structures across 50 distinct\
    \ locations through change detection methodology."
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
- href: https://data.humdata.org/dataset/geodata-of-damage-assessment-in-marcounda-sub-prefecture-central-african-repu-july-08-2014
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from conflict-related destruction assessed
      via satellite imagery
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
  description: Geodata of Damage Assessment in Marcounda Sub-Prefecture, Central African
    Republic (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/CF/CE20131212CAF/CE20131212CAF_shp.zip
  format: null
  id: resource_922bfa20
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20131212CAF_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of Damage Assessment in Marcounda Sub-Prefecture, Central African
    Republic (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/CF/CE20131212CAF/CE20131212CAF.gdb.zip
  format: null
  id: resource_74415725
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20131212CAF.gdb.zip
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-caf_unosat_geodatadamageassessmentma_20140708
spatial:
  bbox: null
  centroid: null
  countries:
  - CAF
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2014-07-08'
temporal_resolution: null
title: Geodata of Damage Assessment in Marcounda Sub-Prefecture, Central African Republic
version: null
vulnerability: null
---
