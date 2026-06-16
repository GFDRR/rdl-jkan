---
attributions:
- entity:
    affiliation: null
    email: null
    name: United Nations Office for the Coordination of Humanitarian Affairs (UNOCHA)
    url: https://data.humdata.org/dataset/guatemala-humanitarian-needs-overview
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Humanitarian partners
    url: https://data.humdata.org/dataset/guatemala-humanitarian-needs-overview
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Latin America and the Caribbean (ROLAC)
  url: https://data.humdata.org/dataset/guatemala-humanitarian-needs-overview
creator:
  affiliation: null
  email: null
  name: OCHA Latin America and the Caribbean (ROLAC)
  url: https://data.humdata.org/dataset/guatemala-humanitarian-needs-overview
dataset_id: rdls_lss-gtm_ocharolac_humanitarianneedsoverview_2023
description: 'This data has been produced by the United Nations Office for the Coordination
  of Humanitarian Affairs (UNOCHA) on behalf of the Humanitarian Country Team and
  partners. The data provides the Humanitarian Country Team''s shared understanding
  of the crisis, including the most pressing humanitarian need and the estimated number
  of people who need assistance. It represents a consolidated evidence base and helps
  inform joint strategic response planning.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/guatemala-humanitarian-needs-overview]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: The dataset aggregates humanitarian needs assessments from multiple
    partners in Guatemala using the Joint and Intersectoral Analysis Framework (JIAF)
    v1.1 methodology. Field data on affected populations and humanitarian needs were
    consolidated by UNOCHA to produce people-in-need (PiN) estimates across multiple
    crisis drivers, supporting joint strategic response planning by the Humanitarian
    Country Team.
  sources:
  - id: source_1
    license: null
    name: United Nations Office for the Coordination of Humanitarian Affairs (UNOCHA)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: Humanitarian partners
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/guatemala-humanitarian-needs-overview
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: People in need due to flood-related humanitarian crisis in Guatemala
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
  - asset_category: population
    asset_dimension: population
    description: People in need due to strong wind/cyclone-related humanitarian crisis
      in Guatemala
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
    id: loss_2
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
  description: The dataset contains information on the number of people in need in
    Guatemala in 2023.
  download_url: https://data.humdata.org/dataset/4f7e8d59-2866-4e0b-a6dd-514579f611a3/resource/cb5e5337-b4da-404a-8a90-8c088eb6b74d/download/jiaf1.1_aggregation_scenario-b_guatemala_220915.xlsx
  format: null
  id: resource_cb5e5337
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: JIAF1.1_PiN_Aggregation_Guatemala_220915.xlsx
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-gtm_ocharolac_humanitarianneedsoverview_2023
spatial:
  bbox: null
  centroid: null
  countries:
  - GTM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2023-12-31'
  start: '2023-01-01'
temporal_resolution: null
title: 'Guatemala: Humanitarian Needs Overview'
version: null
vulnerability: null
---
