---
attributions:
- entity:
    affiliation: null
    email: null
    name: Joint Intersectoral Analysis Framework (JIAF)
    url: https://data.humdata.org/dataset/yem-jiaf-humanitarian-needs-and-response-plan
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Humanitarian partners
    url: https://data.humdata.org/dataset/yem-jiaf-humanitarian-needs-and-response-plan
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Yemen
  url: https://data.humdata.org/dataset/yem-jiaf-humanitarian-needs-and-response-plan
creator:
  affiliation: null
  email: null
  name: OCHA Yemen
  url: https://data.humdata.org/dataset/yem-jiaf-humanitarian-needs-and-response-plan
dataset_id: rdls_lss-yem_ochayem_jiafhumanitarianneedsresp_2025
description: 'The dataset provides a full breakdown of the affected population, people
  in need, severity, planned target by cluster, population group, and SADD at the
  ADM2 level.. [Source: This metadata record was automatically extracted from the
  Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/yem-jiaf-humanitarian-needs-and-response-plan]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: The dataset aggregates humanitarian needs assessments from multiple
    sectors using the JIAF methodology, which integrates data from humanitarian partners
    operating across Yemen. People in need figures are calculated at ADM2 (district)
    level and disaggregated by severity classification, population group (IDPs vs.
    residents), and demographic characteristics (age/gender), with planned response
    targets by cluster.
  sources:
  - id: source_1
    license: null
    name: Joint Intersectoral Analysis Framework (JIAF)
    risk_data_type:
    - loss
    type: model
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
- href: https://data.humdata.org/dataset/yem-jiaf-humanitarian-needs-and-response-plan
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: People in need affected by humanitarian crisis in Yemen, disaggregated
      by severity, population group, and administrative division
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
        metric: exposure
        modelling: observed
        type: total
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons (IDPs) identified as people in need
      in Yemen
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_drought
      intensity_measure: SPI:-
      process: null
      trigger: null
      type: drought
    id: loss_2
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: displaced
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
  description: Yemen - JIAF - HNRP - affected population, PiN, and planned by cluster,
    population group, and SADD at the ADM2 level.
  download_url: https://data.humdata.org/dataset/72077980-b6b2-41e4-bbaf-fe2cb9df7695/resource/28750f50-f323-4203-9793-f94f4c2d1c2b/download/yemen-hnrp-2025.xlsx
  format: null
  id: resource_28750f50
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: JIAF_HNRP_Yemen_2025
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Yemen: JIAF Humanitarian Needs and Response Plan (JIAF Methodology)'
  download_url: https://data.humdata.org/dataset/72077980-b6b2-41e4-bbaf-fe2cb9df7695/resource/df7f3ebe-9346-4c7c-847f-ed88c1e732ff/download/jiaf-2-technical-manual_final-for-2025-hpc.pdf
  format: null
  id: resource_df7f3ebe
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: JIAF-2-Technical-Manual_Final-for-2025-HPC.pdf
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-yem_ochayem_jiafhumanitarianneedsresp_2025
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
  end: '2025-12-31'
  start: '2025-01-01'
temporal_resolution: null
title: 'Yemen: JIAF Humanitarian Needs and Response Plan'
version: null
vulnerability: null
---
