---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/iom-dtm-mosul-crisis-baseline-data
creator:
  affiliation: null
  email: null
  name: International Organization for Migration (IOM)
  url: https://data.humdata.org/dataset/iom-dtm-mosul-crisis-baseline-data
dataset_id: rdls_lss-irq_iom_dtmmosulcrisisbaselinedat_20161024
description: 'The Emergency Tracking (ET) system aims at tracking sudden displacement
  or return movements triggered by emerging crises. The ET is a crisis-based tool.
  It does not depend on the location of displacement or return, only on the cause
  of that movement. The ET figures are not cumulative of the all persons affected
  by the Mosul crisis thus far, rather the ET update provides only a snapshot of the
  current displacement situation for the indicated date. The data and information
  reported on this page are related solely to the displacement caused by the Mosul
  operations which started on 17 October 2016. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/iom-dtm-mosul-crisis-baseline-data]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: IOM Emergency Tracking system collected displacement and return movement
    data via census methodology during the Mosul crisis starting October 17, 2016.
    The dataset provides point-in-time snapshots of displacement situations rather
    than cumulative figures, tracking population movements caused by military operations.
  sources:
  - id: source_1
    license: null
    name: International Organization for Migration (IOM)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/iom-dtm-mosul-crisis-baseline-data
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population displacement caused by Mosul military operations (October
      2016 onwards)
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
        metric: displaced
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
purpose: Census
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Iraq - IOM DTM - Mosul crisis Baseline data (Excel)
  download_url: https://data.humdata.org/dataset/956be982-5d90-4bb6-bde0-5eba2ec59ce9/resource/e8781248-0a94-4e15-bfd1-c76597a89ee1/download/emergencytracking_dtm_iom_idps_dataset.xls
  format: null
  id: resource_e8781248
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: EmergencyTracking_DTM_IOM_IDPs_Dataset.xls
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-irq_iom_dtmmosulcrisisbaselinedat_20161024
spatial:
  bbox: null
  centroid: null
  countries:
  - IRQ
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2016-10-24'
temporal_resolution: null
title: Iraq - IOM DTM - Mosul crisis Baseline data
version: null
vulnerability: null
---
