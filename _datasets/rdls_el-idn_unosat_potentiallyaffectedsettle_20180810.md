---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/potentially-affected-settlements-over-tanjung-and-pemenang-districts-lombok-utara-regency-nusa-
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/potentially-affected-settlements-over-tanjung-and-pemenang-districts-lombok-utara-regency-nusa-
dataset_id: rdls_el-idn_unosat_potentiallyaffectedsettle_20180810
description: 'This map illustrates satellite-detected potentially affected settlements
  over Tanjung and Pemenang Districts, in Lombok Utara Regency, as of 7 August 2018,
  after the 6.9 earthquake, that stroke Lombok Island on 5 August 2018. The analysis
  was conducted using post-event Pleiades satellite imagery acquired on 7 and 8 August
  2018. UNITAR-UNOSAT analysis shows an estimation of the settlement size (Hamlet,
  Little village and Major village) associated to a damage level (Moderately damaged,
  severely damaged and Destroyed). Within the map extent 49 settlements were categorized
  as destroyed, 57 as severely damaged and 129 as moderately damaged. Within the analysed
  area, Tanjung is the most affected district and Sigar Penjalin and Sokong are its
  most affected desa. In Pemenang district the most affected desa is Pemenang Barat.
  This is a preliminary analysis and has not yet been validated in the field. Please
  send ground feedback to UNITAR - UNOSAT.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/potentially-affected-settlements-over-tanjung-and-pemenang-districts-lombok-utara-regency-nusa-]'
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
    description: Settlement buildings classified by size category (hamlet, village,
      major village)
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
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts compared pre- and post-event Pleiades satellite imagery
    (7-8 August 2018) of Tanjung and Pemenang Districts following the 5 August 2018
    magnitude 6.9 earthquake in Lombok. Settlements were manually delineated and classified
    by size and damage level (moderately damaged, severely damaged, destroyed) through
    visual interpretation of structural changes visible in the satellite imagery.
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
- href: https://data.humdata.org/dataset/potentially-affected-settlements-over-tanjung-and-pemenang-districts-lombok-utara-regency-nusa-
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Direct building damage from 6.9 magnitude earthquake classified by
      damage level (moderately damaged, severely damaged, destroyed)
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
  description: Indonesia - Potentially affected settlements over Tanjung and Pemenang
    Districts, Lombok Utara Regency, Nusa Tenggara Barat Province (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/ID/EQ20180805IDN/EQ20180805IDN_shp.zip
  format: null
  id: resource_acb568a2
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EQ20180805IDN_shp.zip
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-idn_unosat_potentiallyaffectedsettle_20180810
spatial:
  bbox: null
  centroid: null
  countries:
  - IDN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2018-08-10'
temporal_resolution: null
title: Indonesia - Potentially affected settlements over Tanjung and Pemenang Districts,
  Lombok Utara Regency, Nusa Tenggara Barat Province
version: null
vulnerability: null
---
