---
attributions:
- entity:
    affiliation: null
    email: null
    name: United Nations Office for the Coordination of Humanitarian Affairs (UNOCHA)
    url: https://data.humdata.org/dataset/el-salvador-humanitarian-needs-overview
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Latin America and the Caribbean (ROLAC)
  url: https://data.humdata.org/dataset/el-salvador-humanitarian-needs-overview
creator:
  affiliation: null
  email: null
  name: OCHA Latin America and the Caribbean (ROLAC)
  url: https://data.humdata.org/dataset/el-salvador-humanitarian-needs-overview
dataset_id: rdls_lss-slv_ocharolac_humanitarianneedsoverview_2023
description: 'This data has been produced by the United Nations Office for the Coordination
  of Humanitarian Affairs (UNOCHA) on behalf of the Humanitarian Country Team and
  partners. The data provides the Humanitarian Country Team''s shared understanding
  of the crisis, including the most pressing humanitarian need and the estimated number
  of people who need assistance. It represents a consolidated evidence base and helps
  inform joint strategic response planning.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/el-salvador-humanitarian-needs-overview]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: Humanitarian needs data compiled by UNOCHA and humanitarian partners
    using the JIAF framework to estimate populations requiring assistance across sectors
    in El Salvador. The dataset consolidates multi-sectoral assessments into a shared
    evidence base for humanitarian response planning.
  sources:
  - id: source_1
    license: null
    name: United Nations Office for the Coordination of Humanitarian Affairs (UNOCHA)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/el-salvador-humanitarian-needs-overview
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: People in need of humanitarian assistance due to flood-related crisis
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
        metric: exposure
        modelling: observed
        type: total
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
  description: 'El Salvador: Humanitarian Needs Overview (El Salvador_data_de_PIN_sectoriales.xlsx)'
  download_url: https://data.humdata.org/dataset/ce5b1c0d-a9dc-44a5-9ede-8e8ddbbc17b8/resource/f7f637bc-8e1e-4da8-b8a3-e722c83f22c4/download/el-salvador_data_de_pin_sectoriales.xlsx
  format: null
  id: resource_f7f637bc
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: El Salvador_data_de_PIN_sectoriales.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-slv_ocharolac_humanitarianneedsoverview_2023
spatial:
  bbox: null
  centroid: null
  countries:
  - SLV
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2023-12-31'
  start: '2023-01-01'
temporal_resolution: null
title: 'El Salvador: Humanitarian Needs Overview'
version: null
vulnerability: null
---
