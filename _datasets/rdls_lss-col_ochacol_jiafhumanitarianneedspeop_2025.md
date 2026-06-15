---
attributions:
- entity:
    affiliation: null
    email: null
    name: United Nations Office for the Coordination of Humanitarian Affairs (OCHA)
    url: https://data.humdata.org/dataset/col-jiaf-humanitarian-needs-pin-and-severity
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Humanitarian partners
    url: https://data.humdata.org/dataset/col-jiaf-humanitarian-needs-pin-and-severity
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OCHA Colombia
  url: https://data.humdata.org/dataset/col-jiaf-humanitarian-needs-pin-and-severity
creator:
  affiliation: null
  email: null
  name: OCHA Colombia
  url: https://data.humdata.org/dataset/col-jiaf-humanitarian-needs-pin-and-severity
dataset_id: rdls_lss-col_ochacol_jiafhumanitarianneedspeop_2025
description: 'This dataset contains the overall people in need and intersectoral severity
  by disaggregation level which Includes administrative divisions and population groups,
  depending on each country''s decision. The dataset is produced by the United Nations
  for the Coordination of Humanitarian Affairs (OCHA) in collaboration with humanitarian
  partners using the Joint Intersectoral Analysis Framework(JIAF).. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/col-jiaf-humanitarian-needs-pin-and-severity]'
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: The dataset aggregates humanitarian needs assessments from OCHA and
    humanitarian partners using the Joint Intersectoral Analysis Framework (JIAF)
    methodology to produce people in need (PiN) and intersectoral severity estimates
    disaggregated by administrative divisions and population groups across Colombia.
    The JIAF integrates multi-sectoral analysis to classify humanitarian impact and
    vulnerability.
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
- href: https://data.humdata.org/dataset/col-jiaf-humanitarian-needs-pin-and-severity
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: People in need and intersectoral severity assessment across Colombia
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
  description: 'Colombia: JIAF Humanitarian Needs People in Need and Severity (COL
    - JIAF Humanitarian Needs People in Need and Severity 2025)'
  download_url: https://data.humdata.org/dataset/60968264-b405-4a6e-931d-8e2acffb5681/resource/89b708e4-0ff0-4c23-97e7-3100273e687c/download/jiaf_colombia_2025.xlsx
  format: null
  id: resource_89b708e4
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: COL_Humanitarian_Needs_PiN_and_Severity_2025
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Colombia: JIAF Humanitarian Needs People in Need and Severity (JIAF
    Methodology)'
  download_url: https://data.humdata.org/dataset/60968264-b405-4a6e-931d-8e2acffb5681/resource/08efe89f-c26a-4e97-aee1-0fe9088b96b0/download/jiaf-2-technical-manual_final-for-2025-hpc.pdf
  format: null
  id: resource_08efe89f
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
  description: 'Colombia: JIAF Humanitarian Needs People in Need and Severity (Hxlated
    version to enable Quick Charts)'
  download_url: https://data.humdata.org/dataset/60968264-b405-4a6e-931d-8e2acffb5681/resource/54ad4e8c-4300-4080-90d0-c0ea2d54ce2c/download/jiaf_colombia_2025_hxl.csv
  format: null
  id: resource_54ad4e8c
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: JIAF_Colombia_2025_hxl
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-col_ochacol_jiafhumanitarianneedspeop_2025
spatial:
  bbox: null
  centroid: null
  countries:
  - COL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2025-12-31'
  start: '2025-01-01'
temporal_resolution: null
title: 'Colombia: JIAF Humanitarian Needs People in Need and Severity'
version: null
vulnerability: null
---
