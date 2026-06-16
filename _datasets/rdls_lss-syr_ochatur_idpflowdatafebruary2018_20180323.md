---
attributions:
- entity:
    affiliation: null
    email: null
    name: OCHA Turkey
    url: https://data.humdata.org/dataset/syria-idp-flow-data-february-2018
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: OCHA Jordan
    url: https://data.humdata.org/dataset/syria-idp-flow-data-february-2018
  id: attribution_2
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: OCHA Damascus
    url: https://data.humdata.org/dataset/syria-idp-flow-data-february-2018
  id: attribution_3
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: PMI
    url: https://data.humdata.org/dataset/syria-idp-flow-data-february-2018
  id: attribution_4
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: CCCM Cluster
    url: https://data.humdata.org/dataset/syria-idp-flow-data-february-2018
  id: attribution_5
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: "OCHA T\xFCrkiye (inactive)"
  url: https://data.humdata.org/dataset/syria-idp-flow-data-february-2018
creator:
  affiliation: null
  email: null
  name: "OCHA T\xFCrkiye (inactive)"
  url: https://data.humdata.org/dataset/syria-idp-flow-data-february-2018
dataset_id: rdls_lss-syr_ochatur_idpflowdatafebruary2018_20180323
description: 'Data contains Syria IDP arrival estimations for February 2018, January
  2016-February 2018 summary and table shows origin to destination estimation by governorate
  for February2018.. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/syria-idp-flow-data-february-2018]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/publicdomain/zero/1.0/
lineage:
  description: IDP flow data consolidated from multiple OCHA regional hubs (Turkey,
    Jordan, Damascus), PMI, and CCCM cluster, each applying their own defined methodology
    for displacement tracking. Data aggregated to provide governorate-level origin-destination
    matrices and monthly arrival estimations.
  sources:
  - id: source_1
    license: null
    name: OCHA Turkey
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: OCHA Jordan
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_3
    license: null
    name: OCHA Damascus
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_4
    license: null
    name: PMI
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_5
    license: null
    name: CCCM Cluster
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/syria-idp-flow-data-february-2018
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Internal displacement flows showing IDP arrivals and origin-destination
      movements by governorate during Syrian conflict
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
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Data contains Syria IDP arrival estimations for February 2018, January
    2016-February 2018 summary and table shows origin to destination estimation by
    governorate for February2018.
  download_url: https://data.humdata.org/dataset/672df142-2353-4035-b92a-8139c9de6e48/resource/b474634a-8e95-4997-a90b-0f3b3da992b3/download/idp_flowdata_share_feb2018.xlsx
  format: null
  id: resource_b474634a
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: IDP_flowData_share_Feb2018.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-syr_ochatur_idpflowdatafebruary2018_20180323
spatial:
  bbox: null
  centroid: null
  countries:
  - SYR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2018-03-23'
temporal_resolution: null
title: Syria IDP flow data - February 2018
version: null
vulnerability: null
---
