---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-idp-settlement-mpoko-airport-bangui-central-african-republic-june-26-2014
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-idp-settlement-mpoko-airport-bangui-central-african-republic-june-26-2014
dataset_id: rdls_el-caf_unosat_geodataidpsettlementmpoko_20140626
description: 'This map illustrates satellite-detected IDP shelters and administrative
  buildings in M''Poko Airport in Bangui, Central African Republic using satellite
  images acquired on the 20 January, 22 February and 6 June 2014. As of 22 February
  2014 approximately 7,789 structures were detected. Imagery from 6 June shows an
  important decrease in the number of tent shelters present inside of the airport
  since an extensive area has been significantly cleared of shelters. As of 6 June
  UNOSAT detected a total of approximately 3193 tent shelters and 61 administrative
  support and other structures. Compared to previous UNOSAT analysis the number of
  shelters has decreased by 58.7%. This is a preliminary analysis and has not yet
  been validated in the field. Please send ground feedback to UNITAR / UNOSAT.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-idp-settlement-mpoko-airport-bangui-central-african-republic-june-26-2014]'
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
    description: IDP shelter structures and administrative buildings detected via
      satellite imagery at M'Poko Airport settlement
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
  description: UNOSAT analysts reviewed and compared multi-temporal satellite imagery
    (January-June 2014) of M'Poko Airport IDP settlement in Bangui, identifying and
    mapping shelter structures and administrative buildings through visual interpretation
    and change detection. Structure counts were extracted for three time periods to
    track settlement dynamics during the complex emergency.
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
- href: https://data.humdata.org/dataset/geodata-of-idp-settlement-mpoko-airport-bangui-central-african-republic-june-26-2014
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Displacement-driven shelter structures quantified through satellite
      change detection analysis
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
  description: Geodata of IDP Settlement, M'Poko Airport, Bangui, Central African
    Republic (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/CF/CE20131212CAF/CE20131212CAF_shp.zip
  format: null
  id: resource_0bcdc6e7
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
  description: Geodata of IDP Settlement, M'Poko Airport, Bangui, Central African
    Republic (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/CF/CE20131212CAF/CE20131212CAF.gdb.zip
  format: null
  id: resource_006b6f98
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20131212CAF.gdb.zip
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-caf_unosat_geodataidpsettlementmpoko_20140626
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
  start: '2014-06-26'
temporal_resolution: null
title: Geodata of IDP Settlement, M'Poko Airport, Bangui, Central African Republic
version: null
vulnerability: null
---
