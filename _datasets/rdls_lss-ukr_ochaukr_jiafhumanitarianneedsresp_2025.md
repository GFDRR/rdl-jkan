---
attributions:
- entity:
    affiliation: null
    email: null
    name: Humanitarian partners
    url: https://data.humdata.org/dataset/ukr-jiaf-humanitarian-needs-and-response-plan
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Ukraine
  url: https://data.humdata.org/dataset/ukr-jiaf-humanitarian-needs-and-response-plan
creator:
  affiliation: null
  email: null
  name: OCHA Ukraine
  url: https://data.humdata.org/dataset/ukr-jiaf-humanitarian-needs-and-response-plan
dataset_id: rdls_lss-ukr_ochaukr_jiafhumanitarianneedsresp_2025
description: 'The dataset provides a full breakdown of the affected population, PiN,
  severity and planned reach by strategic priority, cluster, and population group.
  As applicable, estimates of age and gender disaggregation are also included, along
  with estimates of people with disability. A detailed list of the HNRP activities
  is also included, along with a reference table for the units of analysis coded to
  ADM3 boundaries. Please refer to the dataset''s ReadMe tab for more details.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/ukr-jiaf-humanitarian-needs-and-response-plan]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Humanitarian partners conducted intersectoral needs assessments across
    Ukraine using the JIAF methodology to identify affected populations, people in
    need (PiN), and severity levels by strategic priority, cluster, and population
    group. Data was disaggregated by age, gender, and disability status, then coded
    to ADM3 administrative boundaries and compiled into consolidated HNRP (Humanitarian
    Needs and Response Plan) datasets for 2025 and 2026.
  sources:
  - id: source_1
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
- href: https://data.humdata.org/dataset/ukr-jiaf-humanitarian-needs-and-response-plan
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Total affected population requiring humanitarian assistance across
      all hazard contexts in Ukraine
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
        metric: exposure
        modelling: observed
        type: total
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: population
    asset_dimension: population
    description: Internally displaced persons (IDPs) identified in the humanitarian
      needs assessment
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_earthquake
      intensity_measure: PGA:g
      process: null
      trigger: null
      type: earthquake
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
  description: Ukraine - JIAF - HNRP - affected population, PiN, and planned reach
    by strategic priority, cluster, and population group, and SADD at the defined
    units of analysis.
  download_url: https://data.humdata.org/dataset/73c3eedb-d51d-478d-87ef-c5085422ef1b/resource/b377dea0-cb5a-48b1-9721-03aecff46896/download/jiaf_hnrp_ukraine_2026.xlsx
  format: null
  id: resource_b377dea0
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: JIAF_HNRP_Ukraine_2026.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Ukraine - JIAF - Re-Prioritized HNRP - PiN, Planned Reach by cluster
    and by activity at the ADM2 level. Deprioritized Activities.
  download_url: https://data.humdata.org/dataset/73c3eedb-d51d-478d-87ef-c5085422ef1b/resource/b7dade95-e14b-4249-a95f-2db37a06f782/download/jiaf_re-prioritized_hnrp_ukraine_2025.xlsx
  format: null
  id: resource_b7dade95
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: JIAF_Re-Prioritized_HNRP_Ukraine_2025.xlsx
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Ukraine - JIAF - HNRP - affected population, PiN, and planned reach
    by cluster, population group, and SADD at the ADM2 level.
  download_url: https://data.humdata.org/dataset/73c3eedb-d51d-478d-87ef-c5085422ef1b/resource/59a03ce0-c992-4045-bfe7-1f1dc5e7c3bc/download/jiaf_hnrp_ukraine_2025.xlsx
  format: null
  id: resource_59a03ce0
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: JIAF_HNRP_Ukraine_2025
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Ukraine: JIAF Humanitarian Needs and Response Plan (JIAF Methodology)'
  download_url: https://data.humdata.org/dataset/73c3eedb-d51d-478d-87ef-c5085422ef1b/resource/26582c4c-838d-49d5-8030-c5f0aa7b8285/download/jiaf-2-technical-manual_final-for-2025-hpc.pdf
  format: null
  id: resource_26582c4c
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: JIAF-2-Technical-Manual_Final-for-2025-HPC
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-ukr_ochaukr_jiafhumanitarianneedsresp_2025
spatial:
  bbox: null
  centroid: null
  countries:
  - UKR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-12-31'
  start: '2025-01-01'
temporal_resolution: null
title: 'Ukraine: JIAF Humanitarian Needs and Response Plan'
version: null
vulnerability: null
---
