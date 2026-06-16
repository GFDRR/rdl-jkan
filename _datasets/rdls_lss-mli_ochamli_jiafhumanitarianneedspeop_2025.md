---
attributions:
- entity:
    affiliation: null
    email: null
    name: Humanitarian partners
    url: https://data.humdata.org/dataset/mli-jiaf-humanitarian-needs-pin-and-severity
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Mali
  url: https://data.humdata.org/dataset/mli-jiaf-humanitarian-needs-pin-and-severity
creator:
  affiliation: null
  email: null
  name: OCHA Mali
  url: https://data.humdata.org/dataset/mli-jiaf-humanitarian-needs-pin-and-severity
dataset_id: rdls_lss-mli_ochamli_jiafhumanitarianneedspeop_2025
description: 'This dataset contains the overall people in need and intersectoral severity
  by disaggregation level which Includes administrative divisions and population groups,
  depending on each country''s decision. The dataset is produced by the United Nations
  for the Coordination of Humanitarian Affairs (OCHA) in collaboration with humanitarian
  partners using the Joint Intersectoral Analysis Framework(JIAF).. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/mli-jiaf-humanitarian-needs-pin-and-severity]'
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: The dataset aggregates people in need (PiN) and intersectoral severity
    assessments collected by humanitarian partners across Mali's administrative divisions
    and population groups. Data were compiled and analyzed using the Joint Intersectoral
    Analysis Framework (JIAF) methodology coordinated by OCHA Mali to produce standardized
    humanitarian needs overview figures for 2025.
  sources:
  - id: source_1
    license: null
    name: OCHA Mali
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
- href: https://data.humdata.org/dataset/mli-jiaf-humanitarian-needs-pin-and-severity
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: People in need (PiN) across intersectoral humanitarian clusters in
      Mali
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
  description: 'Mali: JIAF Humanitarian Needs People in Need and Severity (MLI - JIAF
    Humanitarian Needs People in Need and Severity 2025)'
  download_url: https://data.humdata.org/dataset/e68dd97e-08df-4973-a931-ab3a33170b26/resource/e982f7cf-f1e5-44fa-be6d-eee689e3d267/download/jiaf_mali_2025.xlsx
  format: null
  id: resource_e982f7cf
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: MLI_Humanitarian_Needs_PiN_and_Severity_2025
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mali: JIAF Humanitarian Needs People in Need and Severity (JIAF Methodology)'
  download_url: https://data.humdata.org/dataset/e68dd97e-08df-4973-a931-ab3a33170b26/resource/272fe7a6-c7a7-4e8d-8133-0437e701b02f/download/jiaf-2-technical-manual_final-for-2025-hpc.pdf
  format: null
  id: resource_272fe7a6
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: JIAF-2-Technical-Manual_Final-for-2025-HPC
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Mali: JIAF Humanitarian Needs People in Need and Severity (Hxlated
    version to enable Quick Charts)'
  download_url: https://data.humdata.org/dataset/e68dd97e-08df-4973-a931-ab3a33170b26/resource/cd244257-deaf-427c-aa10-60ed7e0dec32/download/jiaf_mali_2025_hxl.csv
  format: null
  id: resource_cd244257
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: jiaf_mali_2025_hxl
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-mli_ochamli_jiafhumanitarianneedspeop_2025
spatial:
  bbox: null
  centroid: null
  countries:
  - MLI
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2025-12-08'
  start: '2025-01-01'
temporal_resolution: null
title: 'Mali: JIAF Humanitarian Needs People in Need and Severity'
version: null
vulnerability: null
---
