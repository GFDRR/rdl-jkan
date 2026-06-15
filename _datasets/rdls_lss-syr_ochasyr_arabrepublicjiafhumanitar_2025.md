---
attributions:
- entity:
    affiliation: null
    email: null
    name: United Nations Office for the Coordination of Humanitarian Affairs (OCHA)
    url: https://data.humdata.org/dataset/syr-jiaf-humanitarian-needs-pin-and-severity
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Humanitarian partners
    url: https://data.humdata.org/dataset/syr-jiaf-humanitarian-needs-pin-and-severity
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Syria
  url: https://data.humdata.org/dataset/syr-jiaf-humanitarian-needs-pin-and-severity
creator:
  affiliation: null
  email: null
  name: OCHA Syria
  url: https://data.humdata.org/dataset/syr-jiaf-humanitarian-needs-pin-and-severity
dataset_id: rdls_lss-syr_ochasyr_arabrepublicjiafhumanitar_2025
description: 'This dataset contains the overall people in need and intersectoral severity
  by disaggregation level which Includes administrative divisions and population groups,
  depending on each country''s decision. The dataset is produced by the United Nations
  for the Coordination of Humanitarian Affairs (OCHA) in collaboration with humanitarian
  partners using the Joint Intersectoral Analysis Framework(JIAF).. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/syr-jiaf-humanitarian-needs-pin-and-severity]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Humanitarian partners conducted field assessments and data collection
    across Syrian administrative divisions and population groups. OCHA compiled and
    integrated these data using the Joint Intersectoral Analysis Framework (JIAF)
    methodology to produce standardized estimates of people in need and intersectoral
    severity for humanitarian response planning.
  sources:
  - id: source_1
    license: null
    name: United Nations Office for the Coordination of Humanitarian Affairs (OCHA)
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
- href: https://data.humdata.org/dataset/syr-jiaf-humanitarian-needs-pin-and-severity
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: People in need across Syria by administrative division and population
      group, assessed through intersectoral analysis
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
  description: 'Syrian Arab Republic: JIAF Humanitarian Needs People in Need and Severity
    (SYR - JIAF Humanitarian Needs People in Need and Severity 2025)'
  download_url: https://data.humdata.org/dataset/bae87b26-a97f-4f7e-8aa1-78a628229d12/resource/9173c283-4617-430a-a456-1e23270f1934/download/jiaf_syria_2025.xlsx
  format: null
  id: resource_9173c283
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SYR_Humanitarian_Needs_PiN_and_Severity_2025
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Syrian Arab Republic: JIAF Humanitarian Needs People in Need and Severity
    (JIAF Methodology)'
  download_url: https://data.humdata.org/dataset/bae87b26-a97f-4f7e-8aa1-78a628229d12/resource/2da0c303-9e15-40b2-9f51-9d8da271234e/download/jiaf-2-technical-manual_final-for-2025-hpc.pdf
  format: null
  id: resource_2da0c303
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
slug: rdls_lss-syr_ochasyr_arabrepublicjiafhumanitar_2025
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
  end: '2025-12-31'
  start: '2025-04-24'
temporal_resolution: null
title: 'Syrian Arab Republic: JIAF Humanitarian Needs People in Need and Severity'
version: null
vulnerability: null
---
